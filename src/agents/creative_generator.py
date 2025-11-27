from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
from typing import List
import yaml
import os

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

class CreativeRecommendation(BaseModel):
    campaign_name: str
    current_performance_issue: str
    suggested_headline: str
    suggested_message: str
    reasoning: str

class CreativeSuggestions(BaseModel):
    recommendations: List[CreativeRecommendation]

class CreativeGenerator:
    def __init__(self):
        self.llm = ChatGroq(
            model=config["llm"]["model"],
            temperature=0.7, # Higher temperature for creativity
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def generate(self, insights: str, top_performing_ads: str) -> CreativeSuggestions:
        """
        Generates new creative concepts based on insights and top performers.
        """
        system_prompt = """You are a Creative Improvement Generator.
Your goal is to propose new creative angles for Facebook Ads.

Inputs:
1. Insights: Analysis of what is going wrong (e.g., "Ad fatigue", "Low CTR").
2. Top Performing Ads: Examples of what works well.

Task:
Generate 3-5 specific creative recommendations.
For each recommendation, provide:
- The target campaign/angle.
- The issue being addressed.
- A new Headline.
- A new Primary Text (Message).
- Why this should work (Reasoning).

Output must be a JSON object matching the CreativeSuggestions schema.
"""
        structured_llm = self.llm.with_structured_output(CreativeSuggestions)
        return structured_llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Insights:\n{insights}\n\nTop Performing Ads:\n{top_performing_ads}")
        ])
