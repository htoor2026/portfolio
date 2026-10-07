"""Simple three-page Streamlit portfolio for Harkamal Toor."""

from html import escape
from pathlib import Path

import streamlit as st

from portfolio_data import PROFILE, PROJECTS, SOCIALS

ROOT = Path(__file__).parent


def safe(value: object) -> str:
    return escape(str(value), quote=True)


def load_css() -> None:
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


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

    image_col, about_col = st.columns([0.8, 1.35], gap="large", vertical_alignment="center")

    with image_col:
        st.image(
            ROOT / PROFILE["image"],
            caption=None,
            use_container_width=True,
        )
        st.caption(PROFILE["location"])

    with about_col:
        st.markdown("## About Me")
        for paragraph in PROFILE["about"]:
            st.write(paragraph)

        st.markdown("### How I work")
        pills = "".join(f'<span class="pill">{safe(item)}</span>' for item in PROFILE["personality"])
        st.html(f'<div class="pill-row">{pills}</div>')

    st.divider()
    st.markdown("## Technical Skills")
    skill_html = "".join(f'<span class="skill-pill">{safe(item)}</span>' for item in PROFILE["skills"])
    st.html(f'<div class="skill-row">{skill_html}</div>')

    st.html(f'<p class="education-line">{safe(PROFILE["education"])}</p>')

    st.divider()
    st.markdown("## Resume")
    st.write("Want the full technical background, projects, skills, and experience? Download my current resume.")
    resume_path = ROOT / PROFILE["resume"]
    st.download_button(
        "Download Resume",
        data=resume_path.read_bytes(),
        file_name="Harkamal_Toor_Data_Scientist_Resume.pdf",
        mime="application/pdf",
        type="primary",
        use_container_width=False,
    )


def project_card(project: dict) -> None:
    with st.container(border=True):
        st.html(f'<p class="project-category">{safe(project["category"])}</p>')
        st.markdown(f"### {project['title']}")
        st.write(project["summary"])
        st.html(f'<p class="featured-result">{safe(project["featured_result"])}</p>')
        tech = "".join(f'<span class="mini-pill">{safe(item)}</span>' for item in project["technologies"])
        st.html(f'<div class="mini-pill-row">{tech}</div>')

        a, b, c = st.columns([1.15, 1, 1])
        with a:
            if st.button("View Project", key=f"view-{project['slug']}", use_container_width=True):
                st.session_state.selected_project = project["slug"]
                st.rerun()
        with b:
            st.link_button("GitHub", project["github"], use_container_width=True)
        with c:
            if project["live"]:
                st.link_button("Live Demo", project["live"], use_container_width=True)


def project_detail(project: dict) -> None:
    if st.button("← Back to all projects"):
        st.session_state.selected_project = None
        st.rerun()

    st.html(
        f"""
        <section class="project-detail-hero">
            <p class="project-category">{safe(project['category'])}</p>
            <h1>{safe(project['title'])}</h1>
            <p>{safe(project['summary'])}</p>
        </section>
        """
    )

    st.markdown("### Problem")
    st.write(project["problem"])

    st.markdown("### Approach")
    st.write(project["approach"])

    st.markdown("### Technologies")
    tech = "".join(f'<span class="skill-pill">{safe(item)}</span>' for item in project["technologies"])
    st.html(f'<div class="skill-row">{tech}</div>')

    st.markdown("### Results")
    for result in project["results"]:
        st.markdown(f"- {result}")

    st.markdown("### Decision / Takeaway")
    st.info(project["decision"])

    left, right = st.columns(2)
    with left:
        st.link_button("View on GitHub", project["github"], use_container_width=True)
    with right:
        if project["live"]:
            st.link_button("Open Live Demo", project["live"], use_container_width=True)


def projects_page() -> None:
    selected = st.session_state.get("selected_project")
    if selected:
        project = next((item for item in PROJECTS if item["slug"] == selected), None)
        if project:
            project_detail(project)
            return

    page_intro(
        "Selected Work",
        "Projects",
        "A focused collection of experimentation, forecasting, decision-support, AI analytics, and production-oriented machine learning work.",
    )

    for row_start in range(0, len(PROJECTS), 3):
        cols = st.columns(3, gap="medium")
        for col, project in zip(cols, PROJECTS[row_start:row_start + 3]):
            with col:
                project_card(project)


def contact_page() -> None:
    page_intro(
        "Contact",
        "Let's Connect",
        "I'm focused on opportunities in Data Science, Machine Learning, experimentation, and applied AI.",
    )

    channels = [(label, url) for label, url in SOCIALS.items() if url]
    cols = st.columns(len(channels), gap="medium")
    for col, (label, url) in zip(cols, channels):
        with col:
            st.link_button(label, url, use_container_width=True)

    st.html(f'<p class="contact-location">{safe(PROFILE["location"])}</p>')

    if SOCIALS.get("Email"):
        st.link_button("Email", f"mailto:{SOCIALS['Email']}")
    else:
        st.caption("Public email will be added before deployment.")


st.set_page_config(
    page_title="Harkamal Toor | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()

pages = [
    st.Page(home_page, title="Home", default=True),
    st.Page(projects_page, title="Projects"),
    st.Page(contact_page, title="Contact"),
]

navigation = st.navigation(pages, position="top")
navigation.run()
