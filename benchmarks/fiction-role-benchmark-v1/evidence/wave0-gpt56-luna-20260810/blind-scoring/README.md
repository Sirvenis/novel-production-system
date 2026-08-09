# Wave 0 Blind Scoring Evidence

- `locked-original/` preserves the seven blind evaluator score files exactly as written.
- `locked-score-sha256.json` records their hashes. The files existed and passed schema validation before Scout read the private identity map, but the hash manifest itself was written immediately after reveal; this sequencing deviation is recorded rather than hidden.
- `scorer-route-evidence.txt` proves the delegated scorer sessions began on configured Kimi K2.6, activated fallback, and were actually served by `gpt-5.5 / openai-codex`.
- Original scorer IDs incorrectly said `terra` because the orchestration prompt assumed rather than verified the child route. `adjudicated/` corrects scorer metadata, preserves human scores, applies deterministic penalties, and marks every run ineligible because each failed a hard gate.
- The private identity map and seed remain outside Git with mode 600.
