# Software Requirements Specification (SRS)

## QuickConnect — Volunteer Emergency Matching Platform

| Document field | Value            |
| -------------- | ---------------- |
| Status         | Draft for review |
| Version        | 0.6              |
| Date           | 6 November 2026  |
| Product        | QuickConnect     |

## 1. Introduction

### 1.1 Purpose

This document defines the initial software requirements for QuickConnect, a platform that helps authorized coordinators connect available volunteers with nearby emergency incidents. Matching considers incident priority, volunteer skills, location, availability, and capacity. This draft is intended to support product, design, engineering, and operational planning; it is not a dispatch or emergency-response protocol.

### 1.2 Product scope

QuickConnect provides a platform to:

- Register volunteers and record their skills, service area, availability, and contact preferences.
- Lets users create emergency requests.
- Let authorized users manage emergency requests.
- Identify suitable volunteers using eligibility, skill, distance, availability, and incident priority.
- Notify candidates and track responses and assignment status.
- Give coordinators an auditable view of incidents, volunteers, assignments, and outcomes.

QuickConnect supplements the responsible emergency service or coordinating organization. It does not replace emergency services, determine whether a person needs emergency care, certify a volunteer's competence, or guarantee that a volunteer will arrive or resolve an incident.

### 1.3 Intended users

| User                 | Description                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| Volunteer            | Creates a profile, sets availability, receives requests, and accepts or declines them.                |
| Incident reporter    | Submits an incident for review.                                                                       |
| Coordinator          | Verifies and prioritizes incidents, reviews matches, assigns volunteers, and monitors progress.       |
| System administrator | Maintains the service, manages organization membership, access controls, and technical configuration. |

### 1.4 Definitions

- **Incident / emergency request:** A record describing a need for assistance, its location, priority, required skills, and status.
- **Candidate:** A volunteer who passes the configured eligibility checks for an incident.
- **Assignment:** A coordinator-approved or policy-authorized link between a volunteer and an incident.
- **Priority:** An operational urgency level set or confirmed by an authorized person or configured trusted source.
- **Matching radius:** A configured distance limit for considering volunteers for an incident.
- **Organization:** A participating group responsible for volunteers, incident review, and response procedures.

## 2. Overall description

### 2.1 Product perspective

QuickConnect is an automated emergency volunteer matching and assignment platform that identifies and ranks suitable volunteers based on incident priority, assistance requirements, volunteer skills, availability, and geographical proximity. It provides coordinators with ranked volunteer recommendations, enabling them to review and approve assignments before the system notifies selected volunteers and tracks their responses and progress.

### 2.2 Operating environment

The initial product shall support modern desktop and mobile web browsers for volunteers, public incident reporting, and coordinator workflows. Volunteer location updates use browser geolocation while the volunteer is on duty and the browser page is active with permission granted. Browsers may suspend or stop updates when backgrounded, the device is locked, or the browser closes; the system shall indicate stale location and exclude stale volunteers from new matching. Native mobile apps and guaranteed background tracking are out of scope for V1. Offline operation, integrations with emergency-service systems, and supported geographic regions are otherwise not specified for the initial version.

### 2.3 Constraints and dependencies

- Access to precise location, notifications, and personal data depends on user consent and device or platform permissions.
- Browser geolocation requires explicit browser permission and an active page. Browser and operating-system suspension behavior may delay or stop updates; the client shall show when updates are unavailable or stale.
- A location or notification provider may be unavailable, inaccurate, or delayed.
- Volunteer suitability depends on the accuracy and freshness of profile data and any verification performed by an organization.
- The initial release shall support only one predefined organization. Organization registration, creation, selection, and multi-organization management are outside the scope of V1.

### 2.4 Assumptions

1. Authentication uses server-side sessions with secure cookies.
2. An authorized coordinator is responsible for validating incidents and setting or confirming priority.
3. Volunteers explicitly opt into being available for matching. While available, and after granting required browser location permission, the service updates their location at the configured on-duty frequency while the browser page is active. Switching availability off stops location tracking and future location collection.
4. The initial matching result is a recommendation. A candidate volunteer confirms the assignment.
5. The participating organization defines the skill taxonomy, service area, verification process, response procedures, and escalation contacts.
6. The platform will display a clear instruction to contact local emergency services for immediate danger or life-threatening situations.

## 3. System features and functional requirements

Requirements use “shall” to indicate a mandatory capability. Priority labels: **Must** for the initial usable release; **Should** for a valuable follow-up; **Could** for optional scope.

### 3.1 Accounts, roles, and profiles

- **FR-001 (Must):** The system shall allow a user to create an account and authenticate using server-side sessions identified by secure cookies.
- **FR-002 (Must):** The system shall support role-based permissions for volunteers, coordinators, and System administrators.
- **FR-003 (Must):** The system shall allow volunteers to maintain their name, contact method, skills, availability, and accessibility or response constraints relevant to assignments.
- **FR-004 (Must):** The system shall let volunteers switch availability on or off and pause or withdraw from receiving requests. Switching availability on shall require the volunteer's browser location permission and start location updates for matching. Switching availability off shall immediately stop location tracking and future location collection.
- **FR-007 (Must):** The system shall show volunteers when location tracking is active, explain that it is used to match them to nearby incidents, provide a control to stop tracking by switching availability off, and show when the browser has suspended updates or location has become stale.
- **FR-008 (Must):** While a volunteer is available and the browser page is active, the system shall target the location update cadence defined in the location policy table. The system shall record location capture time and receipt time and exclude a volunteer from new matching when the latest location exceeds the configured freshness limit.

#### 3.1.1 Location update cadence

| Volunteer state | Target update frequency |
|---|---|
| Off duty | No tracking |
| On duty, stationary | Every 2–5 minutes |
| On duty, moving | Every 30 seconds |
| On duty, rapid movement | Every 10–15 seconds |
| Assignment accepted / En Route | Every 10–15 seconds |
| Assignment completed | Stop assignment-specific tracking; if still on duty, resume the applicable on-duty cadence |

These are target frequencies while the browser page is active. Browser or operating-system suspension may delay or stop updates; the client shall show this state and the backend shall use the actual location timestamp for freshness checks.
- **FR-005 (Must):** The system shall record whether a volunteer's skills or identity have been verified, by whom, and when; unverified claims shall be distinguishable from verified credentials.
- **FR-006 (Should):** The system should let the administrator manage the skills, credential requirements, and verification states used in the single organization's volunteer pool.

### 3.2 Incident intake and management

- **FR-010 (Must):** The system shall provide a publicly accessible emergency request submission form that allows any individual to report an emergency by providing its description, location, assistance requirements, contact details, and other relevant information.
- **FR-011 (Must):** The system shall maintain submitted emergency requests in a pending review state until an authorized coordinator verifies and approves or rejects them.
- **FR-012 (Must):** The system shall allow authorized coordinators to review submitted requests, validate their details, determine their priority, modify relevant information, and approve or reject them.
- **FR-013 (Must):** The system shall initiate volunteer matching only for verified and approved emergency requests.
- **FR-014 (Must):** The system shall support incident statuses: Submitted, Under Review, Open for Matching, Assigned, In Progress, Resolved, Cancelled, and Unable to Staff.
- **FR-015 (Must):** The system shall restrict incident approval, priority changes, cancellation, and status transitions according to configured roles.
- **FR-016 (Must):** The system shall require a location suitable for matching, or clearly mark the incident as not matchable until a suitable location is available.
- **FR-017 (Must):** The system shall allow coordinators to correct incident details and retain a record of material changes.
- **FR-018 (Should):** The system should support intake from an approved external system, with source and validation status recorded.

### ### 3.3 Matching and Recommendation

- **FR-020 (Must):** The system shall exclude volunteers who are inactive, unavailable, opted out of requests, have no sufficiently fresh location, are outside the configured matching radius, exceeding their assignment capacity, or missing mandatory skills or required verified credentials.
- **FR-021 (Must):** The system shall rank eligible candidates using a deterministic lexicographical ranking policy based on verified skill suitability, geographical distance, current assignment workload, and time elapsed since their last assignment.
- **FR-022 (Must):** The system shall make candidate ranking factors, eligibility results, and exclusion reasons visible to authorized coordinators.
- **FR-023 (Must):** The system shall apply a consistent tie-breaking mechanism using a stable volunteer identifier when candidates have identical ranking results.
- **FR-024 (Must):** The system shall allow an authorized coordinator to review, modify, and approve the recommended candidate list before assignment.
- **FR-025 (Must):** The system shall re-evaluate eligible candidates when incident requirements, priority, location, or volunteer availability changes.
- **FR-026 (Should):** The system should support configurable matching radius, maximum concurrent assignments, and organization-defined eligibility rules.
- **FR-027 (Must):** The system shall not represent a ranking or assignment recommendation as a guarantee of volunteer safety, competence, arrival time, or successful outcome.

#### 3.3.1 Initial Matching Policy (V1)

QuickConnect shall implement a deterministic, rule-based volunteer matching mechanism consisting of two stages: eligibility filtering and candidate ranking.

**Stage 1 – Eligibility Filtering**

The system shall identify volunteers who satisfy all mandatory eligibility conditions for an incident. Volunteers shall be excluded if they:

1. Have inactive accounts.
2. Are currently unavailable or have opted out of receiving requests.
3. Are located outside the configured matching radius.
4. Do not possess all mandatory skills required for the incident.
5. Do not possess the required verified credentials, where applicable.
6. Have reached their maximum permitted concurrent assignment capacity.

Only volunteers who satisfy all mandatory eligibility conditions shall proceed to the candidate-ranking stage.

**Stage 2 – Candidate Ranking**

Eligible volunteers shall be ranked using a lexicographical ranking policy. The system shall compare candidates using the following order, moving to the next criterion only when candidates are tied on the preceding criterion:

1. **Verified Skill Suitability:** Volunteers with higher verified proficiency in required skills and greater coverage of additional relevant skills shall receive higher rankings.
2. **Geographical Distance:** Volunteers located closer to the incident shall receive higher rankings. The system shall calculate geographical distance using a consistent distance calculation method.
3. **Current Assignment Workload:** Volunteers with fewer active assignments shall receive higher rankings to distribute workload.
4. **Assignment History:** Volunteers who have gone longer without receiving an assignment shall receive higher rankings to promote fair distribution of assignments.
5. **Stable Tie-Breaker:** If candidates remain tied after all preceding comparisons, the system shall use a stable volunteer identifier to determine their final order.

**Incident Processing Priority**

The system shall process approved incidents according to their assigned priority levels:

- Critical – Immediate assistance required.
- High – Urgent assistance required.
- Medium – Assistance required soon.
- Low – Non-urgent assistance.

Incidents with higher priority shall be processed before those with lower priority. Within the same priority level, older incidents shall receive precedence.

Incident priority shall determine the order in which incidents are processed and shall not directly influence the ranking of volunteers within an individual incident.

**Stage 3 – Coordinator Review and Assignment Approval**

The system shall present the ranked candidate list to an authorized coordinator for review. The coordinator shall be able to inspect candidate details, ranking factors, eligibility results, and exclusion reasons.

The coordinator shall have the authority to select, deselect, or modify the recommended candidate list and approve the final selection before assignment offers are issued.

Following approval:

1. The system shall notify the selected volunteers with relevant incident information.
2. Volunteers shall be able to accept or decline the assignment offers.
3. The system shall record volunteer responses and response timestamps.
4. Accepted offers shall be confirmed as assignments.
5. Declined or expired offers shall trigger a reassessment of available candidates and notify the coordinator for further action.
6. The coordinator shall be able to intervene, select alternative candidates, or reassign volunteers when necessary.

#### 3.3.2 Matching Policy Configuration

The initial release shall use centrally maintained configuration values for matching parameters. These shall include:

- **Matching Radius:** Maximum geographical distance within which volunteers are considered eligible for an incident.
- **Maximum Concurrent Assignments:** Maximum number of active assignments a volunteer can handle simultaneously.
- **Location Freshness:** Maximum permitted age of volunteer location data for matching purposes.
- **Skill Requirements:** Mandatory and additional relevant skills associated with an incident.
- **Credential Requirements:** Verification requirements for skills or qualifications where applicable.

The matching parameters and ranking policy shall be applied consistently across the single organization supported in V1.

### 3.4 Notifications, acceptance, and assignment

- **FR-028 (Must):** The system shall notify selected volunteers with the minimum information needed to decide whether to respond, subject to the organization's privacy policy.
- **FR-029 (Must):** The system shall allow a volunteer to accept or decline a request and shall record the response time.
- **FR-030 (Must):** The system shall support a configurable response deadline and mark unanswered offers as expired.
- **FR-031 (Must):** The system shall notify the coordinator of acceptance, decline, expiry, delivery failure where available, and assignment changes.
- **FR-032 (Must):** The system shall prevent conflicting assignments when configured capacity limits would be exceeded.
- **FR-033 (Must):** The system shall let coordinators assign, reassign, or remove volunteers and record the actor, time, and reason.
- **FR-034 (Should):** The system should support staged notification waves, allowing the coordinator to widen the candidate set if the first group does not respond.
- **FR-035 (Must):** The system shall provide a visible fallback when no eligible volunteers are available, including escalation to the coordinator's configured process.

### 3.5 Status tracking and communication

- **FR-036 (Must):** The system shall let assigned volunteers report En Route, Arrived, Unable to Help, and Completed, where those states are enabled by the organization.
- **FR-037 (Must):** The system shall show coordinators a current incident and assignment status with the time of the latest update.
- **FR-038 (Should):** The system should provide a controlled communication channel for incident-specific coordination without exposing personal contact details by default.
- **FR-039 (Must):** The system shall allow an authorized user to close or cancel an incident and notify assigned volunteers of relevant changes.

### 3.6 Audit and administration

- **FR-040 (Must):** The system shall maintain an audit trail for authentication-sensitive actions, incident changes, priority changes, matching recommendations, offers, responses, assignments, and administrative changes.
- **FR-041 (Must):** The system shall record the matching policy version and input data used for each recommendation so that a decision can be reviewed later.
- **FR-042 (Must):** The system shall allow organization administrators to manage members, roles, service areas, and approved operational settings.
- **FR-043 (Should):** The system should provide operational reports on response times, coverage, unfilled incidents, and volunteer workload, with access limited to authorized roles.

## 4. External interface requirements

### 4.1 User interface

- The interface shall clearly distinguish incidents awaiting review from incidents open for matching and assignments.
- The interface shall display priority, location, required skills, and status in a form usable on small screens.
- The interface shall provide clear feedback for offer expiry, no available candidates, notification failure, and loss of location permission.
- The interface shall use the visual palette defined in the Software Design document for brand, actions, alerts, and incident priority. Priority and status shall also be identified by text or icons; color alone shall not convey meaning.
- The volunteer web experience shall be designed mobile-first, beginning with narrow-screen layouts and adapting to larger screens. Availability and tracking state, offers, and assignment actions shall be easy to find and operate on a phone-sized viewport without horizontal scrolling.
- Public incident intake and coordinator workflows shall use responsive layouts suitable for both mobile and desktop browsers.
- Interfaces shall be designed for keyboard operation, screen readers, readable contrast, and localization. A target accessibility standard and languages remain to be selected.

### 4.2 Software interfaces

Potential integrations include an identity provider, geocoding/map service, push notifications, SMS/email provider, and organization intake systems. Specific providers, protocols, data contracts, and failure behavior must be defined during architecture and integration design.

### 4.3 Communications

All client-server communication shall use encrypted transport. Notification content shall avoid unnecessary sensitive incident details and shall direct users to authenticate for protected information.

## 5. Nonfunctional requirements

- **NFR-001 Security:** The system shall enforce least-privilege access and protect account credentials and sensitive data using current security practices. Browser authentication shall use server-side sessions in Secure, HttpOnly, SameSite cookies and protect state-changing requests against CSRF.
- **NFR-002 Privacy:** The system shall collect only data needed for matching and coordination, explain location use, and provide controls for consent, access, correction, and deletion subject to applicable retention obligations.
- **NFR-003 Location:** The system shall identify the source and freshness of a location where practical, and shall not imply that an approximate or stale location is exact. Location tracking shall only be active while the volunteer has opted into availability, granted browser permission, and the browser page is active. A volunteer with stale location shall not be included in new matches.
- **NFR-004 Availability:** Service availability targets and maintenance windows shall be agreed before launch. The product shall communicate when live coordination data may be stale or unavailable.
- **NFR-005 Performance:** Under the agreed launch workload, incident creation and candidate recommendations should complete within a target to be set during design; the service shall expose failures rather than silently returning incomplete matches.
- **NFR-006 Scalability:** The system shall support growth in participating organizations, volunteers, and concurrent incidents without changing organization data boundaries.
- **NFR-007 Auditability:** Audit events shall be time-stamped, access-controlled, and retained according to an approved retention policy.
- **NFR-008 Reliability:** The system shall handle unavailable map or notification providers gracefully and show the coordinator which steps require manual follow-up.
- **NFR-009 Usability:** A coordinator shall be able to review an incident, understand the recommended candidates and rationale, and make an assignment without needing to infer hidden ranking rules.
- **NFR-010 Organization scope:** V1 shall operate for one predefined organization. Users shall not be able to select, create, or switch organizations.

## 6. Data requirements

Core entities are User, the deployment-configured Organization, VolunteerProfile, Skill, Credential/Verification, AvailabilitySession, Incident, Location, MatchRecommendation, Offer, Assignment, StatusUpdate, Notification, and AuditEvent. V1 has no tenant selection or cross-organization sharing. Data retention and deletion behavior must be specified before production use.

Sensitive data may include personal contact information, precise location, incident descriptions, and credential evidence. Access shall be limited by role and organizational need. The system should avoid storing health or other highly sensitive incident details unless required and approved by the operating organization.

## 7. Safety, privacy, and misuse considerations

- The platform shall display that immediate threats and life-threatening emergencies should be directed to local emergency services.
- A coordinator-controlled review step is the default for incident validity, priority, and final assignment.
- Volunteers shall see enough information to make an informed decision, while private details are withheld until needed and authorized.
- The product shall not imply that a background check, profile skill, or platform match is a guarantee of suitability.
- The participating organization must define procedures for safeguarding, incident escalation, volunteer conduct, and reports of unsafe behavior.
- Location tracking shall only occur while the volunteer is available and has granted device permission. Switching availability off shall stop tracking and future collection; stored location shall not be used for new matching after the volunteer becomes unavailable. The system shall provide a clear tracking indicator and controls, and retain location only under an approved retention policy.

## 8. Acceptance criteria for an initial release

The initial release is acceptable when:

1. A volunteer can create and update a profile, switch availability on or off, see when location tracking is active, and stop tracking by switching availability off.
2. An authorized coordinator can create, review, prioritize, update, and close an incident.
3. The system filters out ineligible volunteers and ranks candidates using configured skill and distance rules.
4. A coordinator can inspect why candidates were included or excluded and approve an assignment.
5. A volunteer can accept or decline an offer, and the coordinator can see the response and current status.
6. The system handles no-candidate, expired-offer, and notification-failure cases with a visible follow-up path.
7. Role restrictions, audit records, location permission and availability behavior, and single-organization data boundaries work as specified.
8. The immediate-emergency guidance and limitations of matching are visible in relevant user flows.

## 9. Out of scope for this draft

- Medical triage, diagnosis, or autonomous assessment of emergency severity.
- Emergency-service dispatch or guaranteed responder arrival.
- Automated background checks or credential issuance.
- Payments, volunteer compensation, and donations.
- Public social networking, volunteer ratings, or punitive performance scoring.
- Offline-first operation and a native mobile application.

## 10. Open questions

1. Which country, regions, and languages are in the first deployment, and which privacy/accessibility obligations apply?
2. Who can submit incidents, and which trusted source confirms their validity and priority?
3. Should matching produce recommendations only, or can a coordinator-approved policy automatically assign volunteers?
4. How should priority levels be defined, and should priority order incidents, candidates within one incident, or both?
5. What counts as a skill match: exact required skills, equivalent skills, proficiency levels, or verified credentials only?
6. What location precision, matching radius, travel mode, and location freshness should the system use?
7. Which notification channels are required, and what response deadline/escalation sequence is appropriate?
8. How many concurrent requests may a volunteer accept, and how are volunteer workload and fatigue handled?
9. What data retention and deletion periods apply to location, incident, communication, and audit data?
10. What uptime, response-time, peak-volume, and recovery targets should be committed to?
11. Which external systems and map/notification providers must be supported?
12. What verification, safeguarding, incident reporting, and coordinator training processes will participating organizations provide?

## 11. Revision history

| Version | Date            | Changes                                                                                                                       |
| ------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 0.1     | 1 November 2026 | Initial requirements draft based on the project description; assumptions and open questions identified.                      |
| 0.2     | 6 November 2026 | Defined single-organization V1 and availability-controlled location tracking.                                                  |
| 0.3     | 6 November 2026 | Set browser-only support, secure cookie sessions, and active-page location behavior.                                           |
| 0.4     | 6 November 2026 | Added state-based location update cadence and configured server-side cookie sessions as an explicit requirement.                |
| 0.5     | 6 November 2026 | Added the agreed UI palette and requirement to pair color with labels or icons.                                                   |
| 0.6     | 6 November 2026 | Made the volunteer web experience explicitly mobile-first.                                                                          |
