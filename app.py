"""Streamlit presentation for the portfolio content."""

from html import escape
from pathlib import Path
from typing import Any

import streamlit as st

from portfolio_data import PORTFOLIO_DATA


ROOT = Path(__file__).parent
SECTIONS = {section["id"]: section for section in PORTFOLIO_DATA["sections"]}


def text(value: Any) -> str:
    """Escape local content before placing it in HTML."""
    return escape(str(value), quote=True)


def load_local_css() -> None:
    """Load the repository-owned stylesheet."""
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


def section_heading(section_id: str, intro: str) -> str:
    section = SECTIONS[section_id]
    heading_id = f"{section_id}-heading"
    return f"""
        <header class="section-heading">
            <p class="section-index" aria-hidden="true">{text(section['title'])}</p>
            <h2 id="{heading_id}">{text(section['title'])}</h2>
            <p>{text(intro)}</p>
        </header>
    """


def action_link(action: dict[str, str], secondary: bool = False) -> str:
    css_class = "button button-secondary" if secondary else "button"
    return (
        f'<a class="{css_class}" href="{text(action["href"])}">'
        f'{text(action["label"])}</a>'
    )


def render_navigation() -> str:
    items = "".join(
        f'<li><a href="#{text(section["id"])}">{text(section["title"])}</a></li>'
        for section in PORTFOLIO_DATA["sections"]
    )
    return f"""
        <nav class="site-nav" aria-label="Portfolio sections">
            <ul>{items}</ul>
        </nav>
    """


def render_hero() -> str:
    identity = PORTFOLIO_DATA["identity"]
    focus = "".join(
        f'<li>{text(item)}</li>' for item in identity["focus"]
    )
    profile = f"""
        <div class="profile-placeholder" role="img"
             aria-label="{text(identity['profile_image_placeholder'])}">
            <span>{text(identity['profile_image_initials'])}</span>
            <p>{text(identity['profile_image_placeholder'])}</p>
        </div>
    """
    return f"""
        <section id="hero" class="portfolio-hero" aria-labelledby="hero-heading">
            <div class="hero-panel">
                <div class="hero-layout">
                    <div class="hero-copy">
                        <p class="hero-eyebrow">{text(identity['eyebrow'])}</p>
                        <h1 id="hero-heading">{text(identity['name'])}</h1>
                        <p class="hero-headline">{text(identity['headline'])}</p>
                        <p class="hero-summary">{text(identity['summary'])}</p>
                        <ul class="focus-list" aria-label="Professional focus">{focus}</ul>
                        <p class="hero-location">{text(identity['location'])}</p>
                        <div class="hero-actions">
                            {action_link(identity['primary_action'])}
                            {action_link(identity['secondary_action'], secondary=True)}
                        </div>
                    </div>
                    {profile}
                </div>
            </div>
        </section>
    """


def render_project_card(project: dict[str, Any]) -> str:
    highlights = ""
    if project["highlights"]:
        items = "".join(
            f"<li>{text(item)}</li>" for item in project["highlights"]
        )
        highlights = f'<ul class="project-highlights">{items}</ul>'

    note = ""
    if project["note"]:
        note = f'<p class="placeholder-note">{text(project["note"])}</p>'

    link = ""
    if project["link"]:
        link = (
            f'<a class="text-link" href="{text(project["link"])}" '
            'target="_blank" rel="noreferrer">'
            f'{text(project["link_label"])}</a>'
        )

    placeholder_class = " is-placeholder" if project["is_placeholder"] else ""
    return f"""
        <article class="project-card{placeholder_class}">
            <p class="card-status">{text(project['status'])}</p>
            <h3>{text(project['title'])}</h3>
            <p class="project-purpose">{text(project['purpose'])}</p>
            {highlights}
            {note}
            {link}
        </article>
    """


def render_projects() -> str:
    cards = "".join(
        render_project_card(project) for project in PORTFOLIO_DATA["projects"]
    )
    return f"""
        <section id="featured-projects" class="portfolio-section"
                 aria-labelledby="featured-projects-heading">
            {section_heading('featured-projects', PORTFOLIO_DATA['projects_intro'])}
            <div class="project-grid">{cards}</div>
        </section>
    """


def render_metric(metric: dict[str, str]) -> str:
    return f"""
        <div class="metric-card">
            <p class="metric-value">{text(metric['value'])}</p>
            <p class="metric-label">{text(metric['label'])}</p>
        </div>
    """


def render_result_group(result: dict[str, Any]) -> str:
    metrics = "".join(render_metric(metric) for metric in result["metrics"])
    decision = ""
    if result["decision"]:
        decision = f"""
            <div class="decision-callout">
                <p>{text(result['decision_label'])}</p>
                <strong>{text(result['decision'])}</strong>
            </div>
        """
    return f"""
        <article class="result-group">
            <header>
                <h3>{text(result['title'])}</h3>
                <p>{text(result['summary'])}</p>
            </header>
            <div class="metrics-grid">{metrics}</div>
            {decision}
        </article>
    """


def render_results() -> str:
    groups = "".join(
        render_result_group(result) for result in PORTFOLIO_DATA["results"]
    )
    return f"""
        <section id="project-results" class="portfolio-section"
                 aria-labelledby="project-results-heading">
            {section_heading('project-results', PORTFOLIO_DATA['results_intro'])}
            <div class="results-stack">{groups}</div>
        </section>
    """


def render_skills() -> str:
    groups = []
    for skill_group in PORTFOLIO_DATA["skills"]:
        items = "".join(
            f"<li>{text(item)}</li>" for item in skill_group["items"]
        )
        groups.append(
            f"""
            <article class="skill-group">
                <h3>{text(skill_group['category'])}</h3>
                <ul>{items}</ul>
            </article>
            """
        )
    return f"""
        <section id="technical-skills" class="portfolio-section"
                 aria-labelledby="technical-skills-heading">
            {section_heading('technical-skills', PORTFOLIO_DATA['skills_intro'])}
            <div class="skills-grid">{''.join(groups)}</div>
        </section>
    """


def render_about() -> str:
    about = PORTFOLIO_DATA["about"]
    paragraphs = "".join(
        f"<p>{text(paragraph)}</p>" for paragraph in about["paragraphs"]
    )
    return f"""
        <section id="about" class="portfolio-section" aria-labelledby="about-heading">
            {section_heading('about', about['intro'])}
            <div class="prose-card">{paragraphs}</div>
        </section>
    """


def render_education_experience() -> str:
    content = PORTFOLIO_DATA["education_experience"]
    education = "".join(
        f"""
        <article class="timeline-card">
            <p class="card-label">Education</p>
            <h3>{text(item['credential'])}</h3>
            <p>{text(item['institution'])}</p>
        </article>
        """
        for item in content["education"]
    )
    experience = "".join(
        f"""
        <article class="timeline-card is-placeholder">
            <p class="card-label">Experience</p>
            <h3>{text(item['role'])}</h3>
        </article>
        """
        for item in content["experience"]
    )
    return f"""
        <section id="education-experience" class="portfolio-section"
                 aria-labelledby="education-experience-heading">
            {section_heading('education-experience', content['intro'])}
            <div class="timeline-grid">{education}{experience}</div>
        </section>
    """


def render_resume() -> str:
    resume = PORTFOLIO_DATA["resume"]
    return f"""
        <section id="resume" class="portfolio-section" aria-labelledby="resume-heading">
            {section_heading('resume', resume['intro'])}
            <div class="placeholder-panel">
                <p>{text(resume['message'])}</p>
            </div>
        </section>
    """


def render_contact_channel(channel: dict[str, Any]) -> str:
    if channel["url"]:
        return (
            f'<a class="contact-card" href="{text(channel["url"])}" '
            'target="_blank" rel="noreferrer">'
            f'<span>{text(channel["label"])}</span><strong>Open profile</strong></a>'
        )
    return f"""
        <div class="contact-card is-placeholder">
            <span>{text(channel['label'])}</span>
            <strong>{text(channel['placeholder'])}</strong>
        </div>
    """


def render_contact() -> str:
    contact = PORTFOLIO_DATA["contact"]
    channels = "".join(
        render_contact_channel(channel) for channel in contact["channels"]
    )
    return f"""
        <section id="contact" class="portfolio-section" aria-labelledby="contact-heading">
            {section_heading('contact', contact['intro'])}
            <div class="contact-location">
                <span>{text(contact['location_label'])}</span>
                <strong>{text(contact['location'])}</strong>
            </div>
            <div class="contact-grid">{channels}</div>
        </section>
    """


def render_page() -> str:
    return f"""
        <a class="skip-link" href="#main-content">Skip to main content</a>
        {render_navigation()}
        <main id="main-content">
            {render_hero()}
            {render_projects()}
            {render_results()}
            {render_skills()}
            {render_about()}
            {render_education_experience()}
            {render_resume()}
            {render_contact()}
        </main>
        <footer class="site-footer"><p>{text(PORTFOLIO_DATA['footer'])}</p></footer>
    """


st.set_page_config(
    page_title=PORTFOLIO_DATA["identity"]["page_title"],
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_local_css()
st.html(render_page())
