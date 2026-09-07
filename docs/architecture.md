# SENTINEL Architecture

## Current architecture

SENTINEL is a static, browser-first evaluation console. The UI, evaluation model, deterministic simulation, scoring, trace rendering, and recommendations currently run on the client side.

```text
+---------------------+
| Agent Configuration |
+----------+----------+
           |
           v
+---------------------+
| Scenario Generation |
+----------+----------+
           |
           v
+---------------------+
| Risk / Category     |
| Classification      |
+----------+----------+
           |
           v
+---------------------+
| Deterministic       |
| Simulation Engine   |
+----------+----------+
           |
           v
+---------------------+
| Result + Failure    |
| Taxonomy            |
+----------+----------+
           |
           v
+---------------------+
| Scoring Engine      |
+----------+----------+
           |
           v
+---------------------+
| Trace + Dashboard   |
| + Recommendations    |
+---------------------+
```

## Design principles

### Determinism

The prototype uses deterministic simulation so a test can be reproduced. A production evaluator should retain a seed, model identifier, prompt version, tool configuration, and evaluator version for each run.

### Separation of concerns

The long-term code structure should separate:

- scenario generation
- execution/adapters
- scoring
- failure classification
- persistence
- presentation

The current single-file implementation is intentionally lightweight; this document defines the target architecture for the next refactor.

## Production evolution

```text
Browser UI
    |
    v
Evaluation API
    |
    +--> Scenario service
    +--> Agent adapter / model gateway
    +--> Tool sandbox
    +--> Evaluator / scoring engine
    +--> Run store
             |
             v
        Evaluation history
```

A future backend should make external model calls server-side, protect credentials, enforce timeouts and rate limits, isolate tool execution, and persist immutable evaluation runs.

## Evaluation run model

Each run should be identifiable by:

- `run_id`
- agent name and version
- model/provider
- scenario suite version
- evaluator version
- timestamp
- seed (when applicable)
- test results
- aggregate scores
- failure taxonomy
- trace metadata

This makes regression analysis and version-to-version comparison reproducible.
