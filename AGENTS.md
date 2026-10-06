# AGENTS.md

## Project

This repository contains the professional portfolio of **Harkamal Toor**, aimed at recruiters and hiring managers for Data Scientist, Machine Learning, and AI roles.

The version 1 platform remains:

- Python
- Streamlit
- Streamlit Community Cloud as the eventual deployment target
- Structured local content
- Local static assets
- Free services only

Do not introduce Next.js, TypeScript, Tailwind CSS, React, another JavaScript framework, a custom backend, an API layer, a database, analytics, or a paid service.

## Current phase

The product architecture is being revised from one long page to three top-level pages. `SPEC.md` and `PLAN.md` are drafts awaiting explicit approval after this revision.

Do not modify application code to implement the three-page design until the user approves both revised documents. The existing single-page implementation is superseded design work, not the new source of product truth.

Do not deploy, connect the repository to Streamlit Community Cloud, change cloud settings, or perform any other cloud action without separate explicit approval.

## Sources of truth

Use this precedence when instructions conflict:

1. The user's current request
2. Approved requirements in `SPEC.md`
3. The active phase and verification gates in `PLAN.md`
4. This file
5. Existing implementation conventions

Do not silently resolve a material conflict. Report it and request direction when the sources above do not establish a clear answer.

## Content integrity

Never invent or embellish:

- Project descriptions, problems, approaches, results, impact, decisions, or lessons
- Technologies, methods, datasets, responsibilities, or proficiency levels
- Employers, roles, dates, education, or credentials
- Email addresses, profile links, repositories, demos, or other URLs
- Resume content, images, testimonials, awards, or metrics

Use only content supplied or approved by Harkamal. Missing optional content must be omitted from release UI. Development placeholders must be unmistakable and must not reach deployment.

Keep every portfolio fact and page-copy value in `portfolio_data.py`. Page modules primarily handle presentation, navigation, and conditional rendering.

## Three-page product contract

Version 1 has exactly three top-level pages in this order:

1. Home
2. Projects
3. Contact

Use supported Streamlit top navigation. Do not create a sidebar navigation experience or a fourth top-level page for project details.

### Home

Home is a visually minimal human introduction. It contains, in order:

1. Approved professional profile photo
2. Harkamal Toor's name and short Data Science / ML / AI headline
3. Concise About Me story
4. Personality keywords: Creative, Analytical, Builder-minded, Clear Communicator, Persistent, Diplomatic
5. Small technical-skills section
6. Approved local resume download at the bottom

Home must not contain project metrics, detailed case studies, result grids, charts, or dashboard widgets.

### Projects

Projects presents technical evidence for:

1. Flight Pulse
2. A/B Testing & Personalization
3. Toronto Climate Analysis
4. Customer Churn Prediction
5. Retail / Recommendation Intelligence
6. End-to-End ML System

Each project card supports only verified name, short description, technologies, selected results, GitHub URL, and live-demo URL. Project detail remains a state inside Projects and supports Problem, Approach, Technologies, Results, Business/technical decision, What was learned, GitHub, and Live Demo.

Conditionally omit missing project fields. Never fill gaps with plausible text.

### Contact

Contact contains verified public email, LinkedIn, GitHub, and X. Email remains a development placeholder until supplied. Do not add a form, backend, scheduling widget, or data collection.

## Proposed architecture

After revised-plan approval, use this structure:

```text
portfolio/
├── AGENTS.md
├── SPEC.md
├── PLAN.md
├── app.py
├── portfolio_data.py
├── requirements.txt
├── views/
│   ├── home.py
│   ├── projects.py
│   └── contact.py
├── .streamlit/
│   └── config.toml
└── assets/
    ├── styles.css
    ├── images/
    │   └── profile.jpg
    └── resume.pdf
```

- `app.py` owns shared page configuration, local CSS loading, and `st.navigation` with `position="top"`.
- `views/home.py` renders Home / About.
- `views/projects.py` renders the project gallery and selected project-detail state.
- `views/contact.py` renders verified contact methods and profiles.
- `portfolio_data.py` remains the single source for structured portfolio content.
- `.streamlit/config.toml` contains the light theme and safe Streamlit configuration.
- `assets/styles.css` contains minimal shared responsive styling.
- `assets/images/profile.jpg` and `assets/resume.pdf` must be approved local files before release.

Do not add a shared helper module unless implementation proves it prevents meaningful duplication across all three views. Do not add a component framework, CMS, state library, build system, test framework, or data layer without an approved requirement.

## Streamlit implementation rules

- Use `st.Page` and `st.navigation(..., position="top")` for the three top-level pages.
- Use supported Streamlit APIs and Python standard-library features first.
- Keep Streamlit as the only direct runtime dependency unless an approved requirement proves another package necessary.
- Pin runtime dependencies for reproducible Community Cloud builds.
- Keep project-detail selection inside Projects using the smallest supported state or query mechanism.
- Do not add JavaScript components, embedded remote applications, or frontend frameworks.
- Do not add a custom server, endpoint, database, authentication, or secret-dependent feature.
- Keep the profile image, resume, CSS, and other owned assets local.
- Prefer Streamlit theme configuration before CSS overrides.
- Keep CSS small and avoid selectors tied to generated class names when stable alternatives exist.
- Avoid unnecessary computation, remote asset requests, and large dependencies.

## Visual design

The result must look like a simple professional portfolio, not a Streamlit dashboard or notebook.

- Use a light theme, restrained palette, clear typography, generous spacing, and narrow readable content widths.
- Keep navigation minimal and visible without relying on a sidebar.
- Do not use gradients.
- Do not use skill progress bars or invented proficiency levels.
- Do not use unnecessary animation.
- Do not use charts on Home or Contact.
- Use a chart in project detail only when it is verified project evidence and materially improves understanding.
- Avoid dense widgets, debug output, controls without a portfolio purpose, and remote decorative assets.

## Responsive and accessible behavior

- Preserve logical heading, reading, and keyboard order on every page and detail state.
- Use descriptive links, meaningful image alternatives, sufficient contrast, and visible focus.
- Do not rely on color alone to communicate meaning.
- Ensure navigation, project-detail actions, downloads, and external links are keyboard operable and clearly labeled.
- Design cards and columns to stack cleanly on narrow screens.
- Check for clipped text, obscured actions, and horizontal overflow at 320, 375, 768, 1024, and 1440 px widths.
- Target WCAG 2.2 AA within Streamlit's platform constraints.

Accessibility basics must not be removed to simplify styling.

## Implementation workflow

For each approved phase or bounded change:

1. Confirm the relevant `FR-*`, `NFR-*`, and `AC-*` requirements in `SPEC.md`.
2. Inspect the files in scope and current Git diff.
3. Preserve verified content before restructuring data or presentation.
4. Make the smallest complete change that satisfies the active phase.
5. Run applicable validation after every significant change.
6. Review responsive behavior, accessibility, page boundaries, visual quality, and content accuracy when affected.
7. Report what changed, what was validated, and every unresolved content dependency or conflict.

Do not proceed past an approval gate on the user's behalf.

## Validation

Once the revised modules exist, baseline checks are:

```bash
python -m pip check
python -m compileall app.py portfolio_data.py views
streamlit run app.py --server.headless true
```

The dependency and compilation checks must exit successfully. The Streamlit app must start without an uncaught exception and be stopped after a smoke test unless the user asks to keep it running.

After significant changes, also verify:

- Top navigation order is Home, Projects, Contact.
- All three pages load directly and through navigation.
- Home contains no project metrics or detailed project evidence.
- All six project cards exist and detail actions map to the correct records.
- Project detail renders only populated, verified fields.
- Contact includes only verified public values; there is no form.
- Portfolio facts and copy come from `portfolio_data.py`.
- The profile image, CSS, external links, and resume download work.
- Mobile and desktop layouts remain usable.
- Keyboard navigation, focus, contrast, headings, and image alternatives remain accessible.
- No fabricated content, release placeholder, broken link, debug output, analytics, or unapproved remote request is present.

Never claim a check passed unless it was actually run.

## Deployment boundary

Streamlit Community Cloud is the only approved version 1 deployment target, but deployment is always a separate user-authorized action.

Without explicit deployment approval, do not:

- Connect or authorize a Git provider or Streamlit account
- Create, update, restart, share, or delete a cloud app
- Change Community Cloud settings, secrets, domains, or access controls
- Publish a preview or production URL

Local development and validation do not authorize cloud activity.

## Git and safety

- Preserve user changes and keep unrelated edits out of the current task.
- Never commit secrets, `.env` files, private contact data, or unlicensed assets.
- Do not add deployment credentials to the repository.
- Do not rewrite Git history or delete user content without explicit permission.
- Keep commits focused by implementation phase when the user asks for commits.
