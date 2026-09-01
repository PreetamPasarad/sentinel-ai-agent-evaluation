# SENTINEL — AI Agent Reliability Console

> A browser-based console for evaluating AI agents against reliability, safety, tool-use, and goal-adherence scenarios.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-4FD3C4?style=for-the-badge)](#live-demo)
[![Built with HTML](https://img.shields.io/badge/HTML-5-E34F26?logo=html5&logoColor=white)](#tech-stack)
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=111)](#tech-stack)

## What is SENTINEL?

SENTINEL is an AI-agent evaluation dashboard designed to answer a practical question:

**"How reliably does an AI agent behave when the request is normal, ambiguous, adversarial, unsafe, or involves tools?"**

Instead of looking only at whether an agent produces a good answer, SENTINEL evaluates different failure modes and turns the results into category scores and actionable recommendations.

## Why I built it

AI agents can fail in ways that ordinary chatbot demos do not reveal. They can follow conflicting instructions, drift away from their task, misuse tools, repeat calls, or bypass safety checks.

This project explores the idea of treating an AI agent like a system that needs **testing, monitoring, and evaluation**, not just prompting.

## Key features

- **Agent management** — define agents, versions, domains, system prompts, and tools.
- **Automatic scenario generation** — creates tests for normal requests, edge cases, conflicting instructions, adversarial prompts, safety cases, goal drift, and tool abuse.
- **Risk classification** — tests are tagged as low, medium, high, or critical risk.
- **Execution simulation** — runs deterministic mock evaluations so the same agent/test combination can be reproduced.
- **Failure taxonomy** — tracks hallucination, unsafe action, goal drift, incorrect responses, incorrect tool usage, tool-call loops, and excessive calls.
- **Reliability scoring** — calculates category scores for Safety, Accuracy, Tool Usage, Goal Adherence, and Robustness.
- **Weighted overall score** — combines evaluation categories into a single reliability score.
- **Trace view** — shows the request, agent decision, tool call/response, and final outcome for each test.
- **Recommendations** — turns failures into concrete engineering suggestions such as verification gates, rate limits, and stronger scope constraints.
- **Version comparison** — supports evaluating agent versions against the same testing concept.

## How the evaluation works

```text
Agent configuration
       ↓
Scenario generation
       ↓
Risk + category classification
       ↓
Deterministic test execution
       ↓
Pass / fail + failure type
       ↓
Category scoring
       ↓
Overall reliability score
       ↓
Engineering recommendations
```

## Evaluation categories

| Category | What it tests |
|---|---|
| Normal | Standard in-scope requests |
| Edge Case | Missing or ambiguous information |
| Adversarial | Attempts to override rules or constraints |
| Conflicting | Contradictory instructions |
| Safety | Verification and sensitive-action guardrails |
| Tool Abuse | Repeated, excessive, or unsafe tool calls |
| Goal Drift | Attempts to move the agent outside its intended task |

## Failure types

SENTINEL currently models failures including:

- Tool-call loops
- Hallucination
- Unsafe actions
- Goal drift
- Incorrect responses
- Incorrect tool usage
- Timeout / excessive calls

## Tech stack

- HTML5
- CSS3
- Vanilla JavaScript
- CSS Grid / responsive layouts
- Browser-local state and deterministic simulation logic

No frontend framework is required for the current prototype.

## Running locally

Because the current prototype is a static web application, you can run it with any local static server.

### Option 1 — VS Code Live Server

1. Open this repository in VS Code.
2. Install the **Live Server** extension.
3. Open `index.html`.
4. Click **Go Live**.

### Option 2 — Python

If Python is installed:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Project structure

The current prototype is intentionally kept simple:

```text
sentinel-ai-agent-evaluation/
├── index.html          # Main application
├── README.md           # Project documentation
├── .gitignore          # Git exclusions
└── .github/
    └── workflows/
        └── pages.yml   # GitHub Pages deployment workflow
```

## Roadmap

### Phase 1 — Portfolio-ready frontend

- [x] Evaluation dashboard
- [x] Test scenario generation
- [x] Risk levels
- [x] Failure classification
- [x] Reliability scoring
- [x] Trace visualization
- [x] Recommendations
- [x] Professional README
- [ ] Split HTML, CSS, and JavaScript into maintainable files
- [ ] Add screenshots and demo GIF

### Phase 2 — Real agent evaluation

- [ ] Connect to a real LLM API
- [ ] Execute real model responses against generated scenarios
- [ ] Add configurable evaluation criteria
- [ ] Store evaluation runs as JSON
- [ ] Add export/import for test suites

### Phase 3 — Production-style evaluation

- [ ] Automated regression testing
- [ ] Prompt/version comparison
- [ ] Model comparison
- [ ] Persistent database storage
- [ ] Authentication and team workspaces
- [ ] CI-based agent evaluation
- [ ] Evaluation history and trend charts

## Important note

The current application is a **prototype / simulation**, not a production safety certification system. Its test outcomes are generated by deterministic simulation logic rather than by executing a real external AI agent.

That distinction is important: the project demonstrates the architecture and UX of an agent-evaluation console, while the roadmap describes how it can evolve into a real evaluation platform.

## Future vision

The long-term goal is to turn SENTINEL into a lightweight evaluation platform where developers can submit an AI agent, define its tools and constraints, run a standardized test suite, inspect failures, compare versions, and identify regressions before deployment.

## Author

**Preetam Pasarad**

AIML student building projects around AI, software engineering, and practical agent systems.

---

If you find the project useful, consider giving the repository a ⭐.