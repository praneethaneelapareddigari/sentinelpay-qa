# Bug Report

**Title:** [PAY-####] Incorrect tax calculation for multi-currency invoice (INR → USD)

**Severity:** High | **Priority:** P0  
**Environment:** Staging | **Build:** 2025-09-24 | **Browser:** Chrome 119

## Steps to Reproduce
1. Create payment intent: amount=1999, currency=INR
2. Change currency to USD during checkout
3. Apply GST=18% then confirm payment

## Expected
- Tax computed once using correct currency basis
- Invoice shows consistent totals

## Actual
- Double‑application of tax when currency switch occurs

## Evidence
- Postman run: `reports/newman.html`
- Pytest: `reports/pytest_api.html`
- Screenshot: `screenshots/pytest_report.png`

## Notes / Suspected Cause
Race on currency conversion service; missing idempotency key on taxation call.

## Links
- Story: PAY-102
- Test Case: TC‑TAX‑MC‑07
