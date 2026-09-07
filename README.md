# SENTINEL — AI Agent Reliability Console

> A browser-based console for evaluating AI agents against reliability, safety, tool-use, and goal-adherence scenarios.

[![CI](https://github.com/PreetamPasarad/sentinel-ai-agent-evaluation/actions/workflows/ci.yml/badge.svg)](https://github.com/PreetamPasarad/sentinel-ai-agent-evaluation/actions/workflows/ci.yml)
[![Deploy](https://github.com/PreetamPasarad/sentinel-ai-agent-evaluation/actions/workflows/pages.yml/badge.svg)](https://github.com/PreetamPasarad/sentinel-ai-agent-evaluation/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

SENTINEL is an AI-agent evaluation dashboard built around a simple engineering question:

**How reliably does an AI agent behave when a request is normal, ambiguous, adversarial, unsafe, conflicting, or tool-dependent?**

Instead of treating an agent as a chatbot demo, SENTINEL models it as a system that can be **tested, scored, traced, compared, and improved**.

> **Current status:** SENTINEL is a deterministic simulation prototype. It does **not** currently call an external LLM or certify real-world agent safety. The simulation exists to make the evaluation workflow reproducible while the architecture is developed toward real-agent testing.

## Why this project matters

Agent failures are not limited to incorrect text. A useful evaluator should also expose behaviors such as:

- ignoring constraints
- drifting away from the assigned goal
- using tools incorrectly
- making excessive or repeated tool calls
- failing safety or verification gates
- producing unreliable answers under ambiguous or adversarial inputs

SENTINEL turns those failure modes into structured evaluation results and engineering recommendations.

## Key features

- **Agent management** — define agents, versions, domains, prompts, and tools.
- **Scenario generation** — create normal, edge-case, conflicting, adversarial, safety, goal-drift, and tool-abuse tests.
- **Risk classification** — label scenarios as low, medium, high, or critical risk.
- **Deterministic execution** — reproduce simulated outcomes for the same test setup.
- **Failure taxonomy** — track hallucination, unsafe actions, goal drift, incorrect responses, incorrect tool usage, loops, and excessive calls.
- **Reliability scoring** — calculate category scores for Safety, Accuracy, Tool Usage, Goal Adherence, and Robustness.
- **Weighted overall score** — combine evaluation dimensions into one reliability indicator.
- **Trace inspection** — inspect request, decision, tool interaction, and outcome steps.
- **Recommendations** — translate failures into engineering actions such as verification gates, rate limits, and tighter scope constraints.
- **Version comparison** — compare evaluation concepts across agent versions.
- **Responsive dashboard** — browser UI designed for desktop and smaller screens.
- **CI validation** — GitHub Actions validates project structure and evaluation fixtures on pushes and pull requests.

## Evaluation pipeline

```text
Agent configuration
       ↓
Scenario generation
       ↓
Risk + category classification
       ↓
Deterministic execution
       ↓
Pass / fail + failure taxonomy
       ↓
Category scoring
       ↓
Overall reliability score
       ↓
Trace inspection + recommendations
```

## Evaluation categories

| Category | Purpose |
|---|---|
| Normal | Standard in-scope requests |
| Edge Case | Missing, incomplete, or ambiguous information |
| Adversarial | Attempts to bypass rules or constraints |
| Conflicting | Contradictory instructions |
| Safety | Verification and guardrail behavior |
| Tool Abuse | Repeated, excessive, or unsafe tool usage |
| Goal Drift | Attempts to move outside the assigned objective |

## Failure taxonomy

The prototype models failures including:

- Hallucination
- Unsafe action
- Goal drift
- Incorrect response
- Incorrect tool usage
- Tool-call loops
- Timeout / excessive calls

## Tech stack

- HTML5
- CSS3
- Vanilla JavaScript
- CSS Grid
- Browser-local state
- Deterministic simulation logic
- Python standard library for fixture validation
- GitHub Actions for CI/CD
- GitHub Pages for deployment

The frontend intentionally has no framework or build dependency in the current prototype.

## Project structure

```text
sentinel-ai-agent-evaluation/
├── index.html                         # Browser application
├── README.md                          # Project documentation
├── LICENSE                            # MIT license
├── CONTRIBUTING.md                    # Contribution workflow
├── .gitignore
├── docs/
│   └── architecture.md               # Current + target architecture
├── scripts/
│   └── validate_fixtures.py           # Dependency-free JSON validation
├── tests/
│   └── fixtures/
│       └── sample-evaluation.json     # Evaluation data contract example
└── .github/
    └── workflows/
        ├── ci.yml                     # Pull request / push validation
        └── pages.yml                  # GitHub Pages deployment
```

## Run locally

### Option 1 — VS Code Live Server

1. Clone the repository.
2. Open it in VS Code.
3. Install the **Live Server** extension.
4. Open `index.html`.
5. Select **Go Live**.

### Option 2 — Python static server

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

### Validate fixtures

No third-party Python packages are required:

```bash
python scripts/validate_fixtures.py
```

## Engineering decisions

### Why deterministic simulation?

A prototype evaluator should be reproducible. Deterministic outcomes make it possible to test the scoring, trace, and dashboard layers without requiring an external model, API key, network connection, or variable model output.

### Why a structured evaluation fixture?

The JSON fixture establishes a small data contract for future persistence and API work. A production implementation can extend the same model with provider/model metadata, prompt versions, timestamps, traces, evaluator versions, and run IDs.

### Why CI for a static site?

The project is intentionally lightweight, but professional projects still benefit from automated checks. CI catches broken fixture data and missing core files before deployment.

## Roadmap

### Phase 1 — Portfolio foundation

- [x] Evaluation dashboard
- [x] Scenario generation
- [x] Risk levels
- [x] Failure classification
- [x] Reliability scoring
- [x] Trace visualization
- [x] Recommendations
- [x] Professional documentation
- [x] License
- [x] Contribution guidelines
- [x] JSON evaluation fixture
- [x] Automated CI validation
- [ ] Split HTML, CSS, and JavaScript into maintainable modules
- [ ] Add polished screenshots and demo GIF

### Phase 2 — Real agent evaluation

- [ ] Add a backend evaluation API
- [ ] Connect an LLM through a provider adapter
- [ ] Execute real model responses against scenario suites
- [ ] Add configurable evaluation criteria
- [ ] Store immutable evaluation runs as JSON
- [ ] Add test-suite import/export
- [ ] Add timeout and rate-limit controls

### Phase 3 — Regression platform

- [ ] Prompt/version comparison
- [ ] Model/provider comparison
- [ ] Persistent database storage
- [ ] Evaluation history and trend charts
- [ ] Automated regression gates in CI
- [ ] Tool sandboxing
- [ ] Authentication and team workspaces

## Limitations

SENTINEL is currently a **prototype / simulation**, not a production safety certification system. Simulated scores should not be interpreted as evidence that a real model or agent is safe or reliable.

The next major engineering step is separating the evaluation engine from the browser UI and introducing a backend adapter that can execute real agents safely and reproducibly.

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for the current design and proposed production evolution.

## Author

**Preetam Pasarad** — AIML student exploring AI, software engineering, and practical agent systems.

If you find the project useful, consider giving the repository a ⭐.
