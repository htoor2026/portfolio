# Portfolio Website Development Plan

**Status:** Draft — revised three-page plan awaiting approval

**Depends on:** `SPEC.md`

**Last updated:** 2026-10-06

## 1. Delivery strategy

Refactor the existing single-page Streamlit portfolio into three focused top-level pages without changing the platform, adding dependencies, or discarding verified content.

`app.py` becomes a small shared router using Streamlit's supported top navigation. Home, Projects, and Contact become separate view modules. `portfolio_data.py` remains the only source of portfolio facts and page copy. Project detail is rendered as a selected state inside Projects so the product retains exactly three top-level pages.

No implementation or deployment begins until this revised specification and plan are explicitly approved.

## 2. Proposed project structure

```text
portfolio/
├── AGENTS.md                    # Repository working agreement
├── SPEC.md                      # Revised product requirements
├── PLAN.md                      # Revised delivery plan
├── app.py                       # Shared config, CSS loading, and top navigation
├── portfolio_data.py            # All verified content and placeholders
├── requirements.txt             # Streamlit only unless approved otherwise
├── views/
│   ├── home.py                  # Home / About presentation
│   ├── projects.py              # Project gallery and in-page detail state
│   └── contact.py               # Contact/profile presentation
├── .streamlit/
│   └── config.toml              # Light theme and safe UI configuration
└── assets/
    ├── styles.css               # Shared minimal responsive styling
    ├── images/
    │   └── profile.jpg          # Approved local profile image
    └── resume.pdf               # Approved local downloadable resume
```

Use `st.navigation(..., position="top")` with explicit `st.Page` definitions. Do not use the automatic sidebar-oriented `pages/` convention or introduce a custom navigation dependency.

Only add a helper module if implementation proves that meaningful logic would otherwise be duplicated across all three views.

## 3. Migration constraints

- Preserve all currently verified facts, metrics, personality keywords, education, and URLs in `portfolio_data.py`.
- Move project cards, metrics, and detailed evidence off Home and into Projects.
- Do not promote existing development placeholders into published content.
- Do not invent technologies or detail fields while adapting the project schema.
- Keep the existing Streamlit dependency unless an approved requirement proves it insufficient.
- Do not deploy or perform Streamlit Community Cloud actions during the refactor.

## 4. Phases

### Revision Phase 0 — Approve the new architecture

**Requirements:** all revised requirements; especially `FR-014`, `D-005`, `D-006`, `D-007`

**Files:** `AGENTS.md`, `SPEC.md`, `PLAN.md`

Tasks:

1. Review the three-page product change and deferred single-page requirements.
2. Confirm that project details remain inside Projects rather than creating a fourth top-level page.
3. Confirm that Home contains no project metrics.
4. Explicitly approve the revised specification and plan.

Gate:

- Harkamal explicitly approves `SPEC.md` and `PLAN.md` after this revision.
- No application refactor starts before that approval.

### Revision Phase 1 — Introduce the three-page shell

**Requirements:** `FR-009`, `FR-011`, `FR-014`, `NFR-001`, `NFR-008`, `NFR-011`

**Expected scope:** `app.py`, `views/home.py`, `views/projects.py`, `views/contact.py`, shared configuration

Tasks:

1. Reduce `app.py` to shared page configuration, local CSS loading, and top navigation.
2. Define Home, Projects, and Contact with explicit `st.Page` objects.
3. Use `st.navigation` with top positioning and run the selected page.
4. Create the three minimal view modules without adding product content outside `portfolio_data.py`.
5. Confirm direct page navigation and headless startup.

Gate:

```bash
python -m pip check
python -m compileall app.py portfolio_data.py views
streamlit run app.py --server.headless true
```

- All three pages load without an uncaught exception.
- Navigation order is Home, Projects, Contact.
- No sidebar navigation or new dependency is introduced.

### Revision Phase 2 — Build Home / About

**Requirements:** `FR-001`, `FR-002`, `FR-005`, `FR-007`, `FR-013`, `FR-016`, `NFR-003`–`NFR-005`, `NFR-008`, `NFR-010`

**Expected scope:** `views/home.py`, the Home portion of `portfolio_data.py`, approved profile image and resume, focused shared CSS

Tasks:

1. Present the approved local profile image, name, and short headline.
2. Add a concise About Me story using only approved content.
3. Display the six approved personality keywords.
4. Display a compact technical-skills list without progress bars.
5. Add the local approved resume download at the bottom.
6. Verify the user-added profile PNG and resume PDF, then map or normalize them to the approved asset paths without changing their content.
7. Remove all project cards, metrics, result grids, and technical-detail content from Home.
8. Keep Home visually minimal and responsive.

Gate:

- `AC-001`, `AC-003`, `AC-004`, `AC-007`, `AC-008`, and `AC-013` pass for Home.
- The profile image has approved alt text.
- The resume action downloads the approved local PDF.
- Home contains no project metric.

### Revision Phase 3 — Build Projects and project details

**Requirements:** `FR-003`, `FR-012`, `FR-013`, `FR-015`, `FR-017`, `NFR-003`–`NFR-005`, `NFR-008`, `NFR-010`, `NFR-012`

**Expected scope:** `views/projects.py`, the project portion of `portfolio_data.py`, focused shared CSS

Tasks:

1. Normalize the six existing project records around the approved optional fields.
2. Render concise responsive cards for all six projects.
3. Show only verified technologies, results, GitHub URLs, and live-demo URLs.
4. Implement a project-detail state within Projects with a clear return path to the gallery.
5. Render Problem, Approach, Technologies, Results, Decision, What was learned, GitHub, and Live Demo only when verified values exist.
6. Keep charts out unless an approved project detail contains a verified chart that materially improves understanding.

Gate:

- `AC-002`, `AC-003`, `AC-004`, `AC-007`, `AC-008`, `AC-010`, and `AC-014` pass for Projects.
- Every displayed fact traces to supplied content.
- Missing fields do not produce fabricated copy, empty controls, or broken links.

### Revision Phase 4 — Build Contact and complete cross-page QA

**Requirements:** `FR-008`–`FR-012`, `FR-014`, `NFR-002`–`NFR-010`

**Expected scope:** `views/contact.py`, contact data, shared CSS, focused corrections across pages

Tasks:

1. Render verified LinkedIn, GitHub, and X links.
2. Keep email as a clear development placeholder until supplied; omit it from release if still unavailable.
3. Confirm no form, backend, database, analytics, or visitor-data collection exists.
4. Verify all three pages and project-detail states at responsive widths.
5. Audit keyboard use, focus, contrast, reading order, links, image alternatives, local assets, console output, and network requests.
6. Run syntax, import, dependency, AppTest, and local HTTP checks.

Gate:

- `AC-002` through `AC-011` pass.
- All external links resolve to their intended destinations or are omitted.
- No publishable placeholder, missing required asset, secret, or uncaught exception remains.
- Harkamal approves the final content and visual presentation before deployment work.

### Revision Phase 5 — Streamlit Community Cloud release

**Requirements:** `NFR-001`, `NFR-002`, `NFR-004`, `NFR-006`, `NFR-007`, `AC-012`

**Expected scope:** deployment configuration and verified deployment-only corrections

Tasks:

1. Confirm `app.py` is the correct entry point and dependencies are minimal.
2. Obtain explicit deployment approval.
3. Connect the approved repository and branch to Streamlit Community Cloud.
4. Configure the supported Python version without adding secrets.
5. Deploy and repeat responsive, accessibility, privacy, asset, download, link, and browser checks.
6. Record the final approved public URL.

Gate:

- All acceptance criteria pass or have an explicitly accepted exception.
- The deployment uses no paid service and requires no secret.
- Harkamal explicitly approves the public release.

## 5. Verification matrix

- **Page architecture:** Home, Projects, and Contact exist in the approved navigation order.
- **Home separation:** no project metrics, result grids, or detailed case studies appear on Home.
- **Project detail:** every project card opens its matching detail state and provides a return path.
- **Content separation:** all factual content and copy come from `portfolio_data.py`.
- **Content accuracy:** human audit against supplied resume, project, education, and profile sources.
- **Python integrity:** successful dependency check, compilation, imports, AppTest, and headless startup.
- **Visual quality:** desktop and mobile review confirms a minimal professional site rather than a dashboard.
- **Accessibility:** automated inspection plus keyboard, focus, reading-order, contrast, and text-alternative review.
- **Responsive layout:** manual review at 320, 375, 768, 1024, and 1440 px.
- **Privacy:** browser storage, cookie, and network inspection confirms no added tracking or data collection.
- **Links and assets:** manual link, local-image, and resume-download review.
- **Compatibility:** primary-journey smoke test in current Chrome, Safari, Firefox, and Edge.

## 6. Known migration conflicts

- The current `app.py` renders one large HTML document and custom anchor navigation; it must become a shared router.
- The current `portfolio_data.py` is organized around eight single-page sections; it must be reorganized by Home, Projects, Contact, and optional project-detail fields without losing verified data.
- Project cards, result metrics, skills, About, education, resume, and contact currently share one page; each must move to its approved destination.
- The current Home includes project evidence, which is prohibited by the revised Home contract.
- The current CSS assumes long-page anchors and section spacing; it must be simplified and made safe across three independent views.
- Existing AppTest assertions target a single rendered document and must become page-aware.
- Candidate profile and resume assets now exist under noncanonical filenames in `assets/images/`; implementation must verify them and map or normalize them to the approved profile and resume paths.
- Several project-detail fields remain unverified, so complete detail views cannot be populated without new source content.
- The public email remains missing.
- The supplied Flight Pulse live-demo URL currently redirects to Streamlit authentication and is not release-ready as a public demo.

## 7. Risks and controls

- **Navigation looks like application chrome:** Control: use Streamlit's supported top navigation, keep labels to three, and avoid sidebar controls.
- **Home regains technical clutter:** Control: prohibit project metrics and detailed project cards on Home.
- **Incomplete project detail:** Control: conditionally render only verified fields and keep missing content out of release UI.
- **Brittle CSS:** Control: prefer Streamlit configuration and stable semantic selectors; keep overrides small.
- **Community Cloud cold starts:** Control: retain one runtime dependency and avoid startup computation.
- **Limited SEO and metadata control:** Control: configure supported page identity and accept the platform tradeoff for version 1.
- **Asset or content integrity:** Control: require approved local files and human review before release.

## 8. Deferred work

The following require a new approved requirement and demonstrated value: custom backend, database, API, contact form, analytics, live inference, general-purpose dashboards, blog/CMS, authentication, advanced animation, gradients, theme switching, internationalization, a custom frontend, and paid or alternative hosting.

## 9. Next decision

Harkamal should review and explicitly approve the revised `SPEC.md` and `PLAN.md`. After approval, implementation begins with Revision Phase 1. Deployment remains separately unauthorized.
