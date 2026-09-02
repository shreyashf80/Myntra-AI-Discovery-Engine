import logging
import json
import textwrap
from typing import List
from src.shared.schemas import RetrievedItem, SynthesisResult
from src.shared.llm import llm_client

logger = logging.getLogger(__name__)

class Synthesizer:
    SYSTEM_PROMPT = """You are a qualitative researcher analyzing user feedback for Myntra.
You will be provided with a user's question and a list of anonymized feedback snippets from various sources.

YOUR GOAL:
Synthesize a clear, structured answer based ONLY on the provided context. Connect the user journey sequentially where possible: Saved → What happened next? → Uncertainty → Workaround → Outcome.

RULES:
1. FOCUS ON BEHAVIOR: Answer the actual question. Highlight decision breakdowns, uncertainties, and what users do outside the platform.
2. NO AUTOMATED SOLUTIONS: Do NOT brainstorm product features, opportunity scores, or UI solutions. Report the objective behavior.
3. CONTRADICTIONS & GAPS: If the evidence is weak, contradictory, or too generic, state "No clear opportunity" or explain the contradiction. Do not manufacture a problem.
4. QUANTIFICATION: If you make quantified claims, explicitly state the proportion from the context.
5. NO HALLUCINATION: If the context lacks data to answer the question, state that clearly.
6. ABSOLUTE PRIVACY: NEVER mention user names, author names, handles, IDs, or any identifying information.
7. ABSOLUTELY NO INLINE CITATIONS: The answer must read as a clean narrative. Do NOT include reference markers like [1]. The evidence section is separate.

OUTPUT FORMAT:
Return ONLY a valid JSON object. Do not wrap in markdown blockquotes like ```json.
CRITICAL: The `answer` field must be a valid JSON string. All newlines in the markdown must be properly escaped as `\n`. Do NOT output raw unescaped newlines inside the JSON string.
{
  "answer": "Your detailed markdown-formatted answer... Use \\n for newlines.",
  "evidence": [
    {"snippet": "A short, anonymized direct quote from user feedback (max 2 sentences)", "source": "app_store or play_store or reddit or youtube"},
    {"snippet": "Another relevant quote", "source": "source_name"}
  ]
}

The "evidence" array should contain 3 to 5 of the most compelling, anonymized direct quotes from the context that back up your answer. Strip any names or IDs from the quotes.
"""

    @classmethod
    async def synthesize(cls, question: str, retrieved: List[RetrievedItem]) -> SynthesisResult:
        if not retrieved:
            return SynthesisResult(
                answer="I couldn't find any relevant insights for that question in the database.",
                citations=[],
                source_breakdown={},
                llm_used="none"
            )
            
        context_blocks = []
        source_counts = {}
        
        for i, item in enumerate(retrieved):
            source = item.source
            source_counts[source] = source_counts.get(source, 0) + 1
            
            # Only pass the snippet text and the source platform — NO IDs, NO metadata with names
            context_blocks.append(f"[Feedback {i+1} from {source}]\n{item.source_snippet}")
            
        user_prompt = f"USER QUESTION: {question}\n\nRETRIEVED FEEDBACK ({len(retrieved)} snippets):\n" + "\n\n".join(context_blocks)
        
        try:
            response = await llm_client.complete(system=cls.SYSTEM_PROMPT, user=user_prompt)
            content = response.content.strip()
            if content.startswith("```json"): content = content[7:]
            if content.startswith("```"): content = content[3:]
            if content.endswith("```"): content = content[:-3]
            
            result_json = json.loads(content)
            
            # Map evidence to citations format
            evidence = result_json.get("evidence", [])
            citations = [{"snippet": textwrap.dedent(e.get("snippet", "")), "source": e.get("source", "unknown")} for e in evidence]
            
            import re
            answer_text = result_json.get("answer", "")
            # Aggressively strip leading whitespace from every line to prevent code block rendering
            answer_text = re.sub(r'^[ \t]+', '', answer_text, flags=re.MULTILINE)
            
            return SynthesisResult(
                answer=answer_text,
                citations=citations,
                source_breakdown=source_counts,
                llm_used=response.llm_used
            )
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Synthesis failed: {error_msg}")
            
            # Formulate a helpful message based on the error
            if "429" in error_msg or "503" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "unavailable" in error_msg.lower() or "high demand" in error_msg.lower():
                display_answer = "The AI service is temporarily unavailable due to high demand. Please try again in a moment."
            else:
                display_answer = f"Sorry, I encountered an error while synthesizing the answer: {error_msg}"
                
            return SynthesisResult(
                answer=display_answer,
                citations=[],
                source_breakdown=source_counts,
                llm_used="error"
            )

class BatchSynthesizer:
    SYSTEM_PROMPT = """You are a qualitative researcher analyzing user feedback for Myntra.
You will be provided with 5 specific discovery questions about wishlist-to-purchase behavior, and a combined list of retrieved snippets from various sources.

YOUR GOAL:
1. Answer ALL 5 seed questions based ONLY on the provided context. Connect the user journey sequentially where possible (Saved → Uncertainty → Workaround → Outcome).
2. Identify 3 to 5 'Emergent Themes' that appear in the citations but are NOT directly covered by the standard questions.

RULES:
1. FOCUS ON BEHAVIOR: Do NOT brainstorm solutions, UI ideas, or opportunity scores. Report objective behavior.
2. CONTRADICTIONS & GAPS: If the evidence is weak, contradictory, or unrelated to wishlist behavior, explicitly state "No clear opportunity" for that segment. Do not manufacture problems.
3. NO HALLUCINATION: If the context lacks data to answer a specific question, state that you don't have enough data for that question.
4. PRIVACY: NEVER mention user names, author names, or handles in the output.
5. NO CITATIONS: Do not include references or citations in the text. Provide a seamless answer.

OUTPUT FORMAT:
Return ONLY a valid JSON object. Do not wrap in markdown blockquotes like ```json.
CRITICAL: The `answer` field must be a valid JSON string. All newlines in the markdown must be properly escaped as `\n`. Do NOT output raw unescaped newlines inside the JSON string.
{
  "summaries": [
    {
      "question": "Exact text of the question",
      "answer": "Your detailed markdown-formatted answer structured for a Product Manager.",
      "confidence": "High, Medium, or Low (Rate High if >3 sources back this up, Low if <2)"
    }
  ],
  "emergent_themes": [
    "theme 1",
    "theme 2",
    "theme 3"
  ]
}
"""

    @classmethod
    async def synthesize_batch(cls, questions: List[str], all_retrieved: List[RetrievedItem]) -> dict:
        context_blocks = []
        source_counts = {}
        
        for i, item in enumerate(all_retrieved):
            source = item.source
            source_counts[source] = source_counts.get(source, 0) + 1
            context_blocks.append(f"[Feedback {i+1} from {source}]\n{item.source_snippet}")
            
        questions_block = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])
        user_prompt = f"SEED QUESTIONS TO ANSWER:\n{questions_block}\n\nRETRIEVED CONTEXT:\n" + "\n\n".join(context_blocks)
        
        try:
            response = await llm_client.complete(system=cls.SYSTEM_PROMPT, user=user_prompt)
            content = response.content.strip()
            if content.startswith("```json"): content = content[7:]
            if content.startswith("```"): content = content[3:]
            if content.endswith("```"): content = content[:-3]
            
            result_json = json.loads(content)
            
            # Dedent answers to prevent code block rendering
            import re
            if "summaries" in result_json:
                for summary in result_json["summaries"]:
                    if "answer" in summary:
                        summary["answer"] = re.sub(r'^[ \t]+', '', summary["answer"], flags=re.MULTILINE)
                        
            result_json["source_counts"] = source_counts
            return result_json
        except Exception as e:
            error_msg = str(e)
            logger.error(f"Batch Synthesis failed: {error_msg}")
            
            # Formulate a helpful message based on the error
            if "429" in error_msg or "503" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "unavailable" in error_msg.lower() or "high demand" in error_msg.lower():
                display_answer = "The AI service is temporarily unavailable due to high demand. Please try again in a moment."
            else:
                display_answer = f"Sorry, I encountered an error while synthesizing the batch answer: {error_msg}"
                
            return {"error": display_answer}
