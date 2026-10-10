"""Simple Streamlit portfolio for Harkamal Singh."""

from html import escape
from pathlib import Path

import streamlit as st

from portfolio_data import (
    EDUCATION,
    OPEN_SOURCE_CONTRIBUTIONS,
    PROFILE,
    PROJECTS,
    SKILL_GROUPS,
    SOCIALS,
)

ROOT = Path(__file__).parent


def safe(value: object) -> str:
    return escape(str(value), quote=True)


def load_css() -> None:
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


def top_navigation() -> str:
    pages = ("Home", "Resume", "Projects", "Contact")
    requested = st.query_params.get("page", "Home")
    active = requested if requested in pages else "Home"

    links = "".join(
        (
            f'<a class="nav-link{" active" if page == active else ""}" '
            f'href="?page={page}" target="_self">{page}</a>'
        )
        for page in pages
    )
    st.html(
        f"""
        <nav class="portfolio-nav" aria-label="Main navigation">
            <a class="nav-brand" href="?page=Home" target="_self">Portfolio</a>
            <div class="nav-links">{links}</div>
        </nav>
        """
    )
    return active


def page_intro(kicker: str, title: str, copy: str) -> None:
    st.html(
        f"""
        <section class="page-intro">
            <p class="eyebrow">{safe(kicker)}</p>
            <h1>{safe(title)}</h1>
            <p>{safe(copy)}</p>
        </section>
        """
    )


def home_page() -> None:
    hero_text, hero_image = st.columns(
        [1.08, 0.92],
        gap="large",
        vertical_alignment="center",
    )

    with hero_text:
        st.html(
            f"""
            <section class="hero-band">
                <p class="eyebrow light">Portfolio</p>
                <h1>{safe(PROFILE['name']).upper()}</h1>
                <p class="hero-role">{safe(PROFILE['headline'])}</p>
                <p class="hero-sub">{safe(PROFILE['subheadline'])}</p>
            </section>
            """
        )

    with hero_image:
        st.image(
            ROOT / PROFILE["image"],
            caption=None,
            use_container_width=True,
            alt=PROFILE["image_alt"],
        )
        st.caption(PROFILE["location"])

    st.divider()

    about_col, work_col = st.columns(
        [1.45, 0.75],
        gap="large",
        vertical_alignment="top",
    )

    with about_col:
        st.markdown("## About Me")
        for paragraph in PROFILE["about"]:
            st.write(paragraph)

    with work_col:
        st.markdown("### How I work")
        pills = "".join(
            f'<span class="pill">{safe(item)}</span>'
            for item in PROFILE["personality"]
        )
        st.html(f'<div class="pill-row">{pills}</div>')

    st.divider()
    st.markdown("## Technical Skills")

    for row_start in range(0, len(SKILL_GROUPS), 2):
        cols = st.columns(2, gap="medium")
        for col, group in zip(cols, SKILL_GROUPS[row_start : row_start + 2]):
            with col:
                with st.container(border=True):
                    st.markdown(f"### {group['category']}")
                    items = "".join(
                        f'<span class="skill-pill">{safe(item)}</span>'
                        for item in group["items"]
                    )
                    st.html(f'<div class="skill-row">{items}</div>')

    st.divider()
    st.markdown("## Education")

    for item in EDUCATION:
        with st.container(border=True):
            st.html('<p class="resume-label">Education</p>')
            st.markdown(f"### {item['credential']}")
            st.markdown(f"**{item['institution']}**")
            st.write(f"{item['location']} · {item['dates']}")
            st.markdown("**Relevant areas**")
            areas = "".join(
                f'<span class="skill-pill">{safe(area)}</span>'
                for area in item["areas"]
            )
            st.html(f'<div class="skill-row">{areas}</div>')


def resume_page() -> None:
    page_intro(
        "Resume",
        "Resume",
        "View the complete resume here without downloading it. A download option is available at the bottom.",
    )

    resume_path = ROOT / PROFILE["resume"]
    st.pdf(
        resume_path,
        height=1100,
        alt="Harkamal Singh data scientist resume",
    )

    st.divider()
    st.html(
        """
        <div class="download-copy">
            <h2>Download Resume</h2>
            <p>Prefer a local copy? Download the complete PDF below.</p>
        </div>
        """
    )

    left, center, right = st.columns([1.35, 1, 1.35])
    with center:
        st.download_button(
            "Download Resume",
            data=resume_path.read_bytes(),
            file_name="Harkamal_Toor_Data_Scientist_Resume.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )


def project_card(project: dict) -> None:
    with st.container(border=True):
        st.html(f'<p class="project-category">{safe(project["category"])}</p>')
        st.markdown(f"### {project['title']}")
        st.write(project["summary"])
        st.html(
            f'<p class="featured-result">{safe(project["featured_result"])}</p>'
        )

        tech = "".join(
            f'<span class="mini-pill">{safe(item)}</span>'
            for item in project["technologies"]
        )
        st.html(f'<div class="mini-pill-row">{tech}</div>')

        live_col, github_col = st.columns(2)

        with live_col:
            if project["live"]:
                st.link_button(
                    "View Project",
                    project["live"],
                    type="primary",
                    use_container_width=True,
                )
            else:
                st.button(
                    "View Project",
                    key=f"missing-live-{project['slug']}",
                    disabled=True,
                    use_container_width=True,
                    help="Live application link has not been added yet.",
                )

        with github_col:
            st.link_button(
                "GitHub",
                project["github"],
                use_container_width=True,
            )


def projects_page() -> None:
    page_intro(
        "Selected Work",
        "Projects",
        "Each project links directly to its live application when a public deployment is available, with GitHub alongside it.",
    )

    for row_start in range(0, len(PROJECTS), 3):
        cols = st.columns(3, gap="medium")
        for col, project in zip(cols, PROJECTS[row_start : row_start + 3]):
            with col:
                project_card(project)

    st.divider()
    st.markdown("## Open-Source Contributions")
    st.write(
        "Python bug fixes, regression tests, and documentation improvements "
        "contributed to aeon-neuro and Kedro Plugins. View each pull request "
        "for its latest review or merge status."
    )

    for row_start in range(0, len(OPEN_SOURCE_CONTRIBUTIONS), 2):
        cols = st.columns(2, gap="medium")
        for col, contribution in zip(
            cols, OPEN_SOURCE_CONTRIBUTIONS[row_start : row_start + 2]
        ):
            with col:
                with st.container(border=True):
                    st.caption(contribution["repository"])
                    st.markdown(f"### {contribution['title']}")
                    st.write(contribution["summary"])
                    st.link_button(
                        f"View Pull Request #{contribution['pr_number']}",
                        contribution["url"],
                    )


def contact_page() -> None:
    page_intro(
        "Contact",
        "Let's Connect",
        "I'm focused on opportunities in Data Science, Machine Learning, experimentation, and applied AI.",
    )

    channels = [
        (label, url)
        for label, url in SOCIALS.items()
        if url and label != "Email"
    ]
    cols = st.columns(len(channels) + 1, gap="medium")

    for col, (label, url) in zip(cols, channels):
        with col:
            st.link_button(label, url, use_container_width=True)

    with cols[-1]:
        st.link_button(
            "Email",
            f"mailto:{SOCIALS['Email']}",
            use_container_width=True,
        )

    st.html(
        f'<p class="contact-location">{safe(PROFILE["location"])} · '
        f'{safe(SOCIALS["Email"])}</p>'
    )


st.set_page_config(
    page_title="Harkamal Singh | Data Science Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()
active_page = top_navigation()

if active_page == "Home":
    home_page()
elif active_page == "Resume":
    resume_page()
elif active_page == "Projects":
    projects_page()
else:
    contact_page()
