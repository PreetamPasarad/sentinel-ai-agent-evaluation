# Contributing to SENTINEL

Thanks for your interest in improving SENTINEL.

## Development

SENTINEL is currently a browser-first prototype built with HTML, CSS, and vanilla JavaScript. No framework or build step is required.

1. Fork the repository.
2. Create a focused branch for your change.
3. Run the local app with a static server:

```bash
python -m http.server 8000
```

4. Open `http://localhost:8000` and test the affected flows.
5. Run the fixture validation command:

```bash
python scripts/validate_fixtures.py
```

6. Keep pull requests small and explain the problem, the change, and how it was tested.

## Contribution guidelines

- Prefer clear, maintainable JavaScript over clever one-liners.
- Keep evaluation results deterministic when adding simulation logic.
- Do not describe simulated results as real model performance.
- Add or update fixture data when changing the evaluation schema.
- Avoid committing secrets, API keys, generated build output, or personal data.
- Preserve keyboard accessibility and responsive behavior.

## Pull requests

A useful PR should include:

- What changed
- Why it changed
- How it was tested
- Screenshots for meaningful UI changes
- Any follow-up work that remains
