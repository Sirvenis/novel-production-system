Treat all material as invented and noncanonical. Use no tools or outside sources. Create exactly eight beats G1–G8. Each beat must provide purpose, visible action, reader effect, evidence boundary, continuity risk, and exit condition. Retain every explicit detail, including the exact paper-tag wording. Build causal escalation rather than a checklist. Separate evidence from character inference. Protect downstream canon and future-story options. Provide at least four protected non-actions, an escalation curve, Tamsin's final decision, and a bounded writer handoff with required inclusions and prohibited conclusions. Return no scene prose.

STRICT OUTPUT CONTRACT:
- Output exactly one JSON object satisfying the supplied schema.
- Output ONLY properties permitted by the supplied schema.
- Do not emit a `$schema` property; `$schema` is not defined as an allowed output property.
- Do not place any explanatory preamble outside the JSON object.
- Do not place any commentary after the JSON object.
- Do not add Markdown fences.
- Do not introduce metadata or unknown properties.
- Property names must match exactly.
- Every required property must be present.
- Prohibited or unknown properties cause deterministic failure.
- The evaluator will not repair, strip, or normalise candidate-created structural violations.
