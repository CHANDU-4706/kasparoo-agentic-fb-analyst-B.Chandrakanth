import pytest
from src.agents.evaluator import EvaluatorAgent
from dotenv import load_dotenv
import os

# Load env for tests
load_dotenv(".env")
# Fallback if not in env (for CI/CD without env file)
if not os.getenv("GROQ_API_KEY"):
     os.environ["GROQ_API_KEY"] = "placeholder_key_for_testing"

def test_evaluator_pass():
    agent = EvaluatorAgent()
    query = "Analyze ROAS drop"
    report = """# Report
    ## Data Analysis
    ROAS dropped by 20%.
    ## Insights
    This was due to CPM increase.
    ## Creative Recommendations
    New headline: 'Buy Now'.
    """
    # Mocking the LLM response is ideal, but for integration test we check structure
    # Here we just check if it runs without error
    try:
        result = agent.evaluate(query, report)
        assert isinstance(result, str)
    except Exception as e:
        pytest.fail(f"Evaluator failed: {e}")

def test_evaluator_fail_empty():
    agent = EvaluatorAgent()
    query = "Analyze ROAS drop"
    report = ""
    try:
        result = agent.evaluate(query, report)
        assert isinstance(result, str)
    except Exception as e:
        pytest.fail(f"Evaluator failed: {e}")
