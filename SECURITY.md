# Security Policy

## Scope

SENTINEL is currently a client-side prototype and does not require API keys or a backend service.

## Reporting a vulnerability

Please do not publish sensitive security details in a public issue. Contact the repository owner privately through GitHub with:

- a short description of the issue
- steps to reproduce it
- expected and observed behavior
- any suggested mitigation

Do not include passwords, API keys, tokens, or other private information in reports.

## Current security limitations

The planned production architecture must move external model credentials and tool execution behind a backend. Credentials should never be embedded in browser JavaScript. Future tool execution should also be isolated and constrained with explicit permissions, timeouts, and rate limits.
