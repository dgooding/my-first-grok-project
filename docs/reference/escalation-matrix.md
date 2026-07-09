---
title: Escalation Matrix
description: When and how to escalate incidents
tags:
  - reference
  - escalation
---

# Escalation Matrix

!!! info "REF-IM-010 · v1.3"

## When to escalate

Escalate when the SLA is at risk, the issue exceeds Tier 1 skills, or a major incident is declared.

| Level | Owner | Trigger |
|-------|-------|---------|
| Tier 1 | Service Desk | Initial triage and known fixes |
| Tier 2 | Platform teams | Complex config, multi-user impact |
| Tier 3 | Engineering / vendor | Code defects, infrastructure faults |
| Major Incident | Duty manager | Sev 1 or widespread Sev 2 |

## Contacts (sample)

- **Duty manager on-call** — PagerDuty schedule `IT-Duty`
- **Security CSIRT** — security@contoso.example
- **Vendor bridge** — open only after Tier 3 acknowledges

## Documentation required

Every escalation must include timeline, impact statement, reproduction steps, and current workaround.
