# Final Showrunner Compliance-Gate Evidence

One candidate attempt only; zero retries. The candidate used exact `openai-codex / gpt-5.6-luna` through `gpt56-luna`, resolved zero tools, and made zero tool turns. Exact schema validation passed with no additional properties, no `$schema`, no fences, no preamble, and no trailing commentary.

Blind scoring was performed from the identity-free `CANDIDATE-001` bundle. Leakage scan passed with zero leaks. Substantive score: 98/100; no material regression.

The launcher encountered a post-response Python call-signature exception after the exact candidate response, judged submission, normalization record, and route log had already been preserved. The candidate was not retried. The already-frozen validator was invoked directly on the exact submission and the bookkeeping record reconstructed from preserved evidence. See `final-luna-showrunner-c1/harness-recovery-record.json`.

Final result: PASS. Recommendation only: `SHOWRUNNER — ELIGIBLE FOR ANDREW / ARDEN FINAL PRODUCTION-ASSIGNMENT APPROVAL.` No production assignment or policy change occurred.
