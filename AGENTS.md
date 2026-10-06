# AGENTS.md

## Project

This repository contains the personal portfolio of **Harkamal Toor**, aimed at recruiters and hiring managers for Data Scientist, Machine Learning, and AI roles.

The approved version 1 architecture is:

- Python
- Streamlit
- Streamlit Community Cloud deployment
- Local static assets
- Free services only

Do not introduce Next.js, TypeScript, Tailwind CSS, React, another JavaScript framework, a custom backend, an API layer, or a database.

## Current phase

`SPEC.md` and `PLAN.md` were approved by the user on 2026-10-06. The repository is ready for Phase 1 implementation when the user requests it.

Do not deploy, connect the repository to Streamlit Community Cloud, change cloud settings, or perform any other cloud action without explicit user approval.

When requirements change, update `SPEC.md` first and keep existing requirement IDs stable. Update `PLAN.md` when a change affects scope, sequencing, architecture, or verification.

## Sources of truth

Use this precedence when instructions conflict:

1. The user's current request
2. Approved requirements in `SPEC.md`
3. The active phase and verification gates in `PLAN.md`
4. This file
5. Existing implementation conventions

Do not silently resolve a material conflict. Report it and ask for direction when the sources above do not establish a clear answer.

## Content integrity

Never invent or embellish:

- Project claims, results, impact, or metrics
- Technologies, methods, datasets, or responsibilities
- Employers, roles, dates, education, or credentials
- Contact details, profile links, repository links, or URLs
- Resume content, images, testimonials, or awards

Use only content supplied or approved by Harkamal. Missing optional content must be omitted from the public interface. Development placeholders must be unmistakable and must not reach deployment.

Keep all portfolio content separate from rendering code in `portfolio_data.py`. Use plain Python dictionaries and lists unless an approved requirement justifies a more complex structure. Do not scatter portfolio copy through `app.py`.

## Homepage contract

Version 1 is a single-page portfolio with these sections in this exact order:

1. Hero
2. Featured Projects
3. Project Results / Impact
4. Skills
5. About
6. Education / Experience
7. Resume
8. Contact

Do not add, remove, rename, reorder, or split these sections without updating the approved specification.

## Architecture and repository structure

Use the smallest structure that satisfies the approved plan:

```text
portfolio/
├── AGENTS.md
├── SPEC.md
├── PLAN.md
├── app.py
├── portfolio_data.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
└── assets/
    ├── styles.css
    ├── images/
    └── resume.pdf
```

- `app.py` owns Streamlit page configuration, section composition, and rendering.
- `portfolio_data.py` is the single source for structured portfolio content.
- `.streamlit/config.toml` contains supported Streamlit theme and UI configuration.
- `assets/styles.css` contains focused portfolio-specific styling.
- `assets/images/` contains optimized, owned or explicitly licensed local images.
- `assets/resume.pdf` is added only when Harkamal supplies and approves the public resume.

Do not create empty directories or files in anticipation of future work. Do not add a component framework, CMS, state layer, build system, test framework, analytics package, or live data integration without an approved requirement.

## Streamlit implementation rules

- Use supported Streamlit APIs and Python standard-library features first.
- Keep runtime dependencies minimal. Version 1 should require only Streamlit unless a concrete approved requirement cannot be met without another package.
- Pin runtime dependencies to compatible versions for reproducible Community Cloud builds.
- Do not add JavaScript components, embedded remote applications, or frontend frameworks.
- Do not add a custom server, API endpoint, database, authentication, or secret-dependent feature.
- Do not add paid services or features that require a paid tier.
- Keep images, the resume, CSS, and other owned assets local to the repository.
- Prefer Streamlit theme configuration before CSS overrides.
- Keep CSS small and avoid selectors tied to generated class names when a stable or semantic selector is available.
- Avoid unnecessary computation, remote requests, and large dependencies during page rendering.

## Visual design

The result must look like a professional Data Science portfolio, not a default Streamlit dashboard or notebook.

- Use a cohesive palette, typography scale, spacing system, content width, and visual hierarchy.
- Present projects as concise case studies and give verified results or impact clear prominence.
- Do not use an unnecessary sidebar, dense widget grids, debug output, chart-first composition, or controls without a portfolio purpose.
- Keep Streamlit chrome visually restrained using supported configuration and maintainable CSS.
- Prefer clear, calm presentation over decorative complexity or excessive motion.
- Do not load remote fonts, images, or decorative assets when a local or system alternative is sufficient.

## Responsive and accessible behavior

- Preserve a logical reading and keyboard order.
- Use clear headings, descriptive links, meaningful image alternatives, sufficient color contrast, and visible focus styles.
- Do not rely on color alone to communicate meaning.
- Ensure buttons, downloads, and links are keyboard operable and clearly labeled.
- Design columns and cards to stack cleanly on narrow screens.
- Check for clipped text, obscured actions, and unintended horizontal overflow at 320, 375, 768, 1024, and 1440 px widths.
- Target WCAG 2.2 AA within Streamlit's platform constraints.

Accessibility basics must not be removed to simplify styling.

## Implementation workflow

For each approved phase or bounded change:

1. Confirm the relevant `FR-*`, `NFR-*`, and `AC-*` requirements in `SPEC.md`.
2. Inspect the files in scope and the current Git diff.
3. Make the smallest complete change that satisfies the active phase.
4. Run applicable validation after every significant change.
5. Review responsive behavior, accessibility, visual quality, and content accuracy when affected.
6. Report what changed, what was validated, and any unresolved content dependency or conflict.

Do not proceed past an approval gate on the user's behalf.

## Validation

Once the relevant files exist, the baseline checks are:

```bash
python -m pip check
python -m compileall app.py portfolio_data.py
streamlit run app.py --server.headless true
```

The dependency and compilation checks must exit successfully. The Streamlit command must start without an uncaught exception and be stopped after the smoke test.

After significant visual or content changes, also verify:

- All eight sections exist in the approved order.
- Content comes from `portfolio_data.py`.
- Local images, CSS, links, and resume behavior work.
- Mobile and desktop layouts remain usable.
- Keyboard navigation, focus, contrast, headings, and image alternatives remain accessible.
- No placeholder, invented claim, broken link, debug output, or unapproved remote request is present.

Run only checks that are available for the current phase. Never claim a check passed unless it was actually run.

## Deployment boundary

Streamlit Community Cloud is the only approved deployment target for version 1, but deployment is a separate user-authorized action.

Without explicit approval, do not:

- Connect or authorize a Git provider or Streamlit account
- Create, update, restart, share, or delete a cloud app
- Change Community Cloud settings, secrets, domains, or access controls
- Publish a preview or production URL

Local development and local validation do not authorize cloud activity.

## Git and safety

- Preserve user changes and keep unrelated edits out of the current task.
- Never commit secrets, `.env` files, private contact data, or unlicensed assets.
- Do not add deployment credentials to the repository.
- Do not rewrite Git history or delete user content without explicit permission.
- Keep commits focused by implementation phase when the user asks for commits.
