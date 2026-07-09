"""Build MkDocs Markdown pages + config from service desk sample content."""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PAGES = {
    "getting-started/overview.md": dedent(
        """\
        ---
        title: Service Desk Overview
        description: How Contoso IT Service Desk works and how to get help
        tags:
          - getting-started
          - service-desk
        ---

        # Service Desk Overview

        !!! tip "Welcome"
            This is your single front door for IT help — incidents, requests, and how-to guidance.

        Contoso IT Service Desk is the **single point of contact** for technology issues and service requests. Work is tracked in tickets so nothing falls through the cracks.

        ## How to contact us

        | Channel | When to use | Details |
        |---------|-------------|---------|
        | :material-web: **Portal** | Preferred for most requests | [support.contoso.example](https://support.contoso.example) |
        | :material-email: **Email** | Non-urgent, attach screenshots | servicedesk@contoso.example |
        | :material-phone: **Phone** | Outages & Sev 1 | +1 (555) 010-2000 |
        | :material-chat: **Chat** | Quick questions | Employee portal, 08:00–17:00 |

        ## What we support

        - Windows and managed macOS endpoints
        - Microsoft 365 (Outlook, Teams, SharePoint, OneDrive)
        - Corporate VPN and zero-trust access
        - Standard printers and conference room AV (hardware faults via Facilities)

        ## Business hours

        **Monday–Friday, 08:00–18:00** local time (company holidays excluded).  
        After-hours coverage is limited to **Severity 1** incidents.

        ## Next steps

        <div class="grid cards" markdown>

        -   :material-key-variant:{ .lg .middle } **Password help**

            ---

            Reset your password with self-service or agent steps

            [:octicons-arrow-right-24: Password reset](../how-to/password-reset.md)

        -   :material-vpn:{ .lg .middle } **Connect remotely**

            ---

            Install and troubleshoot corporate VPN

            [:octicons-arrow-right-24: VPN guide](../how-to/vpn-access.md)

        -   :material-alert-decagram:{ .lg .middle } **Severity levels**

            ---

            How impact maps to response times

            [:octicons-arrow-right-24: Severity guide](../policies/incident-severity.md)

        </div>
        """
    ),
    "how-to/password-reset.md": dedent(
        """\
        ---
        title: Password Reset Procedure
        description: Self-service and agent password reset steps
        tags:
          - how-to
          - identity
          - passwords
        ---

        # Password Reset Procedure

        !!! info "SOP-AUTH-001 · v1.2"
            Audience: end users and Tier 1 agents

        Prefer **self-service**. Agents use the procedure below only when self-service fails or the account is locked.

        ## Self-service steps

        1. Go to [password.contoso.example](https://password.contoso.example)
        2. Enter your work email and complete the MFA challenge
        3. Choose a new password (14+ characters, mixed case, number, symbol)
        4. Sign out of all sessions, then sign back in

        ## Agent procedure

        !!! warning "Verify identity first"
            Never reset a password without confirming employee ID, manager, and an approved contact method.

        1. Open the ticket and confirm identity (employee ID, manager, last four of corporate mobile or HR alternate)
        2. In the identity admin console, select **Reset password** and force change at next sign-in
        3. Clear temporary lockouts if present
        4. Provide the temporary password via a **secure channel** (never email permanent secrets)
        5. Advise MFA re-registration if prompts fail after reset
        6. Document steps and resolve the ticket

        ## Common issues

        | Symptom | What to try |
        |---------|-------------|
        | Password works, apps fail | Clear cached credentials, restart, re-auth VPN/MFA |
        | Account locked | Wait 15 minutes or clear lock in admin console |
        | MFA device lost | Escalate to Identity with manager approval |
        | Shared/service account | Do not reset without owner approval |
        """
    ),
    "how-to/vpn-access.md": dedent(
        """\
        ---
        title: VPN Access Guide
        description: Install, connect, and troubleshoot Contoso Secure Access VPN
        tags:
          - how-to
          - network
          - vpn
        ---

        # VPN Access Guide

        !!! info "KB-NET-014 · v2.0"
            Audience: remote workers

        Use the corporate VPN only when you need **internal systems** that are not published through the secure web gateway (legacy file shares, some finance apps, lab networks).

        ## Install and connect

        1. Install **Contoso Secure Access** from Company Portal / Managed Software Center
        2. Sign in with your work account (SSO)
        3. Approve the MFA prompt
        4. Confirm status shows **Connected** and an internal IP is assigned

        ## Troubleshooting

        !!! tip "Collect logs first"
            Use **Help → Export logs** before contacting the service desk.

        - **Home Wi‑Fi blocking UDP** — try alternate port profile or a wired connection
        - **Certificate errors** — restart the device; ensure date/time is automatic
        - **Split tunnel** — internet should still work; only corporate routes use the VPN

        ## Security rules

        - Do not share VPN profiles
        - Personal devices require MDM enrollment before VPN is allowed
        """
    ),
    "how-to/software-requests.md": dedent(
        """\
        ---
        title: Software Installation Requests
        description: How to request approved software on managed devices
        tags:
          - how-to
          - software
          - requests
        ---

        # Software Installation Request Process

        !!! info "SOP-REQ-008 · v1.1"
            Only approved software may be installed on managed devices.

        ## Request flow

        1. Search the **software catalog** for an existing package
        2. If listed → **Request install** (free tier tools auto-approve)
        3. If not listed → open a Service Request with:
            - Business justification
            - Cost center
            - Data classification
        4. Manager approves; Security reviews if regulated data is involved
        5. Packaging team publishes to Company Portal when approved

        ## SLA targets

        | Request type | Target |
        |--------------|--------|
        | Catalog install | 8 business hours |
        | License add-on | 2 business days |
        | New package (standard) | 5 business days |
        | New package (security review) | 10 business days |
        """
    ),
    "how-to/new-hire-checklist.md": dedent(
        """\
        ---
        title: New Employee IT Checklist
        description: Day-zero through first-week IT onboarding tasks
        tags:
          - how-to
          - onboarding
          - checklist
        ---

        # New Employee IT Onboarding Checklist

        !!! info "CHK-HRIT-003 · v3.0"
            For service desk agents and HR partners

        ## Before day one

        - [ ] Create identity account from HR ticket (name, department, manager, start date)
        - [ ] Assign license bundle from role template
        - [ ] Stage laptop image (ship or pickup)
        - [ ] Add security groups (department + VPN if remote)
        - [ ] Schedule welcome email with first-login instructions

        ## Day one

        - [ ] Verify MFA enrollment completed
        - [ ] Confirm email, Teams, and OneDrive sign-in
        - [ ] Map standard printers if site-based
        - [ ] Walk through password self-service registration
        - [ ] Share link to the knowledge base home

        ## Within first week

        - [ ] Confirm access to role-specific applications
        - [ ] Close onboarding ticket only after user confirmation
        - [ ] Tag ticket with site and department for reporting
        """
    ),
    "how-to/email-troubleshooting.md": dedent(
        """\
        ---
        title: Email Troubleshooting
        description: Tier 1 triage for Outlook desktop and mobile mail
        tags:
          - how-to
          - email
          - microsoft-365
        ---

        # Email Troubleshooting Guide

        !!! info "KB-M365-021 · v1.6"
            Audience: Tier 1 agents

        ## Quick triage

        Before changing settings, determine whether the issue is **send**, **receive**, **calendar**, or **mobile-only**.

        - Can the user sign in at [outlook.office.com](https://outlook.office.com)?
        - Does the issue affect one device or all devices?
        - Any recent password or MFA changes?
        - Is the mailbox full (quota warning)?

        ## Desktop Outlook

        1. Repair Office apps from **Settings → Apps**
        2. Create a new Outlook profile if the profile is corrupt
        3. Clear Credential Manager entries for `MicrosoftOffice*`
        4. Check rules and Focused Inbox for missing mail

        ## Mobile mail

        1. Remove and re-add the work account in **Outlook mobile**
        2. Confirm device compliance in Company Portal
        3. Do **not** recommend native iOS/Android mail for corporate accounts

        ## Escalate when

        !!! danger "Messaging team"
            Mailbox corruption, litigation hold issues, transport rule failures, or hybrid mail flow problems — assign to Messaging with logs attached.
        """
    ),
    "how-to/remote-desktop.md": dedent(
        """\
        ---
        title: Remote Desktop Access SOP
        description: How agents start audited remote support sessions
        tags:
          - how-to
          - remote-support
          - euC
        ---

        # Remote Desktop Access SOP

        !!! info "SOP-EUC-011 · v1.0"
            Audience: support agents

        ## Policy

        Interactive remote control requires **user consent**, except break-glass admin scenarios approved by the duty manager.

        ## Starting a remote session

        1. Open the remote support tool from the agent console
        2. Enter the **ticket number** (required for audit)
        3. Send the session invitation to the user
        4. Wait for **Accept** on the user device
        5. Announce actions before making system changes
        6. End the session and note the outcome in the ticket

        ## Prohibited actions

        - Do not disable security tools without Security approval
        - Do not copy personal files off the device
        - Do not share your admin credentials with the user
        """
    ),
    "how-to/hardware-requests.md": dedent(
        """\
        ---
        title: Hardware Asset Requests
        description: Order laptops, monitors, and peripherals from the catalog
        tags:
          - how-to
          - hardware
          - assets
        ---

        # Hardware Asset Request Guide

        !!! info "SOP-AM-006 · v1.2"

        ## Eligible hardware

        | Item | Refresh cycle | Notes |
        |------|---------------|-------|
        | Laptop | 3–4 years | Role-based models only |
        | Monitor | 5 years | Max two per desk by default |
        | Headset | As needed | Noise-cancelling standard |

        ## How to request

        1. Open **Service Request → Hardware**
        2. Select catalog item and ship-to address
        3. Manager approval required for non-standard items
        4. Asset tag is recorded on delivery; return old kit on refresh

        ## Lost or stolen devices

        !!! danger "Report immediately"
            Contact Service Desk **and** Security. Do not delay waiting on a replacement request.
        """
    ),
    "how-to/printers-peripherals.md": dedent(
        """\
        ---
        title: Printers and Peripherals
        description: Support checklist for printers, docks, and monitors
        tags:
          - how-to
          - printers
          - peripherals
        ---

        # Printer and Peripheral Support

        !!! info "KB-EUC-033 · v1.0"

        ## Supported devices

        Corporate networked printers, standard USB headsets, webcams, and docking stations listed in the hardware catalog.

        ## Printer issues checklist

        1. Confirm the user is on the corporate network or VPN if required
        2. Reinstall the printer from the print server share
        3. Clear stuck jobs from the print queue
        4. Check toner/paper and physical error lights
        5. Escalate to Facilities for paper jams needing hardware service

        ## Docking and monitors

        Update dock firmware via Company Portal. Try a different USB‑C/Thunderbolt cable before replacing hardware.

        !!! tip "MkDocs tip"
            You could later split this into `printers.md` and `docks-monitors.md` linked from a peripherals index.
        """
    ),
    "policies/incident-severity.md": dedent(
        """\
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
        """
    ),
    "policies/sla-overview.md": dedent(
        """\
        ---
        title: SLA Overview
        description: Availability targets and what the service desk SLA covers
        tags:
          - policy
          - sla
        ---

        # Service Level Agreement Overview

        !!! info "POL-SLA-001 · v2.1"

        ## Scope

        This SLA covers Contoso IT services delivered through the Service Desk for full-time employees and long-term contractors.

        - Incident response and resolution targets by severity
        - Service request fulfillment targets
        - Planned maintenance windows

        ## Availability targets

        Core collaboration services target **99.9%** monthly availability excluding announced maintenance.

        | Service | Target availability |
        |---------|---------------------|
        | Email / Teams | 99.9% |
        | VPN / remote access | 99.5% |
        | Service desk portal | 99.5% |
        | Identity / SSO | 99.95% |

        ## Exclusions

        Force majeure, customer-owned networks, and unsanctioned software are excluded from SLA credits.
        """
    ),
    "policies/change-management.md": dedent(
        """\
        ---
        title: Change Management Basics
        description: Standard, normal, and emergency changes
        tags:
          - policy
          - change
        ---

        # Change Management Basics

        !!! info "POL-CHG-001 · v1.5"

        ## Goal

        Changes to production IT services are planned, reviewed, and communicated to reduce unplanned downtime.

        ## Change types

        | Type | Approval | Lead time |
        |------|----------|-----------|
        | Standard | Pre-approved | As scheduled |
        | Normal | CAB / manager | 3 business days |
        | Emergency | Duty manager | As needed |

        ## Service desk role

        - Communicate maintenance windows to users
        - Monitor incidents during change implementation
        - Link related incidents to the change record
        """
    ),
    "reference/escalation-matrix.md": dedent(
        """\
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
        """
    ),
    "reference/kb-authoring.md": dedent(
        """\
        ---
        title: Knowledge Base Authoring
        description: How to write articles that work well in MkDocs
        tags:
          - reference
          - documentation
          - mkdocs
        ---

        # Knowledge Base Authoring Guidelines

        !!! info "STD-KB-004 · v1.0"
            Consistent structure makes search and navigation delightful.

        ## Why structure matters

        MkDocs shines when articles use clear titles, short procedures, and consistent headings — exactly what you see across this sample site.

        ## Article template

        1. **Title** — task-oriented (e.g. *Reset your VPN client*)
        2. **Summary** — 1–2 sentences
        3. **Before you begin** — prerequisites
        4. **Steps** — numbered, one action each
        5. **Result** — what success looks like
        6. **Related articles** — links

        ## Style rules

        - Active voice, second person (*you*)
        - Screenshots only when the UI is non-obvious
        - Risk callouts with admonitions (`!!! warning`, `!!! danger`)
        - Review quarterly or after major product changes

        ## MkDocs learning tip

        Map each source heading to `##` / `###`, turn bullets into Markdown lists, and place pages under topic folders like `how-to/` and `policies/`.
        """
    ),
    "reference/security-incident.md": dedent(
        """\
        ---
        title: Security Incident Quick Reference
        description: First response for phishing, lost devices, and suspected compromise
        tags:
          - reference
          - security
        ---

        # Security Incident Quick Reference

        !!! danger "REF-SEC-002 · Internal"
            Treat suspected security events as high priority.

        ## If you suspect a security incident

        Examples: phishing click, ransomware symptoms, lost device with data, unexpected admin prompts, accidental external data email.

        1. Prefer preserving evidence — disconnect network if malware is active; do not wipe unless instructed
        2. Contact Service Desk and mark the ticket **Security**
        3. Notify Security CSIRT for confirmed or high-confidence events
        4. Do not delete emails or files that may be evidence

        ## Phishing reports

        - Use the **Report phishing** button in Outlook
        - Forward as attachment only if the button is missing
        - Never enter credentials on linked pages from suspicious mail

        ## Service desk first response

        If credential theft is likely: reset password, revoke sessions, review MFA methods, then escalate to CSIRT with a timeline.
        """
    ),
}

INDEX = dedent(
    """\
    ---
    title: Home
    hide:
      - navigation
      - toc
    ---

    # Contoso Service Desk Knowledge Base

    <p class="hero-lead">
      Searchable playbooks for agents and employees — passwords, VPN, severity, SLAs, and more.
      Built with <strong>MkDocs Material</strong> so you can learn docs-as-code.
    </p>

    <div class="hero-search-hint" markdown>
    :material-magnify: Press :material-slash: or use the search bar above — try **VPN**, **password**, or **Sev 1**.
    </div>

    ## Browse by category

    <div class="grid cards" markdown>

    -   :material-rocket-launch:{ .lg .middle } **Getting started**

        ---

        How the service desk works and how to get help

        [:octicons-arrow-right-24: Overview](getting-started/overview.md)

    -   :material-hammer-wrench:{ .lg .middle } **How-to guides**

        ---

        Step-by-step fixes and request processes

        [:octicons-arrow-right-24: Password reset](how-to/password-reset.md)

    -   :material-scale-balance:{ .lg .middle } **Policies**

        ---

        Severity, SLA, and change management

        [:octicons-arrow-right-24: Severity levels](policies/incident-severity.md)

    -   :material-book-open-page-variant:{ .lg .middle } **Reference**

        ---

        Escalation matrix, security, and authoring

        [:octicons-arrow-right-24: Escalation matrix](reference/escalation-matrix.md)

    </div>

    ## Popular articles

    | Topic | Article |
    |-------|---------|
    | Identity | [Password reset procedure](how-to/password-reset.md) |
    | Remote work | [VPN access guide](how-to/vpn-access.md) |
    | Incidents | [Severity levels](policies/incident-severity.md) |
    | Security | [Security incident quick reference](reference/security-incident.md) |
    | Onboarding | [New hire IT checklist](how-to/new-hire-checklist.md) |
    | Email | [Email troubleshooting](how-to/email-troubleshooting.md) |

    ## Site map (all 15 articles)

    ??? abstract "Full article list"
        **Getting started**

        - [Service Desk Overview](getting-started/overview.md)

        **How-to**

        - [Password Reset](how-to/password-reset.md)
        - [VPN Access](how-to/vpn-access.md)
        - [Software Requests](how-to/software-requests.md)
        - [New Hire Checklist](how-to/new-hire-checklist.md)
        - [Email Troubleshooting](how-to/email-troubleshooting.md)
        - [Remote Desktop SOP](how-to/remote-desktop.md)
        - [Hardware Requests](how-to/hardware-requests.md)
        - [Printers & Peripherals](how-to/printers-peripherals.md)

        **Policies**

        - [Incident Severity](policies/incident-severity.md)
        - [SLA Overview](policies/sla-overview.md)
        - [Change Management](policies/change-management.md)

        **Reference**

        - [Escalation Matrix](reference/escalation-matrix.md)
        - [KB Authoring](reference/kb-authoring.md)
        - [Security Incident](reference/security-incident.md)

    ---

    <p class="footer-note">Sample training content for learning MkDocs · Source Word/PDF files live in <code>sample-data/</code></p>
    """
)

MKDOCS_YML = dedent(
    """\
    site_name: Contoso Service Desk
    site_description: Searchable IT service desk knowledge base — sample project for learning MkDocs
    # site_url: https://dgooding.github.io/my-first-grok-project/
    repo_url: https://github.com/dgooding/my-first-grok-project
    repo_name: dgooding/my-first-grok-project
    edit_uri: edit/master/docs/
    copyright: Sample content for MkDocs training · Contoso is a fictional company

    theme:
      name: material
      custom_dir: overrides
      language: en
      favicon: assets/favicon.svg
      logo: assets/logo.svg
      palette:
        - media: "(prefers-color-scheme)"
          toggle:
            icon: material/brightness-auto
            name: Switch to light mode
        - media: "(prefers-color-scheme: light)"
          scheme: default
          primary: custom
          accent: custom
          toggle:
            icon: material/weather-night
            name: Switch to dark mode
        - media: "(prefers-color-scheme: dark)"
          scheme: slate
          primary: custom
          accent: custom
          toggle:
            icon: material/weather-sunny
            name: Switch to system preference
      font:
        text: Inter
        code: JetBrains Mono
      features:
        - announce.dismiss
        - content.action.edit
        - content.code.copy
        - content.tabs.link
        - content.tooltips
        - navigation.expand
        - navigation.footer
        - navigation.indexes
        - navigation.instant
        - navigation.instant.prefetch
        - navigation.path
        - navigation.sections
        - navigation.tabs
        - navigation.tabs.sticky
        - navigation.top
        - navigation.tracking
        - search.highlight
        - search.share
        - search.suggest
        - toc.follow

    plugins:
      - search:
          lang: en
          separator: '[\\s\\-_,:!=\\[\\]()"/]+|(?!=\\b)(?=[A-Z][a-z])|\\.(?!\\d)|(?<=\\d)\\.'
      - tags
      - git-revision-date-localized:
          enable_creation_date: true
          enable_git_follow: false
          type: timeago
          fallback_to_build_date: true

    extra_css:
      - stylesheets/extra.css

    extra:
      social:
        - icon: fontawesome/brands/github
          link: https://github.com/dgooding/my-first-grok-project
          name: Repository
      generator: false
      tags: {}

    markdown_extensions:
      - abbr
      - admonition
      - attr_list
      - def_list
      - footnotes
      - md_in_html
      - tables
      - toc:
          permalink: true
          toc_depth: 3
      - pymdownx.arithmatex:
          generic: true
      - pymdownx.betterem
      - pymdownx.caret
      - pymdownx.details
      - pymdownx.emoji:
          emoji_index: !!python/name:material.extensions.emoji.twemoji
          emoji_generator: !!python/name:material.extensions.emoji.to_svg
      - pymdownx.highlight:
          anchor_linenums: true
          line_spans: __span
          pygments_lang_class: true
      - pymdownx.inlinehilite
      - pymdownx.keys
      - pymdownx.mark
      - pymdownx.smartsymbols
      - pymdownx.superfences
      - pymdownx.tabbed:
          alternate_style: true
      - pymdownx.tasklist:
          custom_checkbox: true
      - pymdownx.tilde

    nav:
      - Home: index.md
      - Getting started:
          - Overview: getting-started/overview.md
      - How-to:
          - Password reset: how-to/password-reset.md
          - VPN access: how-to/vpn-access.md
          - Software requests: how-to/software-requests.md
          - New hire checklist: how-to/new-hire-checklist.md
          - Email troubleshooting: how-to/email-troubleshooting.md
          - Remote desktop: how-to/remote-desktop.md
          - Hardware requests: how-to/hardware-requests.md
          - Printers & peripherals: how-to/printers-peripherals.md
      - Policies:
          - Incident severity: policies/incident-severity.md
          - SLA overview: policies/sla-overview.md
          - Change management: policies/change-management.md
      - Reference:
          - Escalation matrix: reference/escalation-matrix.md
          - KB authoring: reference/kb-authoring.md
          - Security incident: reference/security-incident.md
    """
)

EXTRA_CSS = dedent(
    """\
    /* Contoso Service Desk — custom Material theme accents */
    :root {
      --sd-indigo: #4f46e5;
      --sd-violet: #7c3aed;
      --sd-cyan: #06b6d4;
      --sd-glow: rgba(79, 70, 229, 0.35);
    }

    [data-md-color-scheme="default"] {
      --md-primary-fg-color: #4f46e5;
      --md-primary-fg-color--light: #818cf8;
      --md-primary-fg-color--dark: #3730a3;
      --md-accent-fg-color: #06b6d4;
      --md-typeset-a-color: #4f46e5;
    }

    [data-md-color-scheme="slate"] {
      --md-primary-fg-color: #818cf8;
      --md-primary-fg-color--light: #a5b4fc;
      --md-primary-fg-color--dark: #6366f1;
      --md-accent-fg-color: #22d3ee;
      --md-typeset-a-color: #a5b4fc;
      --md-default-bg-color: #0b1020;
      --md-default-bg-color--light: #121a2f;
      --md-default-bg-color--lighter: #1a243d;
      --md-default-bg-color--lightest: #243050;
    }

    /* Hero */
    .md-typeset h1 {
      font-weight: 800;
      letter-spacing: -0.03em;
      background: linear-gradient(120deg, var(--sd-indigo), var(--sd-violet) 45%, var(--sd-cyan));
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    .hero-lead {
      font-size: 1.15rem;
      line-height: 1.6;
      opacity: 0.9;
      max-width: 42rem;
      margin: 0.5rem 0 1.25rem;
    }

    .hero-search-hint {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.65rem 1rem;
      border-radius: 999px;
      border: 1px solid color-mix(in srgb, var(--sd-indigo) 35%, transparent);
      background: color-mix(in srgb, var(--sd-indigo) 10%, transparent);
      box-shadow: 0 0 0 4px var(--sd-glow);
      margin-bottom: 1.75rem !important;
      font-size: 0.92rem;
    }

    /* Cards polish */
    .md-typeset .grid.cards > ul > li,
    .md-typeset .grid.cards > ol > li {
      border-radius: 0.9rem;
      border: 1px solid color-mix(in srgb, var(--md-default-fg-color) 12%, transparent);
      box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
      transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    }

    .md-typeset .grid.cards > ul > li:hover,
    .md-typeset .grid.cards > ol > li:hover {
      transform: translateY(-3px);
      border-color: color-mix(in srgb, var(--sd-indigo) 55%, transparent);
      box-shadow: 0 16px 40px rgba(79, 70, 229, 0.18);
    }

    /* Tables */
    .md-typeset table:not([class]) {
      border-radius: 0.75rem;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06);
    }

    .md-typeset table:not([class]) th {
      background: linear-gradient(120deg, #4f46e5, #7c3aed);
      color: #fff;
      font-weight: 600;
    }

    [data-md-color-scheme="slate"] .md-typeset table:not([class]) th {
      background: linear-gradient(120deg, #4338ca, #6d28d9);
    }

    /* Header bar subtle glass */
    .md-header {
      backdrop-filter: blur(10px);
    }

    .md-header__button.md-logo img,
    .md-header__button.md-logo svg {
      height: 1.6rem;
    }

    .footer-note {
      opacity: 0.65;
      font-size: 0.85rem;
    }

    /* Search modal emphasis */
    .md-search__form {
      border-radius: 0.6rem;
    }

    .md-search__input {
      border-radius: 0.6rem;
    }
    """
)

LOGO_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Contoso Service Desk">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="55%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="16" fill="url(#g)"/>
  <path d="M18 40V24c0-2.2 1.8-4 4-4h8.5c5 0 8.5 3.2 8.5 7.6 0 3-1.7 5.4-4.4 6.6L40 44h-5.2l-4.5-8.8H27V44H18zm9-14.2v6.6h4.2c2.2 0 3.5-1.2 3.5-3.2s-1.3-3.4-3.5-3.4H27z" fill="#fff"/>
  <circle cx="46" cy="42" r="5" fill="#22d3ee"/>
</svg>
"""

FAVICON_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#06b6d4"/>
    </linearGradient>
  </defs>
  <rect width="32" height="32" rx="8" fill="url(#g)"/>
  <path d="M9 22V10h6.2c3.2 0 5.3 1.9 5.3 4.6 0 1.9-1.1 3.4-2.9 4.1L21 22h-3.2l-2.8-5.2H12.4V22H9zm3.4-8.3v3.8h2.4c1.4 0 2.2-.7 2.2-1.9s-.8-1.9-2.2-1.9h-2.4z" fill="#fff"/>
</svg>
"""

MAIN_HTML = dedent(
    """\
    {% extends "base.html" %}

    {% block announce %}
      <aside>
        <strong>MkDocs training site</strong> — press
        <kbd>/</kbd> to search all 15 service desk articles.
      </aside>
    {% endblock %}
    """
)


def main():
    for rel, body in PAGES.items():
        path = DOCS / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")

    (DOCS / "index.md").write_text(INDEX, encoding="utf-8")
    print("wrote docs/index.md")

    styles = DOCS / "stylesheets"
    styles.mkdir(parents=True, exist_ok=True)
    (styles / "extra.css").write_text(EXTRA_CSS, encoding="utf-8")
    print("wrote docs/stylesheets/extra.css")

    assets = DOCS / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    (assets / "logo.svg").write_text(LOGO_SVG, encoding="utf-8")
    (assets / "favicon.svg").write_text(FAVICON_SVG, encoding="utf-8")
    print("wrote logo + favicon")

    overrides = ROOT / "overrides"
    overrides.mkdir(parents=True, exist_ok=True)
    (overrides / "main.html").write_text(MAIN_HTML, encoding="utf-8")
    print("wrote overrides/main.html")

    (ROOT / "mkdocs.yml").write_text(MKDOCS_YML, encoding="utf-8")
    print("wrote mkdocs.yml")


if __name__ == "__main__":
    main()
