import urllib.request
import json
import time

questions = [
    "Why do users add fashion products to their wishlist?",
    "What prevents wishlisted products from eventually being purchased?",
    "What uncertainties remain after users have identified a product they like?",
    "What causes users to postpone a purchase?",
    "How do users compare multiple shortlisted products?",
    "What information do users seek outside Myntra/AJIO before purchasing?",
    "What role do fit, size, styling, price, reviews, occasion and social validation play?",
    "When do users use the wishlist as genuine purchase intent versus simply as a bookmarking mechanism?",
    "How do these behaviors differ across user segments?",
    "What unmet needs emerge consistently across user conversations?"
]

results = []

for idx, q in enumerate(questions, 1):
    print(f"[{idx}/10] Querying: {q}")
    req_data = json.dumps({"question": q}).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:8000/api/chat",
        data=req_data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            citations = data.get("citations", [])
            results.append({
                "index": idx,
                "question": q,
                "answer": data.get("answer", ""),
                "citations": citations,
                "source_breakdown": data.get("source_breakdown", {}),
                "llm_used": data.get("llm_used", "gemini")
            })
            print(f"  -> Answered ({len(citations)} citations)")
    except Exception as e:
        print(f"  -> Error: {e}")
        results.append({
            "index": idx,
            "question": q,
            "answer": f"Error querying engine: {e}",
            "citations": [],
            "source_breakdown": {},
            "llm_used": "error"
        })
    
    time.sleep(3)

# Build Markdown
md_lines = ["# Myntra Discovery Engine — Core Research Answers\n\n"]
md_lines.append(f"*Generated automatically on {time.strftime('%Y-%m-%d %H:%M:%S')} via Myntra AI Discovery Engine RAG Pipeline*\n\n---\n\n")

for item in results:
    md_lines.append(f"## {item['index']}. {item['question']}\n\n")
    md_lines.append(f"{item['answer']}\n\n")
    
    if item["source_breakdown"]:
        sources_str = ", ".join([f"**{k}**: {v}" for k, v in item["source_breakdown"].items()])
        md_lines.append(f"**Evidence Breakdown:** {sources_str}\n\n")
        
    if item["citations"]:
        md_lines.append("### Key Evidence Citations\n\n")
        for cit in item["citations"]:
            source_tag = cit.get("source", "source").upper()
            snippet = cit.get("snippet", "").strip().replace("\n", " ")
            md_lines.append(f"- **[{source_tag}]** \"_{snippet}_\"\n")
        md_lines.append("\n")
        
    md_lines.append("---\n\n")

with open("RESEARCH_ANSWERS.md", "w") as f:
    f.writelines(md_lines)

print("Finished! Saved all 10 answers to RESEARCH_ANSWERS.md")
