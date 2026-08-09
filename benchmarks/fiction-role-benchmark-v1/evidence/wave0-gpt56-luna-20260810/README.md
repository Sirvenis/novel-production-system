# Wave 0 Raw Evidence — GPT-5.6 Luna / OpenAI Codex

Date: 2026-08-10
Scope: authorised Wave 0 calibration only.

- `a1` preserves the initial launcher attempt. The empty `--toolsets` override was ignored, leaving profile tools available; all seven a1 records are retained and marked invalid. Three runs actually used one tool turn before Hermes' max-turn summary path.
- `a2` preserves the controlled rerun with effective no-tool execution (`--toolsets none`). Hermes printed a known CLI warning to raw stdout; the warning remains in `raw-stdout.txt` and was removed only from the extracted `submission.*` artifact.
- Every served route was verified from the profile-local agent log as `gpt-5.6-luna` via `openai-codex`.
- Raw outputs are evidence only, noncanonical, and not promoted.
- Identity-visible raw evidence was committed before blind scoring or human craft evaluation.
