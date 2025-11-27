# Kasparro Analysis Report

## Query
Analyze ROAS drop and suggest creative improvements

## Data Analysis


### Data Output (Get Daily Metrics):
| date                |     roas |     cpm |       ctr |   spend |
|:--------------------|---------:|--------:|----------:|--------:|
| 2025-03-17 00:00:00 |  7.7474  | 1.98946 | 0.0135922 | 26346   |
| 2025-03-18 00:00:00 |  7.6934  | 1.57666 | 0.0123564 | 23318.1 |
| 2025-03-19 00:00:00 |  7.0084  | 2.03536 | 0.0108061 | 26025.8 |
| 2025-03-20 00:00:00 |  7.5398  | 1.8846  | 0.0115153 | 24941.6 |
| 2025-03-21 00:00:00 |  8.3096  | 1.7107  | 0.0105916 | 22962.3 |
| 2025-03-22 00:00:00 | 10.2298  | 1.55212 | 0.0125521 | 22974   |
| 2025-03-23 00:00:00 |  9.7784  | 1.65683 | 0.0122566 | 20082.4 |
| 2025-03-24 00:00:00 |  5.1906  | 1.91415 | 0.011292  | 26261.2 |
| 2025-03-25 00:00:00 |  9.9738  | 1.74632 | 0.0124675 | 22262.8 |
| 2025-03-26 00:00:00 | 10.3652  | 1.70361 | 0.0126173 | 24592.2 |
| 2025-03-27 00:00:00 |  7.63959 | 1.86394 | 0.0134657 | 22907.8 |
| 2025-03-28 00:00:00 |  7.278   | 1.65371 | 0.0126273 | 20926.7 |
| 2025-03-29 00:00:00 |  7.0234  | 1.80806 | 0.0116385 | 22646.1 |
| 2025-03-30 00:00:00 |  5.6846  | 2.0793  | 0.0123706 | 26046.5 |
| 2025-03-31 00:00:00 |  7.1384  | 1.86675 | 0.0123223 | 24644.9 |

### Data Output (Segment Data):
|                             |     roas |
|:----------------------------|---------:|
| ('Carousel', 'Broad')       |  7.71596 |
| ('Carousel', 'Lookalike')   |  8.72532 |
| ('Carousel', 'Retargeting') | 13.0855  |
| ('Image', 'Broad')          |  7.22714 |
| ('Image', 'Lookalike')      |  9.26197 |
| ('Image', 'Retargeting')    | 12.64    |
| ('UGC', 'Broad')            |  8.32649 |
| ('UGC', 'Lookalike')        |  8.61333 |
| ('UGC', 'Retargeting')      | 10.7558  |
| ('Video', 'Broad')          |  6.15146 |
| ('Video', 'Lookalike')      |  8.47223 |
| ('Video', 'Retargeting')    | 11.092   |

## Insights


### Insights (Identify Correlated Metrics):
### Hypotheses and Insights
Based on the provided data, the following observations, analyses, and conclusions can be drawn:

1. **Observation**: The ROAS dropped significantly on March 24th and March 30th.
   - **Analysis**: On these days, the CPM was higher compared to the days with higher ROAS.
   - **Conclusion/Hypothesis**: The increase in CPM may have led to a decrease in ROAS, suggesting that higher costs per thousand impressions could be driving down the return on ad spend.

2. **Observation**: There's a noticeable fluctuation in ROAS throughout the period.
   - **Analysis**: The spend amount also fluctuates, but there isn't a direct correlation where higher spend always results in higher or lower ROAS.
   - **Conclusion/Hypothesis**: The effectiveness of the ad spend (ROAS) might not be directly tied to the amount spent but could be influenced by other factors such as ad targeting, audience saturation, or the day of the week.

3. **Observation**: The CTR (Click-Through Rate) varies but doesn't seem to have a direct impact on ROAS.
   - **Analysis**: Days with higher CTRs don't consistently have higher ROAS, and vice versa.
   - **Conclusion/Hypothesis**: While CTR is an important metric for engagement, it may not be the primary driver of ROAS in this context. Other factors like conversion rates, cost per conversion, or the value of conversions might play a more significant role.

4. **Observation**: The highest ROAS values are seen on March 22nd and March 26th.
   - **Analysis**: These days have lower CPMs compared to the days with lower ROAS.
   - **Conclusion/Hypothesis**: Lower CPMs might contribute to higher ROAS, indicating that optimizing ad campaigns to reduce costs while maintaining or increasing conversions could be a key strategy for improving return on ad spend.

5. **Observation**: Spend amounts are relatively consistent, with some fluctuation.
   - **Analysis**: Despite the fluctuations in spend, ROAS varies significantly, suggesting that the effectiveness of the ad spend is sensitive to factors other than just the amount spent.
   - **Conclusion/Hypothesis**: The efficiency of ad spend (as measured by ROAS) could be more influenced by the quality of ad targeting, ad creative, bidding strategies, or audience behavior rather than the absolute spend amount.

### Insights (Determine Root Cause):
### Hypotheses and Insights
Based on the provided data, the following hypotheses and insights can be derived:

1. **Observation**: ROAS dropped significantly on March 24th and March 30th.
   * **Analysis**: On these days, CPM was higher compared to other days, and spend was also relatively high.
   * **Conclusion/Hypothesis**: The increase in CPM, possibly due to audience saturation or increased competition, led to a decrease in ROAS. This suggests that the ad spend was not as efficient on these days, potentially due to over-targeting or less effective ad creatives.

2. **Observation**: Certain creative types and audience segments have significantly higher ROAS.
   * **Analysis**: 'Carousel' with 'Retargeting', 'Image' with 'Retargeting', and 'UGC' with 'Retargeting' have higher ROAS compared to their counterparts. Similarly, 'Video' with 'Retargeting' shows a higher ROAS than 'Video' with 'Broad' or 'Lookalike'.
   * **Conclusion/Hypothesis**: Retargeting audiences tend to have a higher ROAS across different creative types, suggesting that targeting users who have already interacted with the brand or product is more effective. This could be due to increased brand awareness and intent among retargeted users.

3. **Observation**: 'Video' with 'Broad' audience has the lowest ROAS among all segments.
   * **Analysis**: This could be due to the broad targeting not being as effective for video content, possibly because video ads are more expensive and may not resonate as well with a broad, less targeted audience.
   * **Conclusion/Hypothesis**: The low ROAS for 'Video' with 'Broad' audience suggests that video content may be more effective when targeted at specific, interested audiences rather than a broad, general audience. This could indicate a need to refine targeting strategies for video ads to improve efficiency.

4. **Observation**: UGC (User-Generated Content) tends to perform well across different audience segments.
   * **Analysis**: UGC with 'Broad', 'Lookalike', and 'Retargeting' all show relatively high ROAS, indicating that UGC is effective across various targeting strategies.
   * **Conclusion/Hypothesis**: The success of UGC across different segments suggests that authentic, user-generated content resonates well with the target audience, regardless of the targeting strategy. This could be due to the perceived authenticity and social proof associated with UGC.

These insights suggest that refining targeting strategies, particularly focusing on retargeting and potentially leveraging UGC, could help improve ROAS. Additionally, optimizing ad spend to avoid days or periods with high CPM could also contribute to better campaign efficiency.

## Creative Recommendations

### Campaign: Adset-2 LAL2
- **Issue**: Ad fatigue
- **New Headline**: Last Chance: Upgrade Your Men's Drawer
- **New Message**: Don't miss out on our 3-pack deal! Get the best athletic briefs for men and elevate your comfort.
- **Reasoning**: The top-performing ad in this set has a high ROAS, but its performance may decline over time due to ad fatigue. Changing the creative message can help mitigate this issue.

### Campaign: Adset-1 Retarget
- **Issue**: Low CTR
- **New Headline**: Unlock Comfort
- **New Message**: Discover the secret to all-day comfort with our wireless sports bras for women.
- **Reasoning**: The current ad has a high ROAS, but its CTR could be improved. Using a more attention-grabbing headline and message can help increase clicks.

### Campaign: Adset-3 Broad
- **Issue**: Low conversion rate
- **New Headline**: Join the Comfort Revolution
- **New Message**: Thousands of men have already made the switch to our breathable modal boxers. Try them today and experience the difference!
- **Reasoning**: The current ad has a relatively low ROAS compared to other top-performing ads. Focusing on the benefits of the product and using social proof can help increase conversions.

### Campaign: Adset-1 Retarget
- **Issue**: Ad fatigue
- **New Headline**: Real People, Real Comfort
- **New Message**: Don't just take our word for it! Our customers rave about our men's boxers. Read their stories and discover why they love our products.
- **Reasoning**: The current ad has a high ROAS, but its performance may decline over time due to ad fatigue. Using user-generated content and emphasizing the product's benefits can help keep the ad fresh and engaging.

### Campaign: Adset-3 Broad
- **Issue**: Low CTR
- **New Headline**: Break Free from Ordinary
- **New Message**: Experience the comfort and freedom of our men's inner vests. Say goodbye to restrictive clothing and hello to a new level of comfort.
- **Reasoning**: The current ad has a relatively low ROAS compared to other top-performing ads. Using a more attention-grabbing headline and message, and emphasizing the product's unique features can help increase clicks.
