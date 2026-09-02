# Myntra Discovery Engine — Core Research Answers

*Generated automatically on 2026-08-21 00:52:27 via Myntra AI Discovery Engine RAG Pipeline*

---

## 1. Why do users add fashion products to their wishlist?

Based on the provided feedback, users add fashion products to their wishlist for three primary behavioral reasons, following a sequential pattern from saving to decision breakdown:

### Reasons for Adding Items to Wishlist

1. **Aspirational & Unplanned Saving**
* **Saved:** Users add items (e.g., dresses or tops) to their wishlist during casual scrolling simply because they find the outfit appealing, rather than having a specific event or immediate need planned.
* **What Happened Next:** Items accumulate in the wishlist over time without purchase action.
* **Outcome:** Users eventually conduct periodic wishlist cleanups and realize that a significant portion (noted as half in 1 out of 20 snippets) of saved items were added impulsively without any concrete intention to purchase.

2. **Price Tracking & Discount Monitoring**
* **Saved:** Users place items in their wishlist to monitor price drops and sale discounts.
* **What Happened Next:** Users revisit their wishlist when search views or notifications indicate that prices have decreased.
* **Uncertainty & Breakdown:** When opening the wishlisted item to select a size, users experience a breakdown where the advertised price drop reverts, showing a lower discount than expected on the product page (1 out of 20 snippets).
* **Outcome:** Price discrepancies between the search/wishlist list view and the size selection screen disrupt the purchasing flow.

3. **Curation for External Recommendations**
* **Saved:** Users build up collections of saved items over extended browsing sessions.
* **Outcome:** Users leverage their accumulated wishlists as references or suggestions for others to review or cover (1 out of 20 snippets).

### Data Gaps
Much of the retrieved context focuses on broader shopping friction (such as sizing uncertainty, innerwear return policies, and catalog repetition) rather than wishlist usage. Direct motivations for wishlisting in this context are strictly limited to impulsive bookmarking, price monitoring, and curation.

**Evidence Breakdown:** **reddit**: 13, **youtube**: 6, **app_store**: 1

### Key Evidence Citations

- **[REDDIT]** "_I was cleaning my wishlist yesterday and realised half the clothes I save are not for anything I actually have planned like I’ll see a cute top or a dress on Savana or myntra_"
- **[REDDIT]** "_Myntra doing this to everything in my wish list. Shows prices went down! Actual search page says prices went down, but the minute you open the product to select size, the discount goes down._"
- **[YOUTUBE]** "_I have lot of wishlist stuff if you want I'll suggest you to cover those._"

---

## 2. What prevents wishlisted products from eventually being purchased?

### User Journey: Wishlist to Purchase Breakdown

#### 1. Saved (Initial Intent)
Users save items to their wishlist to curate potential purchases, hold pre-approved options for gifts, or track price drops over time.

#### 2. What Happened Next? (Friction at Checkout)
When users attempt to transition a wishlisted item to purchase, clear technical and operational breakdowns halt the transaction:
- **Dynamic Price Discrepancies:** Users experience price jumps when attempting to select a size. While search and wishlist pages indicate a price drop, opening the product detail view to pick a size causes the discount to diminish, increasing the final cost (1 out of 20 snippets).
- **Sudden Pincode Unavailability:** Items saved in the wishlist suddenly become unserviceable for delivery to the user's location right as they attempt to buy, especially during major sale events (1 out of 20 snippets).
- **Stock Exhaustion:** Items go out of stock before the transaction can be completed (2 out of 20 snippets).

#### 3. Uncertainty (Fulfillment & Support Concerns)
Conversion from wishlist to order is further limited by distrust stemming from past platform experiences. Users express hesitation due to non-returnable delivery policies for specific pincodes, unannounced post-order cancellations by the platform, and unresolved customer support issues (5 out of 20 snippets).

#### 4. Workarounds & Outcome
- **Platform Switching:** When faced with return policy risks or customer support doubts, users abandon their wishlisted items on Myntra and execute purchases on alternative e-commerce platforms like Amazon or Flipkart (1 out of 20 snippets).
- **External Re-linking:** When wishlisted items become unavailable, users rely on external content creators to share direct re-stock links instead of depending on platform notifications (2 out of 20 snippets).
- **Outcome:** Wishlisted items remain unpurchased, leading to cart abandonment or customer migration to external platforms.

**Evidence Breakdown:** **app_store**: 3, **play_store**: 3, **reddit**: 5, **youtube**: 9

### Key Evidence Citations

- **[REDDIT]** "_Shows prices went down! Actual search page says prices went down, but the minute you open the product to select size, the discount goes down._"
- **[REDDIT]** "_The outfit which was just available just magically isn't shipping to my pincode anymore. This has been going on for a while now but having the same experience during their so-called biggest sale_"
- **[APP_STORE]** "_buy product from Flipkart and Amazon only if get wrong product they don’t return it or you can’t connect with customer care_"
- **[YOUTUBE]** "_maybe the product got out of stock, so youtube removed that product, it will come back once the product is in stock_"

---

## 3. What uncertainties remain after users have identified a product they like?

### Key Uncertainties After Identifying a Product

Once users find a product they like, their decision to purchase breaks down due to several critical uncertainties:

1. **Product Fidelity & Quality Discrepancies**
Users experience doubt about whether the physical item will match the online photos or copy. Concerns exist around receiving counterfeit, cheap, or defective variations of the advertised product, particularly when product links lead to mismatched items.

2. **Trustworthiness & Availability of Reviews**
To validate their choice, users rely on ratings and reviews. However, uncertainty arises when platforms lack reviews entirely, or when users suspect review moderation bias (e.g., negative reviews being rejected or removed). Approximately 15% of the feedback explicitly mentions a breakdown in trust regarding customer reviews.

3. **Return Policy Restrictions & Refund Logistics**
A significant source of friction (highlighted in roughly 25% of the feedback) revolves around post-purchase logistics. Users worry about location-based restrictions (such as non-returnable pincodes), unhandled return pickups, and unhelpful customer service if a refund is required.

---

### User Journey & Workarounds

* **Saved / Identified Item** → User finds an item they like via media, wishlist, or catalog.
* **Uncertainty & Breakdown** → Doubts arise over fabric quality, review authenticity, mismatching listings, or returnability.
* **Workarounds** → 
* Users scrutinize specific product details (such as fabric breakdown) before committing.
* Users actively request direct peer feedback in comment sections ("share your experience if you buy it").
* Users consult external community forums (e.g., Reddit) to ask if buying through a specific marketplace circumvents return or support issues.
* **Outcome** → Users either delay purchase, abandon the order, or buy with hesitation.

**Evidence Breakdown:** **app_store**: 4, **youtube**: 10, **reddit**: 5, **play_store**: 1

### Key Evidence Citations

- **[APP_STORE]** "_At many places the product varies from the copy. Which is misleading to the customers_"
- **[REDDIT]** "_I now see that my review was rejected??? On what basis??... How can I trust reviews on any product? It’s just so shady._"
- **[REDDIT]** "_I heard issues regarding returns, customer support. Will ordering via Myntra etc circumvent this issue ?_"
- **[YOUTUBE]** "_telling that the product is not returnable in my pincode_"
- **[YOUTUBE]** "_check details of product first like fabric, etc._"

---

## 4. What causes users to postpone a purchase?

Based on the provided user feedback, the decision to postpone or hesitate on a purchase on Myntra follows a sequential breakdown triggered by price inconsistencies, delivery anxieties, and fulfillment mistrust:

### 1. Saved / Browsing Phase
Users save items to their wishlist or browse search result pages where products display attractive discounted prices.

### 2. What Happened Next?
When proceeding to purchase, users encounter sudden friction:
* **Price Disparity at Size Selection:** Upon clicking into the product page to select a size, the price increases as the discount drops compared to what was shown on the wishlist or search feed (1 out of 20 snippets, 5%).
* **Sudden Shipping Restrictions:** Items previously listed as available suddenly show as non-deliverable to the user's pincode, especially during sale events (1 out of 20 snippets, 5%).

### 3. Uncertainty & Hesitation
* **Time-Sensitive Delivery Anxiety:** When purchasing for specific events (e.g., birthdays), delayed dispatch timelines create anxiety over whether the outfit will arrive on time or fit properly (1 out of 20 snippets, 5%).
* **Fulfillment & Return Mistrust:** Broader concerns around unannounced order cancellations, logistics delays, price increases on re-orders, and refund friction build hesitation, causing users to second-guess placing orders (15 out of 20 snippets, 75%).

### 4. Workarounds Outside the Platform
To mitigate risk, users turn to external community forums (such as Reddit) to evaluate platform reliability or actively consider off-platform alternatives, such as canceling delayed orders to buy backup outfits elsewhere.

### 5. Outcome
Transactions are stalled, abandoned, or diverted to alternative stores due to loss of price transparency and delivery assurance.

**Evidence Breakdown:** **youtube**: 8, **play_store**: 5, **app_store**: 2, **reddit**: 5

### Key Evidence Citations

- **[REDDIT]** "_Myntra doing this to everything in my wish list. Shows prices went down! Actual search page says prices went down, but the minute you open the product to select size, the discount goes down._"
- **[REDDIT]** "_Order isn’t dispatched yet and delivery shows 10 Feb (one day before my birthday). Do I cancel now and buy a backup, or wait and risk it being late or not fitting?_"
- **[REDDIT]** "_The outfit which was just available just magically isn't shipping to my pincode anymore. This has been going on for a while now but having the same experience during their so-called biggest sale_"
- **[YOUTUBE]** "_Myntra sale is a scam they take order in sale than cancel the order under the reason of logistics. They will then tell you if you want the product re-order it with increased price applicable._"
- **[REDDIT]** "_I heard issues regarding returns, customer support. Will ordering via Myntra etc circumvent this issue ?_"

---

## 5. How do users compare multiple shortlisted products?

### User Comparison Journey & Behavioral Breakdown

When evaluating and comparing shortlisted products, users follow a multi-step process driven by cross-platform research, seller scrutiny, and external validation.

#### 1. Discovery & Shortlisting
Users identify candidate products across multiple platforms (such as Myntra, Ajio, Amazon, Savana) or via third-party video showcases (such as YouTube haul videos). During this initial phase, users gather links and shortlist similar items across sellers and brands.

#### 2. Comparison Criteria & Attribute Checking
Once products are shortlisted, users evaluate specific attributes to differentiate options:
* **Product Specifications:** Users scrutinize fabric details, product descriptions, and display specifications (size and price).
* **Seller & Price Variances:** Users actively compare pricing for identical or similar items offered by different sellers or across competing platforms.
* **Brand vs. Quality Comparison:** Users evaluate whether items from the same brand across different platforms maintain identical quality or if price differences signal duplicate/counterfeit products.

#### 3. Breakdown & Uncertainties
During comparison, decision-making frequently breaks down due to key uncertainties:
* **Authenticity & Quality Doubts:** Users express confusion over wide price gaps for identical items across sellers, questioning whether cheaper listings are duplicates or authentic.
* **Discrepancies in Fit & Variants:** Users experience sizing inconsistencies even when comparing the same item across different colors within the same brand.
* **Trust in Reviews & Descriptions:** Skepticism arises when product descriptions differ from the received items or when platform reviews appear filtered or rejected.

#### 4. External Workarounds
To resolve comparison ambiguities, users rely heavily on external workarounds outside native product listings:
* **Influencer / Creator Guidance:** Users request third-party video creators to showcase side-by-side differences between items, tag exact product links, and display size, price, and fabric details directly on screen.
* **Cross-Platform Browsing:** Users cross-reference items across rival shopping apps to compare pricing, availability, and uniqueness.

#### 5. Outcome & Post-Purchase Impact
Unresolved uncertainties during comparison lead users to rely on trial-and-error purchasing—relying heavily on return and refund policies when sizing, color, or fabric expectations are missed.

---

### Evidence & Data Gaps
The contextual feedback indicates that comparison behavior relies heavily on external content (video reviews) and manual cross-app searching due to uncertainties in seller pricing and product authenticity. There is no direct context in the feedback regarding native, in-app product comparison tools (such as side-by-side spec comparison tables) on the platform.

**Evidence Breakdown:** **youtube**: 10, **app_store**: 3, **reddit**: 6, **play_store**: 1

### Key Evidence Citations

- **[YOUTUBE]** "_check details of product first like fabric, etc._"
- **[REDDIT]** "_Why is there so much of a price gap between these two sellers ?_"
- **[REDDIT]** "_Are they original or duplicate? What would be the difference in quality? Are they trust worthy and worth buying?_"
- **[YOUTUBE]** "_showing us the differences between them .It will really help me_"
- **[REDDIT]** "_Purchased two tops from Zara (sale). Same size, different colours. This is the size difference. Is this… normal?_"

---

## 6. What information do users seek outside Myntra/AJIO before purchasing?

### Information Users Seek Outside Myntra/AJIO

When evaluating purchases on Myntra or AJIO, shoppers frequently exit the platforms to gather external information and validate their decisions before buying. The decision journey typically progresses from platform browsing to external community research driven by uncertainties surrounding service reliability, garment quality, and pricing.

#### 1. Logistics, Return, and Refund Assurances
The most common topic users research externally is post-purchase fulfillment reliability (representing 20% of feedback):
* **Refund & Return Realities:** Shoppers consult community forums to verify whether platforms honor return promises, how quickly refunds are processed, and whether return pickups are hassle-free.
* **Customer Support Protection:** Users ask whether ordering through major aggregators circumvents customer service issues experienced with direct brand websites.
* **Payment Method Safety:** Shoppers seek advice on payment methods (e.g., Cash on Delivery vs. Credit Card) to mitigate financial risk when buying from platforms with disputed return records.

#### 2. Brand Quality and Fit Verification
Concerns regarding cheap materials or inconsistent sizing prompt users to seek peer reviews outside the app (10% of feedback):
* **Brand-Specific Quality Audits:** Shoppers ask community members for real-world feedback on specific brands listed on the platforms (e.g., asking about the material quality and durability of brands like HRX).
* **Curated Brand Recommendations:** Users request recommendations for affordable, decent-quality brands on Myntra/AJIO to avoid low-quality or poorly fitting items.

#### 3. Sale Timelines and Discount Comparisons
To maximize value, shoppers search for promotional insights across platforms (10% of feedback):
* **Upcoming Sale Events:** Users ask external communities for non-public information on when the next major sale event will occur.
* **Cross-Platform Price & Coupon Matching:** Shoppers compare bank offers, platform discounts, and cash-back percentages across competing platforms before deciding where to check out.

#### 4. Alternative Outlets for Unique Styles
When catalog options feel uninspiring, shoppers seek alternative platform recommendations (15% of feedback):
* **Niche & Genuine Storefronts:** Users ask external communities for recommended websites offering unique or trendy outfits when Myntra and AJIO selections feel too common, generic, or overpriced.

#### Summary Breakdown of User Workarounds
Uncertainty around return policies and garment quality causes shoppers to pause their purchase journey and consult social platforms (such as Reddit and YouTube) as an external verification step. Depending on community feedback, users either choose safer payment methods (like COD), wait for upcoming sales, or pivot to alternative stores.

**Evidence Breakdown:** **youtube**: 9, **reddit**: 10, **play_store**: 1

### Key Evidence Citations

- **[REDDIT]** "_Ajio: Delivery, Returns & Refund experiences? CC vs COD as well?_"
- **[REDDIT]** "_I heard issues regarding returns, customer support. Will ordering via Myntra etc circumvent this issue ?_"
- **[REDDIT]** "_Can anyone suggest any brands on Myntra and Ajio that are affordable and have decent quality? ... Was also wondering how HRX is in terms of quality?_"
- **[REDDIT]** "_Ajio vs Myntra vs Nyka. What's the difference really? When is the next sale coming up?_"
- **[REDDIT]** "_need some good websites like what the flex to buy cool outfits which are also genuine , good quality and trusted because myntra and ajio has become too basic._"

---

## 7. What role do fit, size, styling, price, reviews, occasion and social validation play?

Based on the provided context, the roles of fit, size, styling, price, reviews, occasion, and social validation unfold sequentially across the user journey:

### 1. Size & Fit: Inconsistency and Body Representation
Size standards vary significantly across different brands (for example, some brands fitting loosely while others fit tightly). This inconsistency creates fit uncertainty, particularly for specific body types (such as plus-size), where basic keyword searches are insufficient to determine how an item will look. Users need to see clothing on individuals with similar body proportions to make confident choices.

### 2. Price, Reviews, & External Visual Workarounds
Product descriptions and on-platform reviews assist in the initial decision-making process. However, when on-platform visuals feel unclear or heavily edited, users adopt external workarounds—such as watching unfiltered YouTube review videos—to verify true garment details and check price tags for convenience.

### 3. Occasion-Driven Curation
Shopping and outfit selection are strongly motivated by specific social events or occasions, including birthdays, dates, and office events. Outfits for these occasions are frequently curated by mixing pieces purchased from Myntra alongside items from other platforms.

### 4. Post-Purchase Styling & Social Validation
After receiving their items and building an outfit, users experience uncertainty regarding whether the styling is complete or visually appealing. In 40% of the provided context, users post their finalized outfits on external social channels (such as Reddit), explicitly list item sources (including Myntra), and seek social validation and styling feedback from peers (asking how to make the look better or for outfit improvement tips).

**Evidence Breakdown:** **reddit**: 16, **app_store**: 1, **youtube**: 2, **play_store**: 1

### Key Evidence Citations

- **[REDDIT]** "_Some brands like HnM or Mango fit pretty loose on me, while some others like Lee or Pepe are on the opposite end of the spectrum. Its like every brand has its own set of rules when it comes to deciding sizes._"
- **[REDDIT]** "_In plus-size fashion, it’s NOT easy to find the same fit or piece just by searching keywords. Seeing someone with a similar body type wearing something that looks good actually helps people make confident choices._"
- **[YOUTUBE]** "_helpful to choose a dress by seeing youtube videos cz u don't use too much filter and clearly visible every detail of clothes_"
- **[REDDIT]** "_Date fit. Good or can do better? Any suggestions? Heels: Myntra_"
- **[APP_STORE]** "_The product descriptions and reviews are helpful when deciding what to buy_"

---

## 8. When do users use the wishlist as genuine purchase intent versus simply as a bookmarking mechanism?

### Data Gap / Insufficient Evidence

The provided context does not contain sufficient user feedback to comprehensively evaluate or contrast when users use the wishlist as a genuine purchase intent tool versus a simple bookmarking mechanism.

### Limited Observed Wishlist Behavior

* **Price Tracking for Purchase Intent:** Only a single snippet (1 out of 20 feedback items, or 5%) explicitly references wishlist usage. In this case, the user utilizes the wishlist to monitor items for price drops and discount alerts.
* **Decision Breakdown:** When intent is triggered by price-drop notifications on wishlisted items, users experience breakdown during size selection—where the advertised discount decreases or disappears once a specific size is chosen.

Because the remaining feedback focuses on external channel links, order cancellations, return policies, and product authenticity rather than wishlist habits, no broader behavioral patterns regarding bookmarking versus buying intent can be established from the retrieved data.

**Evidence Breakdown:** **app_store**: 2, **reddit**: 5, **youtube**: 11, **play_store**: 2

### Key Evidence Citations

- **[REDDIT]** "_Myntra doing this to everything in my wish list. Shows prices went down! Actual search page says prices went down, but the minute you open the product to select size, the discount goes down._"
- **[APP_STORE]** "_The product descriptions and reviews are helpful when deciding what to buy_"
- **[PLAY_STORE]** "_they always cancel my order without giving any reason just by saying sorry. I mean we are not fool. if we are ordering something again and again that's means we really need that thing_"

---

## 9. How do these behaviors differ across user segments?

### Segment Comparison Data Availability

The provided context does not contain data categorized by defined user segments (such as demographic cohorts, purchase frequency tiers, or user persona types). Consequently, a formal comparison of behaviors across user segments cannot be established from the evidence.

### Behavioral Patterns Across Platform Contexts

While user segments are not explicitly defined, behavioral differences emerge across different interaction channels:

1. **External Content & Video Viewers (YouTube / Shorts)**
* **Discovery & Saved:** Users express interest in products showcased in videos and look for immediate purchase links.
* **Uncertainty & Friction:** Users encounter technical limitations such as unclickable links in short-form content, missing links, or mismatched product links where the linked item differs from the video.
* **Workarounds:** Users frequently navigate away from the primary video page to alternative channels (Telegram, WhatsApp groups, community posts) or manually copy and paste plain text links into external browsers.

2. **Platform & Community Discussants (Reddit / App Store)**
* **Evaluation & Friction:** Users evaluate product authenticity by comparing marketing images, AI renders, and video claims against actual store listings.
* **Outcome:** Users express dissatisfaction with promotional tactics (such as 'DM for link' mechanics) and report trust breakdowns when listing copies or app images vary from the physical item.

### Conclusion
Due to the lack of segmented user data in the provided snippets, no definitive conclusions regarding segment-specific behavior can be drawn.

**Evidence Breakdown:** **youtube**: 16, **reddit**: 3, **app_store**: 1

### Key Evidence Citations

- **[YOUTUBE]** "_Link in the shorts comment and description section are not clickable 😊 ok They are only clickable in the long videos_"
- **[YOUTUBE]** "_If Links are not clickable please copy and paste anywhere and click them it will work_"
- **[YOUTUBE]** "_The link which you send me is not of the top shown in the shorts video_"
- **[REDDIT]** "_If the influencers want to share any product, can't they write in the caption itself? What's this new trend of DM for link... it is very irritating_"
- **[APP_STORE]** "_At many places the product varies from the copy. Which is misleading to the customers_"

---

## 10. What unmet needs emerge consistently across user conversations?

### Friction in Transitioning from Content Discovery to Product Pages

The most consistent unmet need across user conversations involves the **frustration and fragmented journey when trying to access direct product links from creator and influencer content**.

#### User Journey Breakdown

1. **Discovery**: Users discover clothing items and fashion products showcased in creator content (such as haul videos and social posts).
2. **Off-Platform Redirection**: Instead of finding direct product links in captions or video descriptions, users are frequently directed to navigate third-party channels—such as WhatsApp channels, Telegram channels, YouTube community posts—or asked to send direct messages.
3. **Uncertainty & Failure Points**:
- **Missing Links**: Users report being unable to locate links across the designated external channels.
- **Product Mismatches**: When links are provided, users notice that the linked item is different from the product shown in the video.
- **Unclickable Links**: Links provided in video descriptions or comments are often plain text and unclickable.
4. **Workarounds Outside the Platform**:
- Users leave comments requesting creators to resend missing or correct links.
- Users manually copy unclickable link text and paste it elsewhere to open the page.
- Users navigate across multiple external platforms (toggling between YouTube, Telegram, and WhatsApp) to hunt down individual product links.

#### Quantitative Overview & Data Gaps
- **Proportion**: 14 out of 20 feedback snippets (70%) explicitly center on creator link redirections, missing/unclickable links, or user requests for product URLs.
- **Gaps**: Standard product descriptions on product pages are reported as helpful once accessed (1 out of 20 snippets); however, the critical point of breakdown occurs prior to reaching the product page.

**Evidence Breakdown:** **youtube**: 15, **reddit**: 4, **app_store**: 1

### Key Evidence Citations

- **[REDDIT]** "_If the influencers want to share any product, can't they write in the caption itself? What's this new trend of DM for link... it is very irritating_"
- **[YOUTUBE]** "_Can't find the exact link of the 2nd one, neither in attachment nor community post._"
- **[YOUTUBE]** "_shared Links are different that you are showing in video._"
- **[YOUTUBE]** "_If Links are not clickable please copy and paste anywhere and click them it will work_"

---

