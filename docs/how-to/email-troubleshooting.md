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
