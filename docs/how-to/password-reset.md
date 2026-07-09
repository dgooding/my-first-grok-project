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
