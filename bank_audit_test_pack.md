# Bank Audit Web Platform — Pro SDET Test Pack
Author: Pro SDET Freelancer  
Date: 2025-08-23  

> This pack lists **20 business flows** and **10 expert-level test scenarios** for each of the bank's 10 audit services. Flows are phrased for end-to-end validation of a **web-based Audit platform** (UI + APIs + data + controls). Scenarios emphasize negative paths, edge cases, controls, and non-functional concerns relevant to enterprise banking.

---

## 1) Regulatory Compliance Auditing

### 20 Business Flows
1. **Customer Onboarding KYC Review** → ingest documents, run PEP/sanctions screening, risk-rate customer, record evidence, generate approval memo.
2. **Periodic KYC Refresh** → auto-detect due profiles, notify RM, re-collect docs, re-screen, update risk, close with attestation.
3. **Sanctions List Delta Refresh** → fetch OFAC/UN/EU lists, apply deltas, re-screen impacted customers/transactions, log matches.
4. **Adverse Media Screening** → trigger batch screening, triage hits, attach evidence, disposition with second-level review.
5. **UBO & Corporate Structure Validation** → parse corporate tree, verify beneficial owners, risk-rate entity, store lineage.
6. **CTR/STR/SMR Workflow** → detect thresholds, create case, analyst review, manager approval, file report, archive proof.
7. **Cross-Border Activity Review** → identify high-risk corridors, sample transactions, verify documents, record outcomes.
8. **High-Risk Product Onboarding** (e.g., correspondent banking) → enhanced due diligence, approvals, periodic monitoring.
9. **Regulation Change Impact Assessment** → import rule text, map to controls, gap analysis, rollout plan, evidence closure.
10. **Internal Policy Attestation** → assign policies to users/branches, track read/understood, chase exceptions.
11. **SoD (Segregation of Duties) Check** → review user roles, detect conflicts, route for remediation/compensating controls.
12. **Data Retention & Deletion Audit** → verify DPDP/GDPR retention schedules, approve deletions, export audit log.
13. **Customer Risk Re-Scoring** after event (address change, PEP update) → auto-trigger re-assessment and approvals.
14. **Model Governance for Screening Engine** → register model, approvals, performance monitoring, periodic validation.
15. **Third-Party Due Diligence** → vendor onboarding, risk questionnaire, sanctions & financial checks, approval workflow.
16. **Training & Certification Tracking** → assign AML/KYC courses, track completions, escalate overdue, report coverage.
17. **Evidence Sampling & Quality Review** → define sample plan, pull samples, QA evidence, issue fixes with SLA.
18. **Exception/Risk Acceptance Register** → request exception, risk eval, approval, expiry reminders, closure.
19. **Regulatory Exam Readiness** → compile artifacts binder, redaction, secure share with regulators, access logs.
20. **Branch Compliance Scorecard** → compute KPIs (overdues, defects), publish dashboards, action plans, monthly close.

### 10 Expert-Level Test Scenarios
1. **Sanctions Delta Mismatch**: simulate stale list cache vs new list; verify forced re-screen & reconciliation.
2. **Timezone Cutoff Edge**: filings due 23:59 UTC vs IST; ensure correct due-date and late-flag behavior.
3. **PEP False Negative Due to Diacritics**: name normalization test across locales & transliterations.
4. **Backdated Policy Effective Date**: rule versioning applies retroactively without corrupting prior outcomes.
5. **Bulk Re-Scoring Race Condition**: concurrent jobs on same population; idempotent updates and locking.
6. **SoD Bypass Attempt**: user tries to approve own case via API; RBAC + ABAC + audit trail proves block.
7. **Evidence Tamper Detection**: hash mismatch on uploaded PDF triggers quarantine and chain-of-custody review.
8. **Model Rollback**: failed screening model deployment; rollback preserves queue integrity & reprocessing.
9. **Redaction Enforcement**: regulator share-space hides PII per policy while preserving evidentiary value.
10. **Retention Expiry Freeze**: litigation hold overrides deletion job; verify precedence & logging.

---

## 2) Transaction Monitoring & Fraud Detection

### 20 Business Flows
1. **Real-time Payment Screening** (NEFT/RTGS/IMPS/UPI) → rules + ML, block/allow, alert creation.
2. **Velocity Breach Detection** → per-customer/day limits, escalate, step-up authentication.
3. **Geo-Anomaly Check** → impossible travel detection across channels (web, mobile, ATM).
4. **Mule Account Pattern** → inbound bursts, rapid egress; freeze, notify, KYC refresh.
5. **Device Fingerprint Risking** → new device, jailbroken/ rooted signals, challenge or deny.
6. **Merchant Category Risk** → MCC-specific thresholds and watchlists, case routing.
7. **Account Takeover (ATO) Signals** → password reset + payee change + high-value transfer combo.
8. **New Payee Cooling-Off Control** → delayed first transfer, micro-deposits verification.
9. **UPI Collect Request Validation** → phishing pattern detection, report abuse workflow.
10. **Card-Not-Present (CNP) Monitoring** → 3DS outcomes, chargeback correlation, merchant risk.
11. **ATM Skimming Cluster** → hotspot detection via graph analytics, block cards, notify branch ops.
12. **Cross-Channel Correlation** → link alerts across mobile+web+branch for same entity.
13. **SAR/STR Creation from Alerts** → case triage → investigation → regulatory filing.
14. **Auto-Closure on Benign Patterns** → whitelist learned behavior with expiry & review.
15. **Feedback Loop from Chargebacks** → model re-training data pipeline.
16. **False-Positive Review SLA** → measure, escalate breaches, staff forecasting.
17. **High-Risk Beneficiary Screening** → sanctions/negative news on payee accounts.
18. **Cash Deposit Structuring** → threshold layering detection and investigation.
19. **Crypto On/Off Ramp Monitoring** → VASP risk rating, source-of-funds validation.
20. **Disaster Mode** → degraded ruleset activation on core outage; backlog replay later.

### 10 Expert-Level Test Scenarios
1. **Alert Storm Throttle**: 10x spike; ensure queue backpressure, graceful degradation, and no drops.
2. **Model Drift Safeguard**: AUC drop triggers fallback to last-stable model with bannered alerts.
3. **Duplicate Alert Suppression** across channels without losing evidentiary links.
4. **Synthetic Identity Pattern**: multiple accounts share device/IP; graph detection holds transfers.
5. **Edge Timestamp Skews**: terminal vs server clock skews; dedupe & ordering correctness.
6. **Explainability Requirement**: SHAP-like reason codes displayed & exported for each ML alert.
7. **Anomaly Window Mutation**: daylight savings / timezone change changes bins; validate.
8. **Payee Name Mismatch** vs account holder; fuzzy match thresholds & overrides.
9. **Replay Integrity**: historical replay after outage exactly reproduces alerts once.
10. **Human-in-the-Loop Feedback**: analyst dispositions feed training only after QC approval.

---

## 3) Financial Statement Reconciliation

### 20 Business Flows
1. **GL to Subledger Reco** → daily diff, materiality thresholds, certification.
2. **Nostro/Vostro Reco** → bank statements ingest, fee/FX adjustments, break resolution.
3. **Inter-Branch Reco** → mirror entries, suspense clearing workflow.
4. **Payment Gateway Settlement** → acquirer reports vs internal ledgers.
5. **Aging of Breaks** → auto-escalate aged items, root-cause tagging.
6. **Interest Accrual Validation** → product-wise accrual & reversal on closures.
7. **Fee/Charges Reco** → compare configured vs applied charges; refund engine.
8. **EoD/EoM Trial Balance Sign-off** → maker-checker approvals & lock.
9. **Multi-Currency FX Revaluation** → rates feed, reval entries, disclosures.
10. **Card Scheme Billing Reco** → Visa/Mastercard files vs issuing/ acquiring books.
11. **UPI/IMPS Settlement Reco** → NPCI files vs core banking.
12. **Tax Withholding (TDS) Reco** → withheld vs remitted vs reported.
13. **Loan Portfolio Reco** → principal/interest splits, NPA provisioning checks.
14. **Cash Vault Reco** → physical vs system cash, variance approval.
15. **Fixed Assets Reco** → capex additions, depreciation, disposals.
16. **Revenue Recognition Check** → IFRS/Ind-AS compliance for products.
17. **Backdated Entry Handling** → period reopen rules & audit trail.
18. **Blackline/Automation Integration** → tasks sync, controls evidence.
19. **Mass Journal Upload** → CSV import, validation, posting, rollback.
20. **Close Calendar Orchestration** → dependencies, reminders, dashboard.

### 10 Expert-Level Test Scenarios
1. **Rounding & FX Precision** causing pennies-in-rounding breaks across thousands of entries.
2. **Partial Statement Files**: missing last page; system flags and blocks certification.
3. **Cutover Period Lock**: posting after lock creates future-dated entries only.
4. **Duplicate Statement Ingest** handled idempotently with hash checks.
5. **Materiality Rule Change** mid-month preserves historical thresholds for audit.
6. **Dr/Cr Sign Conventions** consistent across sources; mis-signed entries auto-corrected with evidence.
7. **Aged Break Write-off** approval hierarchy with SoD enforcement.
8. **Journal Reversal Chain**: multiple reversals tracked with net effect shown.
9. **Time-Series Integrity**: recalculation reproduces same results deterministically.
10. **Attachment Integrity**: checksum for bank statements; tamper alert on mismatch.

---

## 4) Risk & Controls Assessment

### 20 Business Flows
1. **RCSA Cycle** → risk identification, control mapping, assessment, action plans.
2. **Key Risk Indicators (KRI)** setup, data sourcing, threshold breaches, governance.
3. **Control Testing Program** → sample, test scripts, defects, retest, closure.
4. **Issue Management** → central register, prioritization, remediation tracking.
5. **Scenario Analysis** → stress events, impact modeling, approvals.
6. **Loss Event Capture** → ORX taxonomy, root cause, insurance recovery.
7. **Sox/ICFR Walkthroughs** → process mapping, control design effectiveness sign-off.
8. **Third-Party Risk** → inherent/residual scoring, monitoring cadence.
9. **Risk Appetite & Limits** → board-approved metrics, breaches, escalation.
10. **Change Risk Assessment** → new product/process, pre-implementation assessment.
11. **Model Risk Management** → inventory, validation, performance oversight.
12. **Business Continuity** → BIA, plans, tests, lessons learned.
13. **Data Risk** → classification, lineage, quality controls.
14. **Cyber/Tech Risk Linkage** → feed from VA/PT and SIEM into enterprise risk.
15. **Risk Acceptance** → temporary waivers with expiry and review.
16. **Audit Read-Across** → thematic issues create cross-domain actions.
17. **Board Reporting** → packs generation with narrative and metrics.
18. **Regulatory Queries Handling** → evidence collation, response tracking.
19. **Attestation Workflow** → control owners certify effectiveness quarterly.
20. **Heatmap & Aggregation** → roll-up by BU/region/process with drill-through.

### 10 Expert-Level Test Scenarios
1. **Risk Appetite Re-baselining** mid-year updates do not rewrite historic breaches.
2. **Control Sampling Bias** detection & prevention in automated sampling.
3. **KRIs with Data Gaps** handled via imputation flags and governance.
4. **Loss Events Confidentiality** masking yet allowing aggregate reporting.
5. **Cascading Issues**: one root-cause spawns linked actions across processes.
6. **Model Inventory SoD**: validators cannot approve their own models.
7. **Change Risk Fast-Track** correctly bypasses low-risk with logged rationale.
8. **Heatmap Performance** on 100k+ records stays <2s with caching.
9. **Evidence Retention vs DPDP**: right-to-erasure exceptions documented.
10. **Board Pack Versioning** with watermarks and immutable archive.

---

## 5) Loan & Credit Portfolio Review

### 20 Business Flows
1. **Sample-Based File Review** → borrower docs, covenants, collateral checks.
2. **Automated EWS (Early Warning Signals)** → trigger cases from financial ratios/behaviors.
3. **Credit Approval SoD** → maker-checker & committee minutes capture.
4. **Pricing & Limit Review** → contracted vs system rates/limits.
5. **NPA Classification** → days-past-due checks, provisioning linkage.
6. **Restructuring Cases** → eligibility, approvals, revised schedules.
7. **Collateral Valuation & Revaluation** → panel valuer uploads, variance review.
8. **Covenant Breach Monitoring** → reminders, breach cases, waivers.
9. **Syndicated Loans Sharing** → agent/participant notices and reconciliations.
10. **Retail Scorecard Backtesting** → PD/LGD calibration review.
11. **Fraud in Lending** → doc forensics, income verification, bureau mismatch.
12. **Disbursement Controls** → pre-disbursal checklist, stage-wise release.
13. **Top-Up/Refinance Audits** → eligibility and net exposure view.
14. **Collections Strategy Review** → bucket-wise strategies and outcomes.
15. **Charge-off & Write-back** → approvals, tax impacts, reporting.
16. **Exposure Aggregation** → related-party and group exposure checks.
17. **Portfolio Concentration** → sector/geography caps monitoring.
18. **IFRS/Ind-AS ECL Review** → staging, overlays, disclosures.
19. **KFS (Key Facts Statement) Compliance** → fees/terms transparency.
20. **Customer Grievance Linkage** → complaint patterns tied to underwriting issues.

### 10 Expert-Level Test Scenarios
1. **Backdated NPA Cure** incorrectly flips staging; ensure rules prevent misuse.
2. **ECL Overlay Governance**: manual overlay requires strong approvals & audit trail.
3. **Bureau Hit Latency**: stale bureau data tested against recency SLA.
4. **Collateral Double-Pledge** detection across portfolios.
5. **Committee Minutes Integrity**: edits after sign-off blocked; version control.
6. **Syndication Data Mismatch** auto-reco and exception management.
7. **Batch Repricing** interest recalculation accuracy & customer notice logs.
8. **Restructuring Abuse**: multiple restructures flagged per policy.
9. **Scorecard Drift**: PSI/KS tests trigger recalibration workflow.
10. **Collections Hardship Flags**: regulatory moratorium correctly overrides dunning.

---

## 6) IT Systems & Cybersecurity Audit

### 20 Business Flows
1. **User Access Review** → RBAC recertification, toxic combinations, removals.
2. **Privileged Access Management** → checkout/approval, session recording.
3. **Vulnerability Management** → scan → prioritize → patch → verify.
4. **Penetration Test Intake** → scope, execution evidence, fix validation.
5. **Secure SDLC Audit** → SAST/DAST/SCA gates, waiver tracking.
6. **Change & Release Audit** → CAB approvals, rollback plans, post-implementation review.
7. **Backup & Restore Drill** → RPO/RTO verification with evidence.
8. **BCP/DR Test** → failover, capacity, runbook adherence.
9. **Endpoint Security Posture** → EDR compliance, disk encryption.
10. **Network Segmentation Review** → firewall rules, micro-segmentation attestations.
11. **Cloud Security Posture** → CIS benchmarks, IAM checks, KMS use.
12. **Key Management Audit** → key lifecycle, rotation, dual control.
13. **Logging & SIEM Coverage** → critical systems log & retention checks.
14. **Incident Response** → playbook execution, RCA, lessons learned.
15. **Third-Party Connection Review** → API contracts, least privilege, monitoring.
16. **Data Leakage Prevention** → channel coverage, policy exceptions.
17. **Secure Secrets Handling** → vault usage, no hard-coded secrets.
18. **Certificate Lifecycle** → expiry alerts, auto-rotation, pinning policy.
19. **Container/K8s Controls** → image signing, runtime policies.
20. **Mobile App Security** → jailbreak/root detection, transport security.

### 10 Expert-Level Test Scenarios
1. **Privileged Session Tamper**: hash-verified session recording cannot be altered.
2. **Patch Supersedence**: earlier patches auto-closed on cumulative install with proof.
3. **SIEM Blind Spot**: simulate log source outage; coverage alert & backlog catch-up.
4. **Key Custodian Dual-Control**: two-person rule enforced via workflow & cryptographic proof.
5. **Emergency Change Abuse**: E-Change requires post-facto CAB; missing evidence blocks close.
6. **Vault Outage**: app startup fails safe; secrets never logged; retries exponential.
7. **TLS Cert Near-Expiry**: auto-renew; failure triggers canary & rollback.
8. **K8s Image Drift**: unsigned image blocked at admission controller.
9. **IR Clock Sync**: incident timeline preserved despite NTP drift via monotonic clocks.
10. **Data Residency**: cloud backups remain within approved regions only.

---

## 7) Branch & Operations Audit

### 20 Business Flows
1. **Cash Management Audit** → vault limits, teller balancing, surprise checks.
2. **Account Opening Process** → KYC docs, signatures, welcome kit controls.
3. **Cheque Clearing Controls** → holds, returns, fraud checks.
4. **ATM Replenishment & Reco** → cassette counts, variance logging.
5. **Locker Operations** → access logs, dual control, CCTV alignment.
6. **Remittance Services** → fees, limits, AML checks.
7. **Demand Draft/Banker’s Cheque** issuance & cancellation controls.
8. **Foreign Exchange Counter** → rate application, ID capture, limits.
9. **Cash Deposit Machines (CDM) Ops** → jams, reversals, dispute resolution.
10. **Dormant/Inactive Accounts** → reactivation controls and approvals.
11. **Charge Reversals** → approvals, customer notice, audit trail.
12. **Branch GL Accounts** → suspense/clearing accounts monitoring.
13. **Complaints Handling** → TAT adherence, RCA, customer communication.
14. **Holiday Branch Ops** → staffing, limit overrides, EOD controls.
15. **Courier/Document Dispatch** → POD tracking, tamper-evident packaging.
16. **AML/CTF Onsite Checks** → random sampling of high-risk transactions.
17. **Insurance Cross-Sell** → consent, disclosures, mis-selling checks.
18. **Cash Transit Security** → vendor checks, GPS logs, incident handling.
19. **Business Continuity at Branch** → generator, connectivity, offline kits.
20. **Physical Security** → access control, alarm testing, CCTV retention.

### 10 Expert-Level Test Scenarios
1. **Dual-Control Break**: locker opened without second key; system should hard-block/log alert.
2. **Negative Cash Variance Cover-Up**: forced balancing prevented; exception workflow only.
3. **Cheque Kiting Pattern** detection and escalation.
4. **Backdated Charge Reversal** restricted after EoM lock with approvals.
5. **Dormant Reactivation Fraud**: identity verification with biometric/OTP.
6. **CDM Note Spoilage**: detection logs & customer refund SLA adherence.
7. **Holiday Ops Limits**: temporary limits revert automatically at day end.
8. **Courier Chain-of-Custody**: missing POD triggers investigation workflow.
9. **FX Counter Rate Abuse**: deviation beyond tolerance forces supervisor approval.
10. **CCTV Retention Breach**: retention policy gap triggers compliance escalation.

---

## 8) Regulatory Reporting & Documentation

### 20 Business Flows
1. **Report Catalog & Ownership** → assign owners, frequencies, dependencies.
2. **Data Lineage Capture** → source-to-report mapping with transformations.
3. **Automated Filing** → RBI/central bank e-filing with acknowledgments.
4. **Manual Adjustment Workflow** → maker-checker with narrative & evidence.
5. **Variance Analysis** → period-over-period deltas with drill-down.
6. **Reference Data Governance** → product/GL hierarchies versioning.
7. **XBRL Generation** → validation rules, schema updates.
8. **Late Filing Management** → root cause, regulator comms, penalty tracking.
9. **Restatement Handling** → recall/replace with versioned archive.
10. **Multi-Entity Consolidation** → eliminations and intercompany logic.
11. **Data Quality Rules** → completeness, accuracy, timeliness scoring.
12. **Pre-Filing Attestations** → CFO/Compliance sign-offs.
13. **Secure Regulator Portal Integration** → SSO, MFA, evidence push.
14. **Calendar Orchestration** → dependencies, reminders, holiday handling.
15. **What-If Simulations** for schema changes before go-live.
16. **KPI/MI Packs** → automated narrative sections with data points.
17. **Audit Evidence Binder** → freeze with checksums and retention tags.
18. **Access Controls** → least-privilege and SoD for reporting roles.
19. **Regulatory Query Response** → track Q&A threads, deadlines, artifacts.
20. **Disaster Recovery for Reporting** → secondary path, replay, reconciliation.

### 10 Expert-Level Test Scenarios
1. **Schema Version Mismatch**: new XBRL taxonomy deployed mid-cycle.
2. **Reference Data Drift**: product hierarchy change alters prior period numbers; controlled restatement only.
3. **E2E Timeliness SLA** with time-zone aware cutoffs.
4. **DQ Rule Overrides** require CFO approval with rationale.
5. **Partial Filing Retries** idempotent re-submission without duplicates.
6. **Negative Assurance**: no-data filings handled explicitly with proofs.
7. **Large File Handling**: 1GB+ evidence attachments uploaded reliably with resume.
8. **Regulator Portal Downtime**: store-and-forward with signed payloads.
9. **Immutable Binder**: checksum mismatch blocks export and raises incident.
10. **Calendar Roll**: holiday shifts deadline; alerts and re-plans propagate.

---

## 9) Audit Trail & Evidence Management

### 20 Business Flows
1. **Event Logging Coverage** → define events, ensure capture across services.
2. **Immutable Log Storage** → WORM / append-only with retention.
3. **Chain-of-Custody for Evidence** → hash on upload, movement logs.
4. **e-Sign & Approvals** → compliant digital signatures with timestamps.
5. **Redaction & PII Minimization** → role-based redaction for shares.
6. **Evidence Review Workflow** → annotate, request rework, accept.
7. **Large Artifact Handling** → chunked uploads, virus scanning.
8. **Link Evidence to Case/Control** with verifiable references.
9. **Legal Hold** → suspend deletion with scope and expiry.
10. **Export/Share Securely** → time-bound links, watermarking.
11. **Retention Schedules** per policy and regulation tags.
12. **Disaster Recovery of Vault** → restore test with integrity check.
13. **API Ingestion of Evidence** → system-to-system proofs.
14. **OCR & Searchability** → index content, multilingual support.
15. **Duplicate Detection** → hash-based dedupe with linking.
16. **Access Review** for vault permissions.
17. **Tamper Alerts** → integrity checkers on a schedule.
18. **Evidence Sampling for QC** → percentage-based random pulls.
19. **Bulk Migration** → import legacy archive with mapping.
20. **Audit Trail Reporting** → who, what, when, where dashboards.

### 10 Expert-Level Test Scenarios
1. **Clock Skew on Signatures**: verify monotonic ordering with trusted time source.
2. **Hash Collision Handling**: dedupe links artifacts rather than discarding.
3. **Virus Scan Timeouts**: quarantine with retriable state, not lost.
4. **Redaction Irreversibility**: ensure originals protected; redactions view-limited.
5. **Legal Hold Overrides** blocked even by admins; break-glass with approvals only.
6. **GDPR/DPDP Right-to-Erasure** conflict resolved via lawful basis tagging.
7. **Large Upload Resume** after network drop without rehashing entire file.
8. **e-Sign Key Rotation**: past signatures stay verifiable.
9. **DR Restore Consistency**: point-in-time restore preserves linkage graphs.
10. **Search Privacy**: index terms respect RBAC; no result leakage via snippets.

---

## 10) Dashboard & Analytics for Auditors

### 20 Business Flows
1. **Role-Based Dashboards** → auditor, manager, compliance, exec views.
2. **Drill-Through from KPI to Case** → click-through with full context.
3. **Saved Views & Subscriptions** → scheduled emails/exports.
4. **What-If Filters** → simulate thresholds and see impact.
5. **Anomaly & Trend Detection** → time-series visualizations with alerts.
6. **Cross-Domain Correlation** → join compliance, fraud, and risk datasets.
7. **Near Real-Time Tiles** → streaming alerts panel.
8. **Backlog & SLA Heatmaps** → triage queues and staffing projections.
9. **Self-Service Metrics Builder** → governed semantic layer, templates.
10. **Data Quality Scorecards** → pipeline health & freshness.
11. **Mobile-Friendly Views** → responsive layouts, offline snapshots.
12. **Export Governance** → watermarking, row-level security in exports.
13. **Narrative Insights** → auto-generated text with explainers.
14. **Benchmarking** → branch/region peer comparisons.
15. **KPI Certification** → owner attestation & change logs.
16. **Threshold Management** → propose/approve KPI targets.
17. **Multi-Tenancy / Entity Switcher** → legal entity or region toggle.
18. **Accessibility Compliance** → WCAG checks on visuals.
19. **Ad Hoc Analysis Workspace** → SQL/Notebook with governed access.
20. **Incident & Exception Widgets** → consolidated view with actions.

### 10 Expert-Level Test Scenarios
1. **Row-Level Security (RLS)**: attempts to bypass via export API are blocked & logged.
2. **Drill Path Integrity**: breadcrumbs maintain context across entity/time filters.
3. **Streaming Tile Gaps**: backfill after outage preserves continuity markers.
4. **KPI Definition Versioning**: historical tiles render with period-correct formulas.
5. **Cache Consistency**: refresh shows atomic swap, no mixed-period visuals.
6. **Mobile Offline**: queued subscriptions send once online; no duplicate sends.
7. **Accessibility Edge**: keyboard-only navigation and screen reader alt-texts validated.
8. **Explainability Cards**: reasons for KPI change traceable to upstream data deltas.
9. **Export Watermark Tamper**: altering watermark detectable via embedded checksum.
10. **Semantic Layer Governance**: unauthorized metric creation blocked; request workflow triggered.

---

## Notes for the Bank
- All flows assume **maker-checker**, **RBAC/ABAC**, immutable **audit trails**, and **evidence** capture.
- Non-functional expectations: **performance SLAs**, **availability/DR**, **security**, **privacy**, and **observability**.
- Where ML is referenced, include **model governance**: versioning, monitoring, explainability, bias tests, and rollback.
