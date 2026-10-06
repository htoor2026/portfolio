# Portfolio Website Specification

**Owner:** Harkamal Toor

**Status:** Draft — revised three-page architecture awaiting approval

**Last updated:** 2026-10-06

## 1. Product summary

Create a professional three-page portfolio that presents Harkamal Toor as a strong candidate for Data Scientist, Machine Learning, and AI roles.

Version 1 separates the recruiter's journey into three focused pages:

1. **Home / About** provides a concise human introduction.
2. **Projects** provides technical evidence and project-detail views.
3. **Contact** makes verified contact and professional profiles easy to reach.

The site remains a Python application built with Streamlit and intended for Streamlit Community Cloud. It uses structured local content and local assets, with no custom backend, database, paid service, analytics, or third-party content system.

## 2. Audience and primary journey

### Primary audience

- Recruiters screening candidates for data and AI roles
- Hiring managers and technical interviewers evaluating applied work

### Secondary audience

- Potential collaborators and professional peers

### Primary journey

1. A visitor opens Home and quickly understands who Harkamal is, his professional focus, and his working personality.
2. The visitor opens Projects to scan verified technical work and inspect a selected project's details.
3. The visitor downloads the approved local resume from the bottom of Home.
4. The visitor opens Contact to use a verified email or professional profile.

## 3. Goals

- Give recruiters a clear, human introduction without overwhelming them with technical evidence.
- Keep project metrics and technical depth on the Projects page.
- Make six primary portfolio projects easy to scan while supporting deeper verified case-study content.
- Make contact information and professional profiles immediately understandable.
- Present Streamlit as a simple professional site rather than a dashboard or notebook.
- Keep content updates local, structured, and independent of rendering code.

## 4. Non-goals for version 1

- A single long homepage containing all project evidence
- Project metrics, detailed case studies, charts, or technical result grids on Home
- A blog, newsletter, content management system, or admin area
- A custom contact form or email-sending service
- A custom backend, API, database, authentication, or user account system
- Paid analytics, hosting, fonts, imagery, or SaaS products
- Unnecessary charts, animations, gradients, progress bars, or dashboard widgets
- A JavaScript frontend framework or custom Streamlit component
- Automatically generated or invented portfolio content
- Dark mode, multilingual support, or multiple themes unless later approved

## 5. Functional requirements

- **FR-001 — Home identity:** Home must display an approved professional profile photo with meaningful alt text, Harkamal Toor's name, and a short Data Science / Machine Learning / AI headline.
- **FR-002 — About:** Home must include a concise, verified About Me story that communicates Harkamal's Computer Programming background, Data Science and ML focus, end-to-end problem solving, experimentation, and business decision-making.
- **FR-003 — Project cards:** Projects must display cards for the six primary projects. Each card must support a project name, short verified description, verified technologies, selected verified result or results, detail action, GitHub URL when available, and live deployment URL when available.
- **FR-004 — Experience (deferred):** A standalone experience section is no longer required in version 1. Employment details must not appear outside the approved resume or a future approved requirement unless verified content is supplied.
- **FR-005 — Technical skills:** Home must include a small, scannable technical-skills section. It must not use progress bars or imply proficiency levels that were not supplied.
- **FR-006 — Education (deferred):** A standalone education section is no longer required in version 1. Verified education may inform the About story or remain in the approved resume.
- **FR-007 — Resume:** The bottom of Home must provide a clearly labeled button that downloads a local, current, approved PDF. The button must not appear when the approved file is unavailable.
- **FR-008 — Contact:** Contact must show public email, LinkedIn, GitHub, and X. Missing values must remain clear development placeholders and must not become fabricated links. No contact form is permitted.
- **FR-009 — Navigation:** The app must provide minimal top navigation between Home, Projects, and Contact using supported Streamlit navigation. All navigation and actions must work with keyboard input.
- **FR-010 — Responsive presentation:** All three pages and project-detail states must remain usable on mobile, tablet, laptop, and wide desktop viewports.
- **FR-011 — Page identity:** Each top-level page must have a clear page title and heading. Shared Streamlit configuration must provide the approved browser title, favicon, and light theme.
- **FR-012 — Honest incomplete-content behavior:** Missing facts, assets, technologies, results, decisions, lessons, or URLs must be omitted from publishable UI or remain unmistakable development placeholders. Nothing may be inferred or fabricated.
- **FR-013 — Project results:** Verified results and metrics may appear only on Projects cards or project-detail views. Home must not display project metrics.
- **FR-014 — Three-page structure:** Version 1 must have exactly three top-level pages in this order: Home, Projects, Contact.
- **FR-015 — Project-detail view:** The Projects page must support a detail state for each project with fields for Problem, Approach, Technologies, Results, Business/technical decision, What was learned, GitHub, and Live Demo. Empty fields must not be invented.
- **FR-016 — Personality:** Home must display these approved personality keywords: Creative, Analytical, Builder-minded, Clear Communicator, Persistent, and Diplomatic.
- **FR-017 — Primary project set:** The Projects page must support these projects: Flight Pulse; A/B Testing & Personalization; Toronto Climate Analysis; Customer Churn Prediction; Retail / Recommendation Intelligence; and End-to-End ML System.

## 6. Non-functional requirements

- **NFR-001 — Technology and hosting:** The implementation must use Python and Streamlit and remain deployable on Streamlit Community Cloud.
- **NFR-002 — Cost:** The production site must operate without paid services. New services require explicit approval and must not be necessary for version 1.
- **NFR-003 — Accessibility:** The site must target WCAG 2.2 AA within Streamlit's platform constraints, including logical reading order, keyboard access, visible focus, sufficient contrast, descriptive links, and meaningful image alternatives.
- **NFR-004 — Performance and local assets:** The profile photo, resume, styles, and other owned assets must be stored locally and appropriately sized. The app must avoid unnecessary dependencies, remote asset requests, and expensive rendering work.
- **NFR-005 — Professional visual quality:** The site must use a restrained light theme, deliberate typography, spacing, content width, and hierarchy. It must not use gradients, skill progress bars, unnecessary animation, dense widgets, or default dashboard-style composition.
- **NFR-006 — Privacy:** Version 1 must add no analytics, behavioral tracking, fingerprinting, or visitor-submitted data collection.
- **NFR-007 — Security:** No secrets or private data may be committed or rendered. Only approved public contact details, links, documents, and images may ship.
- **NFR-008 — Maintainability:** All portfolio facts and page copy must remain in `portfolio_data.py`; page modules must primarily handle presentation and navigation.
- **NFR-009 — Compatibility:** The deployed app must complete its primary journey in current stable versions of Chrome, Safari, Firefox, and Edge.
- **NFR-010 — Content integrity:** Every public claim, technology, date, metric, credential, image, document, and external URL must be supplied or approved by Harkamal before release.
- **NFR-011 — Simple architecture:** Version 1 must have no custom backend, database, API layer, frontend framework, or runtime dependency beyond what is required to render the Streamlit portfolio.
- **NFR-012 — Charts:** Charts are prohibited on Home and Contact. A chart may appear in a project-detail view only when it is part of verified project evidence and improves understanding.

## 7. Page content contracts

### Page 1 — Home / About

Home contains, in this order:

1. Professional profile photo
2. Name and short professional headline
3. Concise About Me story
4. Six approved personality keywords
5. Small technical-skills section
6. Local resume download at the bottom

Home must remain visually minimal and must not show project metrics.

### Page 2 — Projects

Projects contains cards for all six primary projects. Each card and detail view may show only supplied information.

Each project record supports:

- Name
- Short description
- Technologies
- Selected results
- Problem
- Approach
- Business or technical decision
- What was learned
- GitHub URL
- Live Demo URL

Project detail is a state within the Projects page, not a fourth top-level navigation page.

### Page 3 — Contact

Contact contains:

- Public email — currently missing
- LinkedIn — `https://www.linkedin.com/in/harkamal-s/`
- GitHub — `https://github.com/htoor2026`
- X — `https://x.com/HarryToor01`

Contact must not contain a form or collect visitor data.

## 8. Content contract

Implementation may use unmistakable local placeholders, but public deployment is blocked until required publishable content is supplied and verified.

### Required Home content

- Approved local profile image and alt text
- Approved short headline
- Approved About Me story
- Approved technical-skill subset
- Current approved local resume PDF

### Required Projects content

- Six project names
- Verified short descriptions
- Verified technologies
- Verified selected results where available
- Verified detail fields where available
- Approved GitHub and live-demo URLs where available

### Required Contact content

- Public email address
- Verified LinkedIn, GitHub, and X URLs

Unknown content must never be guessed. Quantitative metrics require a supplied source; qualitative claims must also be approved.

## 9. Information architecture

The top navigation order is:

1. Home
2. Projects
3. Contact

`app.py` acts as the shared Streamlit router and frame. Project-detail views remain within Projects so no additional top-level page is introduced.

## 10. Acceptance criteria

- **AC-001 — Home clarity:** At 375 px and 1440 px viewport widths, Home clearly presents the approved photo, name, headline, concise About story, personality, compact skills, and resume action without project metrics or horizontal overflow. Covers `FR-001`, `FR-002`, `FR-005`, `FR-007`, `FR-010`, `FR-013`, `FR-016`.
- **AC-002 — Three-page content path:** Home, Projects, and Contact appear in the approved order and each contains only its assigned content. Covers `FR-003`, `FR-008`, `FR-014`, `FR-017`.
- **AC-003 — Keyboard use:** A keyboard-only reviewer can reach and activate top navigation, project-detail actions, external links, and resume download in a logical order with visible focus and no keyboard trap. Covers `FR-009`, `NFR-003`.
- **AC-004 — Responsive review:** All pages and detail states have no unintended horizontal overflow, clipped text, or obscured action at 320 px, 375 px, 768 px, 1024 px, and 1440 px widths. Covers `FR-010`.
- **AC-005 — Automated checks:** Dependency integrity, Python compilation, imports, Streamlit AppTest coverage for all three pages, and headless local startup all pass. Covers `NFR-001`, `NFR-008`, `NFR-011`.
- **AC-006 — Page identity:** Each top-level page has the approved navigation label, heading, browser identity, favicon, and light theme. Covers `FR-011`.
- **AC-007 — Accessibility review:** Automated inspection reports no critical or serious issue introduced by custom markup or styling, and manual review confirms reading order, text alternatives, contrast, keyboard use, and focus visibility. Covers `NFR-003`.
- **AC-008 — Professional presentation:** Desktop and mobile review confirms a minimal professional site with no dashboard appearance, gradients, progress bars, unnecessary animation, or unapproved charts. Covers `NFR-005`, `NFR-012`.
- **AC-009 — Privacy and network review:** Browser storage, cookies attributable to the app, and production network activity show no added analytics, tracking, form collection, or unapproved third-party asset request. Covers `NFR-002`, `NFR-004`, `NFR-006`.
- **AC-010 — Content and link audit:** Human review confirms every claim and project field against supplied material, every published external link reaches its intended destination, and no publishable page contains a fabricated or broken value. Covers `FR-012`, `NFR-007`, `NFR-010`.
- **AC-011 — Browser smoke test:** The deployed app completes its primary journey in current stable Chrome, Safari, Firefox, and Edge. Covers `NFR-009`.
- **AC-012 — Community Cloud deployment:** Streamlit Community Cloud can install the declared dependencies, start `app.py`, load all local assets, and expose the approved public URL without a paid service. Covers `NFR-001`, `NFR-002`, `NFR-004`.
- **AC-013 — Resume download:** The Home resume button downloads the approved local PDF and does not expose a missing, stale, or remote placeholder file. Covers `FR-007`, `NFR-004`, `NFR-010`.
- **AC-014 — Project details:** Each project card can open its matching detail state; populated fields match verified data and missing fields are not fabricated. Covers `FR-003`, `FR-012`, `FR-015`, `FR-017`.

## 11. Architecture decisions and assumptions

- **D-001:** Version 1 uses Python and Streamlit.
- **D-002:** Version 1 targets Streamlit Community Cloud.
- **D-003:** Owned images, the resume, and styles remain local.
- **D-004:** Version 1 has no custom backend, database, paid service, or analytics.
- **D-005:** Version 1 has exactly three top-level pages: Home, Projects, and Contact.
- **D-006:** `app.py` uses supported Streamlit top navigation and acts as the shared router.
- **D-007:** Project details render inside the Projects page rather than as additional top-level pages.
- **A-001:** English is the only language in version 1.
- **A-002:** Contact uses public links rather than a form.
- **A-003:** The site uses system fonts and local assets instead of remote runtime assets.
- **A-004:** A plain Python module remains the simplest structured content source.
- **A-005:** The initial public URL may use a Streamlit Community Cloud subdomain.
- **A-006:** Missing project-detail fields remain absent or visibly marked during development and are not release-ready content.

## 12. Approval gate

This revision supersedes the approved single-page information architecture. Do not refactor application code until Harkamal explicitly approves this revised specification and the matching revised plan. Deployment remains separately blocked until all release acceptance criteria pass and Harkamal explicitly authorizes it.
