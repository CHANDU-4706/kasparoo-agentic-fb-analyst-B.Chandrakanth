# Kasparro — Agentic Facebook Performance Analyst

## Quick Start (Step-by-Step)

Follow these exact steps to set up and run the project:

### 1. Clone the Repository
```bash
git clone https://github.com/CHANDU-4706/kasparoo-agentic-fb-analyst-B.Chandrakanth.git
cd kasparoo-agentic-fb-analyst-B.Chandrakanth
```

### 2. Set up Python Environment
```bash
# Check Python version (must be >= 3.10)
python -V

# Create virtual environment
python -m venv .venv

# Activate environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
1. Copy the example environment file:
   ```bash
   # Windows
   copy .env.example .env
   # Mac/Linux
   cp .env.example .env
   ```
2. Open `.env` and paste your **Groq API Key**:
   ```text
   GROQ_API_KEY=gsk_...
   ```

### 5. Run Analysis
```bash
python src/run.py "Analyze ROAS drop in last 7 days"
```

---

## Data
- **Default**: The system uses `data/sample_fb_ads.csv` by default (configured in `config.yaml`) for instant reproducibility.
- **Full Data**: To use the full dataset:
    1. Place `synthetic_fb_ads_undergarments.csv` in the `data/` folder.
    2. Edit `config/config.yaml` and set `use_sample_data: false`.
- See `data/README.md` for details.

## Config
Edit `config/config.yaml`:
```yaml
python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: true
```

## Repo Map
- `src/agents/` — planner.py, data_agent.py, insight_agent.py, evaluator.py, creative_generator.py
- `prompts/` — *.md prompt files with variable placeholders
- `reports/` — report.md, insights.json, creatives.json
- `logs/` — trace.json (structured logs)
- `tests/` — test_evaluator.py

## Run Options
```bash
make run  # or: python src/run.py "Analyze ROAS drop"
```

## Outputs
- `reports/report.md`
- `reports/insights.json`
- `reports/creatives.json`

## Observability
- Structured JSON logs are saved to `logs/trace.json`.
- These logs capture inputs, outputs, and timestamps for every agent step.

## Release
- Tag: `v1.0` (See GitHub Releases)

## Self-Review
- **Architecture**: Used LangGraph-style orchestration (Planner -> Data -> Insight -> Creative -> Evaluator) for robust reasoning.
- **Tradeoffs**: 
    - Selected `llama-3.3-70b` on Groq for speed and performance after Gemini quota issues.
    - Implemented local JSON logging instead of heavy external dependencies for simplicity.
    - Used Pandas for data analysis to ensure deterministic calculation of metrics.
- **Verification**: Verified all agents and outputs.
