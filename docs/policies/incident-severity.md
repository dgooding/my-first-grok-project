---
title: Incident Severity Levels
description: Severity definitions, response targets, and communication rules
tags:
  - policy
  - incidents
  - severity
---

# Incident Severity Levels

!!! info "POL-IM-002 · v1.4"
    Severity is based on **business impact**, not preference alone.

## Severity table

| Severity | Definition | Initial response | Example |
|----------|------------|------------------|---------|
| **Sev 1** | Critical service down for many users or revenue impact | 15 minutes | Email outage company-wide |
| **Sev 2** | Major function degraded; limited workaround | 1 hour | VPN down for one region |
| **Sev 3** | Single user or small group; business continues | 4 hours | One laptop cannot print |
| **Sev 4** | Low impact / cosmetic | 1 business day | Desktop shortcut missing |

## How to choose severity

- Count of users affected
- Whether a viable workaround exists
- Regulatory, safety, or security implications
- Production vs. test environment

## Communication

Sev 1 and Sev 2 require status updates on the major-incident channel until resolved or mitigated.
