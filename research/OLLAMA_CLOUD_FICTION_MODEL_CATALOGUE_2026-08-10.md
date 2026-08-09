# Ollama Cloud Models for Arden Studios Fiction Production

Date: 2026-08-10
Scope: Official Ollama Cloud catalogue and preliminary fiction-role triage
Status: Research inventory, not benchmark results or model assignments

## Answer first

Ollama's public library contains hundreds of local model families and many more tags, but Andrew's Ollama Cloud path does not currently expose hundreds or thousands of hosted models. The official Cloud search lists 16 current families, and `https://ollama.com/api/tags` returned 18 exact hosted model tags on 2026-08-10.

The distinction matters:

- **Ollama library:** hundreds of downloadable local models and quantized tags;
- **Ollama Cloud catalogue:** 18 current hosted tags returned by the official API;
- **Andrew's local Ollama list:** previously pulled cloud pointers plus local models; it is not the authoritative current Cloud catalogue;
- **account entitlement:** some models can require a particular subscription or extra credits. Official listing does not guarantee cost-free access under every account.

Official sources:

- https://ollama.com/search?c=cloud
- https://ollama.com/api/tags
- https://docs.ollama.com/cloud

## Current exact Cloud catalogue

| Exact API model | Family/use evidence | Preliminary fiction-lab disposition |
|---|---|---|
| `glm-5.2` | 976K context; long-horizon task model; high usage | Tier A showrunner, architecture, long-manuscript synthesis candidate |
| `deepseek-v4-flash:0731` | 1M context; medium usage; reasoning/tool model | Use current family default instead of pinning dated variant unless benchmark proves otherwise |
| `deepseek-v4-flash:preview` | older preview variant | Exclude from first round; retain only for regression comparison |
| `deepseek-v4-pro` | 1M context; extra-high usage; strongest DeepSeek reasoning variant | Tier A developmental editor/canon auditor; expensive, not first-choice routine prose |
| `kimi-k3` | 1M multimodal frontier model | High-interest writer/showrunner candidate, but official page says Pro/Max plus extra usage credits; cost gate required before testing |
| `kimi-k2.6` | 256K; high usage; proven by Arden on Last Clean-Up Crew | Tier A prose/autonomous-writer baseline, but series specialist rather than universal author |
| `kimi-k2.7-code` | coding-focused K2.6 derivative | Exclude from prose round; possible pipeline automation/tool worker |
| `qwen3.5:397b` | 256K; multimodal; 201 languages; strong instruction following/planning | Tier A research, reader, continuity, and possible prose candidate |
| `minimax-m2.7` | 200K; medium usage; official page highlights character consistency and emotional intelligence | Tier A character, dialogue, reader, and prose candidate |
| `minimax-m3` | 512K guaranteed; high usage; multimodal/agentic/research | Tier B showrunner, researcher, long-context audit candidate |
| `gemma4:31b` | 256K; low-usage Cloud option; multimodal/system prompts | Tier A low-cost reader, editor, and voice-test candidate |
| `mistral-large-3:675b` | 256K; medium usage; strong system-prompt adherence, multilingual, JSON/tooling | Tier A editor, researcher, and controlled prose candidate |
| `nemotron-3-super` | 256K; medium usage; multi-agent/instruction model | Tier B showrunner/structural support; requires fiction-specific retest |
| `nemotron-3-ultra` | 256K hosted; high usage; long-running agent focus | Tier B showrunner/deep-research candidate, not presumed prose specialist |
| `nemotron-3-nano:30b` | 1M; low usage; efficient agentic model | Tier A mechanical audit, inventory, metadata, and cheap-reader candidate |
| `gpt-oss:120b` | 128K; medium usage; reasoning/tools/structured output | Tier B editor, QA, structured analysis candidate |
| `gpt-oss:20b` | 128K; low usage | Tier A mechanical checks and inexpensive baseline |
| `glm-5.1` | 198K; high usage; predecessor to GLM-5.2 | Exclude from first round except as a regression baseline |

## Important retirement findings

The official Ollama Cloud documentation records several July 2026 retirements that affect current Hermes history and profiles:

- `deepseek-v3.2` retired; recommended replacement is `deepseek-v4-flash`;
- `gemini-3-flash-preview` retired;
- `glm-5` and `glm-4.7` retired; recommended replacement is `glm-5.2`;
- older Qwen coder/next cloud variants retired in favour of Qwen 3.5;
- Kimi K2 Thinking/K2 1T retired in favour of Kimi 2.6;
- MiniMax M2.5 retires 2026-07-31 in favour of M2.7.

Therefore `scout-cloud-audit` and any other profile still naming `deepseek-v3.2:cloud` need a later configuration review. This report does not change runtime configuration.

## What official marketing cannot tell us

No official model page proves that a model can write a commercially satisfying Arden Studios novel. Coding, mathematics, tool-use, long-context, and general instruction benchmarks do not measure:

- voice originality and stability;
- scene-level emotional movement;
- character interiority;
- dialogue distinction;
- narrative abundance without padding;
- suspense and reveal timing;
- romance chemistry;
- genre-specific reader satisfaction;
- resistance to summary-like prose;
- preservation during surgical revision.

Those capabilities require Arden-controlled blind tests.

## Recommended first-round shortlist

### Prose and character

- Kimi K2.6 — proven baseline;
- MiniMax M2.7 — high-interest new candidate because character consistency/emotional intelligence are explicitly claimed;
- Qwen 3.5 397B — instruction/long-context/multilingual candidate;
- Gemma 4 31B — low-usage wildcard;
- Mistral Large 3 — system-prompt/controlled-output candidate;
- GPT-5.6 Luna through Codex — non-Ollama comparison baseline.

Kimi K3 enters only after explicit extra-credit approval.

### Architecture/showrunner

- GLM 5.2;
- DeepSeek V4 Pro;
- Qwen 3.5 397B;
- Nemotron 3 Ultra;
- GPT-5.6 Terra/Sol comparison baselines.

### Developmental editing and canon logic

- DeepSeek V4 Pro;
- DeepSeek V4 Flash;
- GLM 5.2;
- Mistral Large 3;
- GPT-5.6 Terra comparison baseline.

### Reader lane

- MiniMax M2.7;
- Gemma 4 31B;
- Qwen 3.5 397B;
- Kimi K2.6;
- GPT-5.6 Luna comparison baseline.

### Research

- Qwen 3.5 397B;
- DeepSeek V4 Flash;
- GLM 5.2;
- MiniMax M3;
- Mistral Large 3.

### Mechanical/QA

- Nemotron 3 Nano 30B;
- GPT-OSS 20B;
- Gemma 4 31B;
- deterministic scripts remain authoritative wherever the check can be encoded.

## Required benchmark controls

1. Freeze and hash shared input packets.
2. Test exact model/provider routes in fresh sessions.
3. Save outputs outside canonical manuscript paths.
4. Blind model identities during human/Scout scoring.
5. Separate writer, editor, and reader rubrics.
6. Include known failure traps: summary prose, repetition, unwanted explanation, voice flattening, invented continuity, over-editing, and chapter truncation.
7. Use deterministic validators for word count, required beats, forbidden terms, preservation, JSON, and citation checks.
8. Record latency, usage class, failures, context limits, and routing deviations.
9. Do not select a model from one sample.
10. Do not promote experimental prose without an explicit canonical gate.

## Commercial-use gate

Before a model becomes a production writer, record the provider terms and model licence relevant to commercial fiction. MiniMax explicitly states official commercial licensing through Ollama Cloud. Other models have Apache, MIT, Gemma, NVIDIA, or model-specific terms. Generated-output rights and provider data handling must be checked rather than inferred from open weights alone.

## Next artifact

Build a reusable `fiction-role-benchmark-v1` pack containing frozen packets, scoring rubrics, automated validators, blind mappings, and a results schema. Run the low/medium-usage candidates first, then high/extra-high candidates only where the cheaper models do not settle the role.