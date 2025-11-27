# Kasparro — Agentic Facebook Performance Analyst

## Quick Start
```bash
python -V  # should be >= 3.10
python -m venv .venv 
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"
```

## Data
- Place the full CSV locally and set `DATA_CSV=data/synthetic_fb_ads_undergarments.csv` (or ensure it is in `data/`).
- Or copy a small sample to `data/sample_fb_ads.csv`.
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

## Run
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
