import argparse
import asyncio
import os
import json
from dotenv import load_dotenv
from tabulate import tabulate
import time
from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.creative_generator import CreativeGenerator
from agents.evaluator import EvaluatorAgent

# Load environment variables
load_dotenv(".env")

# Fallback for API Key if not found in env
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("⚠️ GROQ_API_KEY not found in .env. Using fallback key.")
    api_key = "" # Placeholder - do not commit real keys
    os.environ["GROQ_API_KEY"] = api_key

print(f"✅ API Key loaded: {api_key[:5]}...{api_key[-4:]}")

async def main():
    parser = argparse.ArgumentParser(description="Kasparro Agentic FB Analyst")
    parser.add_argument("query", type=str, help="The analysis query (e.g., 'Analyze ROAS drop')")
    args = parser.parse_args()

    query = args.query
    print(f"\n🚀 Starting Analysis for: '{query}'\n")

    # Initialize Agents
    planner = PlannerAgent()
    data_agent = DataAgent()
    insight_agent = InsightAgent()
    creative_gen = CreativeGenerator()
    evaluator = EvaluatorAgent()

    # Initialize Logging
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/trace.json"
    logs = []

    def log_step(step_name, agent, input_data, output_data):
        entry = {
            "timestamp": time.time(),
            "step": step_name,
            "agent": agent,
            "input": input_data,
            "output": output_data
        }
        logs.append(entry)
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)

    # Step 1: Plan
    print("📋 Planner: Creating execution plan...")
    plan = planner.create_plan(query)
    print(f"Plan created with {len(plan.steps)} steps.\n")
    log_step("Planning", "PlannerAgent", query, [s.model_dump() for s in plan.steps])
    
    context = {"query": query, "data_summary": "", "insights": "", "top_ads": ""}
    
    # Step 2: Execute Plan
    for i, step in enumerate(plan.steps):
        print(f"▶️ Step {i+1}: {step.step_name} ({step.agent})")
        print(f"   Description: {step.description}")
        
        step_output = ""
        if step.agent == "DataAgent":
            result = data_agent.execute(step.description)
            context["data_summary"] += f"\n\n### Data Output ({step.step_name}):\n{result}"
            step_output = result
            print(f"   ✅ Data Agent finished.")
            
        elif step.agent == "InsightAgent":
            result = insight_agent.analyze(context["data_summary"], step.description)
            context["insights"] += f"\n\n### Insights ({step.step_name}):\n{result}"
            step_output = result
            print(f"   ✅ Insight Agent finished.")
            
        elif step.agent == "CreativeGenerator":
            # For creative gen, we need top ads. Let's ask DataAgent to get them if not present.
            if not context["top_ads"]:
                print("   ⚠️ Fetching top ads for context...")
                top_ads = data_agent.execute("Get top 5 ads by ROAS with their creative messages")
                context["top_ads"] = top_ads
            
            result = creative_gen.generate(context["insights"], context["top_ads"])
            # Convert Pydantic model to JSON/Dict for report
            result_json = result.model_dump_json()
            context["creative_recommendations"] = result_json
            step_output = result_json
            print(f"   ✅ Creative Generator finished.")
        
        log_step(step.step_name, step.agent, step.description, step_output)
        print("   ⏳ Waiting 10s to respect API rate limits...")
        time.sleep(10)

    # Step 3: Compile Report
    print("\n📝 Compiling Final Report...")
    report = f"""# Kasparro Analysis Report

## Query
{query}

## Data Analysis
{context['data_summary']}

## Insights
{context['insights']}

## Creative Recommendations
"""
    if "creative_recommendations" in context:
        recs = json.loads(context["creative_recommendations"])
        if "recommendations" in recs:
             for rec in recs["recommendations"]:
                report += f"\n### Campaign: {rec['campaign_name']}\n"
                report += f"- **Issue**: {rec['current_performance_issue']}\n"
                report += f"- **New Headline**: {rec['suggested_headline']}\n"
                report += f"- **New Message**: {rec['suggested_message']}\n"
                report += f"- **Reasoning**: {rec['reasoning']}\n"

    # Step 4: Evaluate
    print("🔍 Evaluator: Reviewing report...")
    eval_result = evaluator.evaluate(query, report)
    print(f"Evaluator Result: {eval_result}\n")
    log_step("Evaluation", "EvaluatorAgent", report, eval_result)

    # Save Outputs
    os.makedirs("reports", exist_ok=True)
    with open("reports/report.md", "w") as f:
        f.write(report)
    
    if "creative_recommendations" in context:
        with open("reports/creatives.json", "w") as f:
            f.write(context["creative_recommendations"])

    # Save Insights JSON
    insights_data = {
        "query": query,
        "insights": context.get("insights", ""),
        "data_summary": context.get("data_summary", "")
    }
    with open("reports/insights.json", "w") as f:
        json.dump(insights_data, f, indent=2)
            
    print(f"✅ Analysis Complete! Report saved to reports/report.md")

if __name__ == "__main__":
    asyncio.run(main())
