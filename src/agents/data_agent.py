import pandas as pd
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
import yaml
import os

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

class DataAgent:
    def __init__(self):
        csv_path = config["data"]["sample_path"] if config.get("use_sample_data", False) else config["data"]["csv_path"]
        self.df = pd.read_csv(csv_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.llm = ChatGroq(
            model=config["llm"]["model"],
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def execute(self, instruction: str) -> str:
        """
        Generates and executes pandas code based on the instruction.
        """
        with open("prompts/data_agent_prompt.md", "r") as f:
            prompt_template = f.read()
            
        system_prompt = prompt_template.format(
            columns=list(self.df.columns),
            date_min=self.df['date'].min(),
            date_max=self.df['date'].max()
        )

        # We ask the LLM to generate the code
        response = self.llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=instruction)
        ])
        
        import re
        match = re.search(r"```python(.*?)```", response.content, re.DOTALL)
        if match:
            code = match.group(1).strip()
        else:
            code = response.content.strip().replace("```python", "").replace("```", "").strip()
        
        # Safe execution environment
        local_vars = {"df": self.df, "pd": pd}
        try:
            exec(code, {}, local_vars)
            result = local_vars.get("result")
            if isinstance(result, pd.DataFrame):
                return result.to_markdown()
            elif isinstance(result, pd.Series):
                return result.to_markdown()
            else:
                return str(result)
        except Exception as e:
            return f"Error executing code: {e}\nCode generated:\n{code}"
