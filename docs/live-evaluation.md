# Live LLM evaluation

SENTINEL now has a real evaluation path in addition to the deterministic browser prototype.

## Architecture

```text
real.html
   |
   | POST /api/evaluate
   v
server.py
   |
   +--> target LLM (agent response)
   |
   +--> judge LLM (JSON verdict)
   v
PASS/FAIL + five scores + failure type + recommendation + latency
```

The browser never receives the API key. `server.py` reads it from `.env` and calls an OpenAI-compatible `/chat/completions` endpoint.

## Run locally

1. Install Python 3.10+.
2. Copy `.env.example` to `.env`.
3. Put your API key in `.env`.
4. Run `python server.py`.
5. Open `http://localhost:8000/`.
6. Enter a system prompt, scenario, and expected behavior.
7. Click **Run real evaluation**.

The evaluator limits a request to 25 scenarios and does not execute tools. Tool descriptions are supplied to the judge as metadata only.

## Why two model calls?

The first call behaves as the agent under test. The second call acts as an independent judge and returns structured scores for Safety, Accuracy, Tool Usage, Goal Adherence, and Robustness. This makes the result substantially more meaningful than a hard-coded simulation while still being clearly labeled as LLM-as-a-judge evaluation.

## Security

Never put API keys in `real.html`, `index.html`, JavaScript files, GitHub Pages, screenshots, or commits. `.env` is ignored by Git.
