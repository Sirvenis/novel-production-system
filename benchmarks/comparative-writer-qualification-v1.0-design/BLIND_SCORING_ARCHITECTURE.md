# Writer Blind-Scoring Architecture

1. Candidate execution creates raw outputs in isolated candidate folders.
2. Deterministic validator runs before human scoring; Category D failures are visible to Scout but candidate text may still be scored for diagnostic value if Andrew / Arden want failure-mode data.
3. Blind-pack builder assigns CANDIDATE-001..N using a seed recorded outside scorer packets.
4. Fresh reader, editor, and showrunner scorers receive only anonymized packets and the relevant scoring lens.
5. Scorers must declare: independent / received prior analysis / saw identity / saw other scorer output.
6. Identity reveal occurs only after all valid blind scores are frozen and hash-recorded.
7. Scout synthesizes deterministic results, blind scores, route evidence, cost/usage, and revision burden.
8. Andrew / Arden decide whether any candidate advances to holdout or production consideration.
