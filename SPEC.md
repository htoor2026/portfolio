# Portfolio Website Specification

**Owner:** Harkamal Toor

**Status:** Approved

**Last updated:** 2026-10-06

## 1. Product summary

Create a professional personal portfolio that presents Harkamal Toor as a strong candidate for Data Scientist, Machine Learning, and AI roles. The site should let a recruiter quickly understand his focus, assess evidence of his work, review relevant experience, and contact him.

Version 1 is a single-page Python application built with Streamlit and deployed on Streamlit Community Cloud. It uses local static assets and structured local content, with no custom backend, database, paid service, or third-party content system.

Although Streamlit is the delivery framework, the finished site must read visually as a polished professional portfolio rather than a default analytics dashboard.

## 2. Audience and primary journey

### Primary audience

- Recruiters screening candidates for data and AI roles
- Hiring managers and technical interviewers evaluating applied work

### Secondary audience

- Potential collaborators and professional peers

### Primary journey

1. A visitor lands on the page and immediately sees Harkamal's name, target roles, and concise value proposition.
2. The visitor scans featured projects and a dedicated results section for relevant, credible evidence.
3. The visitor reviews skills, background, education, and experience.
4. The visitor downloads an approved resume or follows a verified contact or professional link.

## 3. Goals

- Communicate professional positioning within the first viewport.
- Make two to four strong, relevant projects easy to evaluate.
- Give project results and impact more prominence than a technology inventory.
- Present Streamlit with a deliberate portfolio visual system rather than its default dashboard appearance.
- Provide reliable resume and contact actions.
- Keep content updates simple and local, with no paid or operational infrastructure.

## 4. Non-goals for version 1

- A blog, newsletter, content management system, or project-detail routes
- A custom backend, API, database, authentication, or admin area
- A custom contact form or email-sending service
- Paid analytics, hosting, fonts, imagery, or SaaS products
- Live model inference, data pipelines, dashboards, or interactive data applications
- Complex animation, 3D content, or a JavaScript frontend framework
- Automatically generated or invented portfolio content
- Dark mode, multilingual support, or multiple themes unless later approved

## 5. Functional requirements

- **FR-001 — Hero:** The first viewport must display Harkamal Toor's name, target discipline, a short evidence-based value proposition, and one primary call to action.
- **FR-002 — About:** The site must include a concise professional summary covering specialization, working style, and the kinds of problems Harkamal solves.
- **FR-003 — Featured projects:** The site must present two to four verified projects. Each project must identify its problem or goal, Harkamal's contribution, approach, tools, and only those links intended to be public.
- **FR-004 — Experience:** The site must present relevant experience in reverse chronological order with role, organization, dates, and outcome-oriented highlights.
- **FR-005 — Skills:** The site must group verified capabilities into a small number of meaningful categories such as machine learning, data, engineering, and tools. Prominent skills should be supported by project or experience evidence.
- **FR-006 — Education and credentials:** The site must display verified relevant education and optional credentials when supplied.
- **FR-007 — Resume:** The site must provide a clearly labeled download or external resume action only when a current, approved public resume is available.
- **FR-008 — Contact:** The site must offer verified ways to contact or learn more about Harkamal, such as email, LinkedIn, and GitHub. A submission form is not required.
- **FR-009 — Navigation:** Visitors must be able to understand and reach every major section through a clear page flow and, where reliable in Streamlit, compact section navigation. All actions must work with keyboard input.
- **FR-010 — Responsive presentation:** All required content and actions must remain usable on mobile, tablet, laptop, and wide desktop viewports.
- **FR-011 — Page identity:** The Streamlit page configuration must provide an approved page title, favicon, and wide or centered layout choice. Additional metadata is limited to what Streamlit Community Cloud reliably supports without a separate frontend.
- **FR-012 — Honest incomplete-content behavior:** Missing facts, assets, or URLs must be omitted from the published interface rather than replaced with fabricated or broken content.
- **FR-013 — Project results and impact:** A dedicated section must summarize verified project outcomes, metrics, or qualitative impact separately from the project descriptions. It must not invent quantitative results when none are available.
- **FR-014 — Section order:** The page must present sections in this order: Hero, Featured Projects, Project Results / Impact, Skills, About, Education / Experience, Resume, and Contact.

## 6. Non-functional requirements

- **NFR-001 — Technology and hosting:** The implementation must use Python and Streamlit and must be deployable on Streamlit Community Cloud.
- **NFR-002 — Cost:** The production site must operate without paid services. New services require explicit approval and must not be necessary for the initial release.
- **NFR-003 — Accessibility:** The site must target WCAG 2.2 AA within Streamlit's platform constraints, including logical reading order, keyboard access, visible focus, sufficient contrast, descriptive link text, and meaningful image alternatives.
- **NFR-004 — Performance and assets:** Images, the resume, styles, and other owned assets must be stored locally in the repository and appropriately sized. The app must avoid unnecessary dependencies, remote asset requests, and expensive computation during page rendering.
- **NFR-005 — Professional visual quality:** The site must use a cohesive custom theme, deliberate typography, spacing, color, content width, and project presentation. Default Streamlit dashboard patterns such as an unnecessary sidebar, exposed debug output, dense widget layouts, or chart-first composition must not dominate the experience.
- **NFR-006 — Privacy:** The initial release must add no analytics, behavioral tracking, fingerprinting, or visitor-submitted data collection.
- **NFR-007 — Security:** No secrets or private data may be committed to the repository or rendered in the app. Only approved public contact details and assets may ship.
- **NFR-008 — Maintainability:** Portfolio content must be separate from rendering code and editable in one structured Python or JSON file. Version 1 should use a plain Python content module unless approved content reveals a need for JSON.
- **NFR-009 — Compatibility:** The deployed app must complete its primary journey in current stable versions of Chrome, Safari, Firefox, and Edge.
- **NFR-010 — Content integrity:** Every public claim, date, metric, credential, image, document, and external URL must be supplied or approved by Harkamal before release.
- **NFR-011 — Simple architecture:** Version 1 must have no custom backend service, database, API layer, frontend framework, or runtime dependency beyond what is required to render the Streamlit portfolio.

## 7. Content contract

Implementation may begin with clearly marked local draft content, but public deployment is blocked until the following are supplied and verified:

- Professional headline and short biography
- Primary call to action
- Location or work-authorization statement, if Harkamal wants it public
- Preferred public email address
- LinkedIn, GitHub, and any other approved profile URLs
- Current resume PDF or approved external resume URL
- Employment history with exact titles, organizations, dates, and highlights
- Education and approved credentials
- Two to four projects with role, problem, approach, technology, result or impact, links, and approved visuals
- Headshot or portrait choice, if one will be used
- Final Streamlit Community Cloud URL

Unknown content must remain visibly marked in local development and must never be guessed. Quantitative project metrics require a verifiable source; otherwise, use accurate qualitative outcomes.

## 8. Information architecture

The initial release is one page in this exact order:

1. Hero
2. Featured Projects
3. Project Results / Impact
4. Skills
5. About
6. Education / Experience
7. Resume
8. Contact

A compact header or navigation treatment may be included if it works reliably without making the page resemble a Streamlit control panel.

## 9. Acceptance criteria

- **AC-001 — First-view clarity:** At 375 px and 1440 px viewport widths, the first viewport shows Harkamal's name, target discipline, positioning statement, and primary action without overlap or unintended horizontal scrolling. Covers `FR-001`, `FR-010`.
- **AC-002 — Complete ordered content path:** Every supplied and approved section appears in the order defined by `FR-014`; unavailable optional content is omitted cleanly. Covers `FR-002` through `FR-008`, `FR-012` through `FR-014`, and `NFR-010`.
- **AC-003 — Keyboard use:** A keyboard-only reviewer can reach and activate every link, download, and navigation control in a logical order, can see focus, and encounters no keyboard trap. Covers `FR-009`, `NFR-003`.
- **AC-004 — Responsive review:** The page has no unintended horizontal overflow, clipped text, or obscured action at 320 px, 375 px, 768 px, 1024 px, and 1440 px widths. Covers `FR-010`.
- **AC-005 — Automated checks:** The documented Python syntax check and dependency integrity check both exit successfully from a clean checkout, and the Streamlit app starts in headless mode without an uncaught exception. Covers `NFR-001`, `NFR-008`, `NFR-011`.
- **AC-006 — Page identity:** The deployed app shows the approved browser title, favicon, and layout configuration. Covers `FR-011`.
- **AC-007 — Accessibility review:** Automated inspection reports no critical or serious issues introduced by custom markup or styling, and manual review confirms reading order, text alternatives, contrast, keyboard use, and focus visibility. Covers `NFR-003`.
- **AC-008 — Professional presentation:** A desktop and mobile visual review confirms a cohesive portfolio aesthetic, clear hierarchy, restrained Streamlit chrome, readable project cards, and no default dashboard or notebook-like presentation. Covers `NFR-005`.
- **AC-009 — Privacy and network review:** Browser storage, cookies attributable to the app, and the production network log show no added analytics, tracking, form-data collection, or unapproved third-party asset requests. Covers `NFR-002`, `NFR-004`, `NFR-006`.
- **AC-010 — Content and link audit:** A human review confirms every factual claim against supplied source material, every public link resolves to its intended destination, the resume is current, and no placeholder or broken asset remains. Covers `FR-012`, `NFR-007`, `NFR-010`.
- **AC-011 — Browser smoke test:** The deployed app completes its primary journey in current stable versions of Chrome, Safari, Firefox, and Edge. Covers `NFR-009`.
- **AC-012 — Community Cloud deployment:** Streamlit Community Cloud can install the declared dependencies, start the app from the documented entry point, load local assets, and expose the approved public URL without a paid service. Covers `NFR-001`, `NFR-002`, `NFR-004`.

## 10. Approved architecture decisions and remaining assumptions

- **D-001:** Version 1 uses Python and Streamlit.
- **D-002:** Version 1 deploys to Streamlit Community Cloud.
- **D-003:** All owned assets are stored locally in the repository.
- **D-004:** Version 1 has no custom backend, database, or paid service.
- **A-001:** The first release is a single-page portfolio.
- **A-002:** English is the only language in the first release.
- **A-003:** Contact uses public links such as `mailto:`, LinkedIn, and GitHub rather than a form.
- **A-004:** The site uses system fonts and local assets to avoid external runtime asset requests.
- **A-005:** The site launches without analytics.
- **A-006:** Two to four strong projects are more useful than a long project archive.
- **A-007:** A plain Python module is the simplest structured content source for version 1; JSON remains acceptable if the final content workflow favors it.
- **A-008:** The initial public URL may use the Streamlit Community Cloud subdomain; a custom domain is outside version 1 unless separately approved.

## 11. Approval status

Harkamal approved this specification on 2026-10-06. Implementation may proceed according to the approved plan. Public deployment remains blocked by `AC-010` and requires separate explicit approval.
