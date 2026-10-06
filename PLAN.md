# Portfolio Website Development Plan

**Status:** Approved

**Depends on:** `SPEC.md`

**Last updated:** 2026-10-06

## 1. Delivery strategy

Build version 1 as one small Streamlit application: a single rendering entry point, one structured Python content module, local assets, and minimal styling needed to create a professional portfolio presentation. There is no custom backend, database, API, JavaScript application, or paid service.

Work proceeds through explicit approval and verification gates. A phase is complete only when its checks pass and its required content decisions are resolved.

## 2. Proposed project structure

```text
portfolio/
├── AGENTS.md                    # Repository working agreement
├── SPEC.md                      # Product requirements and acceptance criteria
├── PLAN.md                      # Sequenced delivery plan
├── app.py                       # Streamlit page composition and rendering
├── portfolio_data.py            # Structured, verified portfolio content
├── requirements.txt             # Minimal pinned runtime dependencies
├── .streamlit/
│   └── config.toml              # Streamlit theme and safe UI configuration
└── assets/
    ├── styles.css               # Focused portfolio styling
    ├── images/                  # Optimized owned images
    └── resume.pdf               # Added only after approval
```

The default content format is a plain Python module because it requires no parser, schema library, or duplicate model layer. JSON remains an allowed substitution before implementation if Harkamal prefers to edit JSON directly.

Only create files that the approved implementation needs. Do not add a component framework, data layer, utility package, build system, or test framework for static portfolio rendering.

## 3. Phases

### Phase 0 — Approve scope and gather source content

**Requirements:** all requirements; especially `FR-012`, `FR-014`, `NFR-010`

**Files:** `AGENTS.md`, `SPEC.md`, `PLAN.md`

Tasks:

1. Specification and plan review completed.
2. Harkamal approved the specification and plan on 2026-10-06.
3. `AGENTS.md` reconciled with the approved Streamlit architecture.
4. Supply the content listed in the `SPEC.md` content contract.
5. Identify which assets and URLs are approved for public use.
6. Decide the primary call to action and whether version 1 includes a portrait.

Gate:

- Specification and plan approval recorded.
- Implementation may proceed one approved phase at a time.
- Missing content and assets have named owners or are intentionally omitted from release.

### Phase 1 — Bootstrap the minimal Streamlit app

**Requirements:** `NFR-001`, `NFR-002`, `NFR-008`, `NFR-011`

**Expected scope:** `app.py`, `portfolio_data.py`, `requirements.txt`, `.streamlit/config.toml`

Tasks:

1. Select and document a Python version supported by Streamlit Community Cloud.
2. Declare only the Streamlit runtime dependency, pinned to a compatible version.
3. Create the smallest launchable `app.py` and separate structured content module.
4. Configure the page title, favicon, layout, and base theme.
5. Confirm local headless startup and dependency integrity.

Gate:

```bash
python -m pip check
python -m compileall app.py portfolio_data.py
streamlit run app.py --server.headless true
```

The first two commands must exit successfully, and the Streamlit command must start the app without an uncaught exception before Phase 2.

### Phase 2 — Establish verified content, assets, and visual system

**Requirements:** `FR-001`–`FR-008`, `FR-012`, `FR-013`, `NFR-003`–`NFR-005`, `NFR-008`, `NFR-010`

**Expected scope:** `portfolio_data.py`, `.streamlit/config.toml`, `assets/styles.css`, approved files under `assets/`

Tasks:

1. Define only the Python dictionaries and lists required by the approved content.
2. Enter supplied facts and make development-only placeholders unmistakable.
3. Prepare and optimize approved images; add the resume only after its public version is approved.
4. Establish a restrained palette, typography scale, spacing system, content width, cards, links, buttons, and focus treatment.
5. Use Streamlit's supported theme configuration first, then a small local stylesheet for portfolio-specific presentation.
6. Avoid brittle styling that depends on generated CSS class names when a stable Streamlit or semantic selector is available.

Gate:

- Every entered claim has a supplied source.
- No unlicensed, private, or remotely hosted asset is present.
- Text and controls meet WCAG AA contrast targets.
- Content changes can be made in `portfolio_data.py` without restructuring rendering code.

### Phase 3 — Build the ordered portfolio page

**Requirements:** `FR-001`–`FR-014`, `NFR-003`–`NFR-005`, `NFR-008`, `NFR-011`

**Expected scope:** `app.py`, with content read from `portfolio_data.py`

Tasks:

1. Render the Hero section with positioning and a primary action.
2. Render Featured Projects as concise, visually consistent case-study cards.
3. Render Project Results / Impact as a separate evidence-focused section.
4. Render Skills, About, Education / Experience, Resume, and Contact in the approved order.
5. Add compact section navigation only if it remains reliable and visually appropriate in Streamlit.
6. Use Streamlit columns and containers carefully so content stacks cleanly on narrow screens.
7. Keep the sidebar unused and avoid dashboard widgets, debug output, charts, or interactivity with no portfolio purpose.

Gate:

- `AC-001` through `AC-005` pass.
- All eight required sections appear in the approved order.
- The primary journey works with keyboard input.
- There is no unintended horizontal overflow at the specified widths.

### Phase 4 — Quality, accessibility, and content audit

**Requirements:** `FR-010`–`FR-014`, `NFR-003`–`NFR-010`

**Expected scope:** focused corrections to `app.py`, content, configuration, and local assets

Tasks:

1. Review desktop and mobile screenshots for hierarchy, spacing, consistency, and a non-dashboard appearance.
2. Audit keyboard use, focus, contrast, reading order, link text, and image alternatives.
3. Inspect image sizing, browser console output, local asset loading, storage, cookies, and network requests.
4. Review every claim, date, metric, resume file, and URL with Harkamal.
5. Test the primary journey in current Chrome, Safari, Firefox, and Edge.
6. Re-run syntax, dependency, and headless-start checks.

Gate:

- `AC-006` through `AC-011` pass.
- No placeholder text, broken link, missing asset, or uncaught exception remains.
- Harkamal approves the final content and visual presentation for deployment.

### Phase 5 — Streamlit Community Cloud release

**Requirements:** `NFR-001`, `NFR-002`, `NFR-004`, `NFR-006`, `NFR-007`, `AC-012`

**Expected scope:** deployment configuration and any verified deployment-only correction

Tasks:

1. Confirm the repository contains the correct entry point and minimal dependency declaration.
2. Connect the approved repository and branch to Streamlit Community Cloud.
3. Configure the supported Python version without adding secrets.
4. Deploy and verify all local images, styles, links, and resume behavior at the public URL.
5. Repeat the responsive, accessibility, privacy, and browser smoke checks on the hosted app.
6. Obtain explicit release approval and record the final URL in the project documentation.

Gate:

- `AC-001` through `AC-012` pass or have an explicitly accepted exception.
- The deployment uses no paid service and requires no secret.
- Harkamal explicitly approves the public release.

## 4. Verification matrix

- **Python integrity:** successful dependency check, syntax compilation, and Streamlit headless startup.
- **Content separation:** page copy and project records come from the dedicated structured content module.
- **Content accuracy:** human audit against supplied resume, project, education, and employment sources.
- **Visual quality:** desktop and mobile review confirms a cohesive portfolio rather than a default Streamlit dashboard.
- **Accessibility:** automated inspection plus keyboard, focus, reading-order, contrast, and text-alternative review.
- **Responsive layout:** manual review at 320, 375, 768, 1024, and 1440 px.
- **Privacy:** browser storage, cookie, and network inspection confirms no added tracking or data collection.
- **Links and assets:** manual link, download, and local-asset review on the deployed app.
- **Compatibility:** primary-journey smoke test in current Chrome, Safari, Firefox, and Edge.

## 5. Risks and controls

- **Default Streamlit appearance:** The result could look like a dashboard or notebook. Control: custom theme, restrained local CSS, no sidebar, clear content hierarchy, and visual acceptance review.
- **Brittle CSS overrides:** Streamlit internals may change. Control: prefer theme configuration and stable or semantic selectors; keep overrides small and verify after dependency upgrades.
- **Community Cloud cold starts:** Free hosting may sleep inactive apps. Control: avoid heavy dependencies and startup work, keep assets small, and accept platform cold-start behavior for version 1.
- **Limited SEO and metadata control:** Streamlit does not offer the same document control as a static site framework. Control: configure supported page identity and accept this tradeoff for the simpler first release.
- **Unverified or thin content:** Visual design cannot replace evidence. Control: finish the content contract early and omit unsupported claims.
- **Unavailable project metrics:** Invented numbers would damage trust. Control: use accurate qualitative outcomes when approved quantitative measures do not exist.
- **Asset licensing or privacy issues:** Control: use only owned or explicitly licensed local assets and review the repository before deployment.

## 6. Deferred work

The following require a new approved requirement and demonstrated value: a custom backend, database, API, contact form, analytics, live model demos, interactive dashboards, project-detail pages, blog/CMS, authentication, advanced animation, theme switching, internationalization, a custom frontend, and paid or alternative hosting.

## 7. Current authorization

Phase 1 implementation is authorized. Later phases require separate approval. Verified content may be collected in parallel; public deployment remains blocked until the content audit passes and Harkamal explicitly authorizes deployment.
