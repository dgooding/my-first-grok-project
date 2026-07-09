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
