# SIP Rescue Navigator — Planned Skip, Missed Payment Recovery & Flexible Contribution
*Standalone Indian Mutual Fund Investor Continuity MVP*

---

## 1. Product Overview & Purpose

**SIP Rescue Navigator** is a standalone, investor-facing fintech product prototype designed to help retail mutual fund investors navigate temporary cash crunches, upcoming debits, and payment failures without dropping off or incurring avoidable bank penalty charges.

Unlike generic research tools or raw dashboards, **SIP Rescue Navigator** is structured around an actual retail investor journey:
- **Plan Ahead:** Help investors act before their upcoming SIP debit (planned skip, pausing, stepping down).
- **Missed Payment Rescue:** Help investors understand what happened when a scheduled payment was not debited, check mandate health, and evaluate repeat debit risks.
- **Flexible Contribution:** Let investors voluntarily explore an affordable smaller one-time investment in the same fund without modifying their recurring SIP.
- **Comeback Plan:** Supportive reflection reminder and standard .ics calendar generator so investors can pause without fear of losing investment discipline.

### Product Principle:
**Understand the situation -> Explain the available options -> Let the investor choose -> Verify the outcome.**

---

## 2. Realistic Indian Mutual Fund Context

All mutual fund schemes are verified against official AMC product registries:

| AMC Name | Official Scheme Name | Verified Plan / Option | Demo Amount | Frequency | Next Debit Timing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HDFC Mutual Fund** | HDFC Flexi Cap Fund | Direct Plan – Growth | ₹3,000 / mo | Monthly (10th) | Due in 2 days (Cutoff approaching) |
| **SBI Mutual Fund** | SBI Nifty Index Fund *(Nifty 50 Index)* | Direct Plan – Growth | ₹2,000 / mo | Monthly (5th) | Due in 9 days (Active) |
| **ICICI Prudential Mutual Fund** | ICICI Prudential Balanced Advantage Fund | Direct Plan – Growth | ₹2,500 / mo | Monthly (15th) | Due in 18 days (Active) |

*Disclaimer:* All portfolio amounts, account numbers, and debit schedules shown are fictional demo data for prototype evaluation. This application does not connect to actual bank accounts, initiate financial transactions, or alter live bank mandates.

---

## 3. How to Launch Locally

### Option A: Using Python (Recommended)
`ash
python run.py
`
Open **[http://localhost:5173](http://localhost:5173)** in any modern browser.

### Option B: Using Node.js / NPM
`ash
npm run dev
`

---

## 4. Architecture & Key Modules

`	ext
SIP-Rescue-Navigator/
├── index.html                  # HTML5 entry point with responsive viewport
├── css/
│   └── styles.css              # Fintech design system (emerald green, dark navy sidebar, cards)
├── js/
│   ├── app.js                  # Application orchestrator, URL hash router, and view manager
│   ├── components/
│   │   ├── Header.js           # Top branding, demo scenario menu
│   │   ├── TopNav.js           # Search bar, mobile hamburger toggle
│   │   ├── Sidebar.js          # Dark navy sidebar navigation & scenario picker
│   │   ├── HomeScreen.js       # Overview dashboard with Plan Ahead & Missed Payment cards
│   │   ├── SipDetailScreen.js  # Scheme breakdown, lifecycle timeline, rules overview
│   │   ├── PlanAheadFlow.js    # Flow A: 5-step guided wizard for upcoming cash shortages
│   │   ├── MissedPaymentFlow.js# Flow B: Missed payment diagnosis, repeat debit check & choices
│   │   ├── FlexibleContributionView.js # Voluntary one-time investment in same fund
│   │   ├── RescueNavigator.js  # Core Get SIP Help wizard
│   │   ├── ComebackPlan.js     # Reflection review date picker & .ics export
│   │   ├── GuidanceScreen.js   # Platform rules comparison (Groww, Zerodha Coin, AMC Direct)
│   │   └── FeedbackModal.js    # Lightweight feedback widget
│   └── data/
│       ├── sampleSips.js       # Verified Indian mutual fund schemes with illustrative demo data
│       ├── rulesConfig.js      # Deterministic platform rules and decision logic
│       └── demoScenarios.js    # 7 ready-to-run assessor test scenarios
├── run.py                      # Standalone zero-dependency Python local server (port 5173)
├── package.json                # Project descriptor & npm launch scripts
└── README.md                   # Documentation
`

---

## 5. License
MIT License. Built for fintech product evaluation and investor continuity research.
