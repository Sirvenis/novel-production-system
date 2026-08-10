# Known-Defect Register Specification

Before running the 16-novel regression audit, compile a register of known historical findings so true-positive and false-positive behaviour can be measured.

## Required fields

- defect_id
- series
- book
- source_repo
- source_file_or_report
- evidence_path
- defect_type
- historical_status: fixed / accepted-intentional / unresolved / superseded / uncertain
- severity_at_time
- current_expected_verdict: should-detect / should-not-detect / informational
- notes

## Source priority

1. Canonical series repo reports/status/handoffs.
2. Elias Silver Library catalogue/readiness records only for publication status, not prose truth.
3. Arden Studios/Arden-Hermes institutional records.
4. Session records only where repo records are missing.

A known-defect register must be frozen and hashed before the regression audit sees the manuscripts.
