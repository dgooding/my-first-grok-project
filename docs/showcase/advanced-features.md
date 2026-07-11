---
title: Advanced Material showcase
description: Visual demo of advanced MkDocs Material capabilities for modern documentation sites
tags:
  - showcase
  - advanced
  - material
hide:
  - feedback
---

# Advanced Material showcase

<div class="showcase-hero" markdown>

:material-star-four-points: **What a high-end MkDocs site can look like**

Not a tutorial — a live gallery of Material for MkDocs capabilities. Open this anytime from the **✦ star** in the header.

[Back to home](../index.md){ .md-button .md-button--primary }

</div>

---

## Status dashboard

<div class="grid cards" markdown>

-   :material-check-decagram:{ .lg .middle } **Identity**

    ---

    :material-circle:{ .green } Operational  
    SSO + MFA healthy

-   :material-email-fast:{ .lg .middle } **Email / Teams**

    ---

    :material-circle:{ .green } Operational  
    99.98% last 30 days

-   :material-vpn:{ .lg .middle } **Remote access**

    ---

    :material-circle:{ .orange } Degraded  
    EU node elevated latency

-   :material-shield-alert:{ .lg .middle } **Security**

    ---

    :material-circle:{ .green } Clear  
    No open Sev 1 security events

</div>

### SLA attainment (progress bars)

Identity / SSO — 99.95%  
[=100% "99.95%"]

Email & collaboration — 99.90%  
[=99% "99.90%"]

VPN / remote access — 99.50%  
[=95% "99.50%"]

Service desk portal — 99.70%  
[=97% "99.70%"]

---

## Rich callouts

!!! success "Change window complete"
    Standard change **CHG-10428** (print servers) closed with zero related incidents.

!!! warning "Elevated volume"
    Password-reset tickets +34% vs. weekly baseline after MFA re-enrollment campaign.

!!! danger "Do not share break-glass credentials"
    Emergency admin accounts require dual control and must be checked back into the vault within 60 minutes.

??? tip "Deep dive — why this ticket spiked"
    A mobile OS update invalidated push MFA tokens for a subset of Android devices. Workaround: fall back to TOTP, then re-register the authenticator app.

---

## Multi-path procedures (tabs)

=== "End user"

    1. Open `password.contoso.example`
    2. Complete MFA
    3. Set a 14+ character password
    4. Sign out of all apps and back in

=== "Tier 1 agent"

    1. Verify identity (employee ID + manager + approved contact)
    2. Admin reset with **force change at next sign-in**
    3. Deliver temporary secret on a secure channel
    4. Document steps; resolve ticket

=== "Automation"

    ```yaml title="automation-hook.yml"
    trigger: ticket.category == "password-reset"
    actions:
      - verify_identity:
          methods: [employee_id, manager_ok, mfa_device]
      - idp.reset_password:
          force_change: true
      - notify:
          channel: secure_message
    ```

---

## Annotated automation

```python title="severity_router.py" linenums="1" hl_lines="10-12"
from dataclasses import dataclass

@dataclass
class Impact:
    users: int
    workaround: bool
    security: bool

def route(impact: Impact) -> str:
    if impact.security:
        return "csirt"          # (1)
    if impact.users >= 50:
        return "major-incident" # (2)
    if impact.users >= 5 and not impact.workaround:
        return "tier-2"         # (3)
    return "tier-1"
```

1.  Security-tagged impact never stays in generic queues.
2.  Broad outages open the major-incident path.
3.  Multi-user, no workaround → escalate early.

Keys on this site: ++slash++ opens search · theme toggle switches light/dark · star opens this showcase.

Marked revisions: the SLA is ==four hours== for Sev 3 (was ~~eight hours~~).

---

## Interactive-style data

| Service | Target | Month | Trend | Owner |
|---------|--------|-------|-------|-------|
| Email | 99.9% | 99.97% | :material-trending-up:{ .green } | Messaging |
| VPN | 99.5% | 99.41% | :material-trending-down:{ .red } | Network |
| IdP | 99.95% | 99.99% | :material-trending-up:{ .green } | Identity |
| Portal | 99.5% | 99.88% | :material-trending-neutral:{ .blue } | Service Desk |

*[IdP]: Identity Provider — SSO / MFA platform
*[SLA]: Service Level Agreement

Hover **IdP** and **SLA** for definitions.

---

## Diagrams

### Intake & escalation

``` mermaid
flowchart LR
  U[User] --> P[Portal / Chat / Phone]
  P --> T1[Tier 1]
  T1 -->|Known fix| R[Resolve + KB]
  T1 -->|Complex| T2[Tier 2]
  T2 --> T3[Tier 3 / Vendor]
  T1 -->|Sev 1| MI[Major incident]
  T2 --> MI
  MI --> R
```

### Agent assist sequence

``` mermaid
sequenceDiagram
  actor Agent
  participant KB as Knowledge base
  participant SM as Service mgmt
  participant User

  User->>SM: Open ticket
  Agent->>KB: Search symptom
  alt Article found
    KB-->>Agent: Procedure hit
    Agent->>User: Guided resolution
  else No article
    Agent->>SM: Escalate + flag KB gap
  end
```

### CMDB sketch

``` mermaid
erDiagram
  PERSON ||--o{ DEVICE : assigned
  PERSON ||--o{ TICKET : reports
  DEVICE }o--|| SITE : located-at
  TICKET }o--|| SERVICE : affects
  SERVICE ||--o{ SLA_TARGET : measured-by
```

### Journey — new hire day one

``` mermaid
journey
  title New hire IT day one
  section Arrive
    Collect laptop: 5: HR, Desk
    First sign-in: 4: Employee
  section Secure
    Enroll MFA: 5: Employee
    VPN test: 3: Employee
  section Validate
    Apps open: 4: Employee, Manager
    Ticket closed: 5: Desk
```

---

## Command & config samples

=== "mkdocs.yml (excerpt)"

    ```yaml
    theme:
      name: material
      features:
        - navigation.tabs
        - navigation.instant
        - search.suggest
        - content.code.annotate
    plugins:
      - material/search   # required for header search bar
    markdown_extensions:
      - admonition
      - pymdownx.tabbed:
          alternate_style: true
      - pymdownx.superfences:
          custom_fences:
            - name: mermaid
              class: mermaid
              format: !!python/name:pymdownx.superfences.fence_code_format
    ```

=== "PowerShell deploy"

    ```powershell
    .\.venv\Scripts\Activate.ps1
    mkdocs build
    mkdocs gh-deploy --force
    ```

=== "GitHub Actions idea"

    ```yaml
    on:
      push:
        branches: [master]
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.12"
          - run: pip install -r requirements.txt
          - run: mkdocs gh-deploy --force
    ```

---

## Cards, buttons, and iconography

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Ship docs like product**

    ---

    Versioned Markdown, PR review, instant preview, static publish

-   :material-magnify-scan:{ .lg .middle } **Search-first UX**

    ---

    Suggestions, highlighting, shareable deep links into hits

-   :material-theme-light-dark:{ .lg .middle } **Theme aware**

    ---

    Light / dark / system — diagrams and chrome follow the palette

-   :material-graph-outline:{ .lg .middle } **Visual systems thinking**

    ---

    Mermaid flows beat five-page prose for escalations

</div>

[Open overview](../getting-started/overview.md){ .md-button .md-button--primary }
[Security quick ref](../reference/security-incident.md){ .md-button }
[GitHub repo :fontawesome-brands-github:](https://github.com/dgooding/MKDocs-figuring-out-stuff){ .md-button }

---

## Checklists & definitions

- [x] Sticky navigation tabs  
- [x] Instant loading and search suggest  
- [x] Header search (`material/search`)  
- [x] Custom header action (star → showcase)  
- [x] Mermaid and annotated code  

Incident
:   Unplanned service interruption or degradation.

Request
:   Planned fulfillment work (access, hardware, software).

Problem
:   Underlying cause tracked across related incidents.

---

## Math & footnotes

Availability:

\[
A = \frac{\text{uptime}}{\text{uptime} + \text{downtime}}
\]

Inline form \(A \ge 0.999\) for core collaboration services[^sla].

[^sla]: See [SLA overview](../policies/sla-overview.md) for exclusions and maintenance windows.

---

## Quote strip

> Great internal docs feel like a product: fast search, obvious structure, and visuals that remove ambiguity.
>
> — What this showcase is meant to prove
