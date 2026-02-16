# Strategic Execution Roadmap: Welfare Optimization Protocol

This roadmap outlines the necessary steps to realize the maximum potential value (559.440 DKK/year) defined in `maximum_potential_analysis.json`. It is divided into three distinct phases: Bureaucratic Setup, Liquidity Activation, and Asset Acquisition.

## Phase 1: Bureaucratic Setup (Months 1-2)

**Goal:** Establish the legal entity and secure compliance.

1.  **Entity Formation:**
    *   **Action:** Hold "Stiftende Generalforsamling" and register "Frivillig Forening" with CVR (Danish Business Register).
    *   **Status:** *Pending*.
    *   **Tools:**
        *   [Vedtægter Template](templates/association_statutes.md) - Use this for the association's legal statutes.
        *   [Referat af Stiftende Generalforsamling](templates/founding_minutes.md) - Use this to document the founding meeting.
    *   **Constraint:** Ensure "Ingen moms" (No VAT) registration.
    *   **Deliverable:** CVR Number.

2.  **Bank Account Setup:**
    *   **Action:** Open a dedicated association bank account (Foreningskonto).
    *   **Status:** *Pending*.
    *   **Constraint:** Must be separate from personal NemKonto to avoid contamination.
    *   **Cost:** Approx. 1.000-2.500 DKK setup fee (use personal funds initially, reimburse later).

3.  **Chairman Recruitment:**
    *   **Action:** Recruit an external chairman (non-beneficiary) to sign off on accounts.
    *   **Status:** *Pending*.
    *   **Why:** Risk mitigation. Proves to authorities that Mik/Sofie/Tomas do not control the payouts directly.

## Phase 2: Liquidity Activation (Months 2-3)

**Goal:** Unlock the 163.440 DKK liquid cash flow (Socialfrikort).

1.  **Municipal Approval (Visitation):**
    *   **Action:** Each member (Mik, Sofie, Tomas) contacts their caseworker.
    *   **Script:** Use the [Visitation Script](templates/visitation_script.md) to prepare for the meeting.
    *   **Target:** Approval letter within 4 weeks.

2.  **Socialfrikort Registration:**
    *   **Action:** Register the association as a "godkendt udbetaler" on `socialfrikort.dk`.
    *   **Status:** *Pending*.
    *   **Process:** Link CVR number to the Socialfrikort system.

3.  **Payout Execution:**
    *   **Action:** Report hours/tasks monthly.
    *   **Limit:** Max 3.440 DKK/month per person (to hit 41.280/year evenly).
    *   **Tracking:** Use `accounting/socialfrikort_ledger.json`.

## Phase 3: Asset Acquisition (Months 3-12)

**Goal:** Secure the 300.000 DKK in asset value and 96.000 DKK in operational savings.

1.  **§18 Application (The Foundation):**
    *   **Action:** Submit application to the local municipality's "Pulje til Frivilligt Socialt Arbejde".
    *   **Template:** Use `templates/grant_application_section18.md`.
    *   **Ask:** 50.000 DKK for "Opstart af kulturelt værested".

2.  **Private Foundations (The Expansion):**
    *   **Action:** Apply to 3-5 private foundations (e.g., Tuborgfondet, Nordea-fonden).
    *   **Focus:** "Music equipment for vulnerable youth" (Mik's domain) or "Community Kitchen" (Sofie's domain).
    *   **Target:** 200.000 DKK total.

3.  **Operational Subsidy Activation:**
    *   **Action:** Schedule 2 weekly events (Community Dinner / Music Workshop).
    *   **Benefit:** Association pays for food/transport.
    *   **Result:** Participants save personal food budget (approx. 600 kr/event).

## Annual Review & Compliance

*   **Audit:** External chairman reviews `socialfrikort_ledger.json`.
*   **Report:** Submit annual report to municipality for §18 funds.
*   **Tax Check:** Ensure commercial sales < 50.000 DKK to stay VAT exempt.
