"""Verified portfolio content, kept separate from Streamlit presentation."""


PORTFOLIO_DATA = {
    "identity": {
        "name": "Harkamal Toor",
        "page_title": "Harkamal Toor | Data Science Portfolio",
        "eyebrow": "Data Science Portfolio",
        "location": "Greater Toronto Area, Canada",
        "headline": (
            "Data Scientist | Machine Learning | A/B Testing & Experimentation | "
            "Python • SQL • Statistics"
        ),
        "focus": (
            "Data Science",
            "Machine Learning",
            "AI",
            "A/B Testing and Experimentation",
        ),
        "summary": (
            "Computer Programming background focused on Data Science, Machine "
            "Learning, experimentation, and end-to-end problem solving for business "
            "decisions."
        ),
        "primary_action": {
            "label": "Explore selected work",
            "href": "#featured-projects",
        },
        "secondary_action": {
            "label": "Contact",
            "href": "#contact",
        },
        "profile_image": None,
        "profile_image_alt": None,
        "profile_image_initials": "HT",
        "profile_image_placeholder": (
            "PLACEHOLDER — verified profile image not supplied."
        ),
    },
    "sections": (
        {"id": "hero", "title": "Hero"},
        {"id": "featured-projects", "title": "Featured Projects"},
        {"id": "project-results", "title": "Project Results / Impact"},
        {"id": "technical-skills", "title": "Technical Skills"},
        {"id": "about", "title": "About"},
        {"id": "education-experience", "title": "Education / Experience"},
        {"id": "resume", "title": "Resume"},
        {"id": "contact", "title": "Contact"},
    ),
    "projects_intro": (
        "Selected work across applied AI, controlled experimentation, climate analysis, "
        "predictive modeling, recommendation systems, and end-to-end ML practice."
    ),
    "projects": (
        {
            "title": "Flight Pulse",
            "status": "Verified purpose",
            "purpose": (
                "AI-assisted flight delay intelligence system combining flight, "
                "weather, and contextual information to help explain flight delays."
            ),
            "highlights": (),
            "note": (
                "PLACEHOLDER — verified technologies, quantitative results, and a "
                "publicly accessible live-demo URL are not yet available."
            ),
            "is_placeholder": False,
            "link": "https://github.com/htoor2026/flight-pulse",
            "link_label": "GitHub",
        },
        {
            "title": "A/B Testing & Personalization",
            "status": "Verified experiment",
            "purpose": (
                "End-to-end controlled experiment comparing popularity-based "
                "recommendations with personalized recommendations."
            ),
            "highlights": (
                "28,000 synthetic users",
                "+9.05% relative CTR lift",
                "p-value: 0.0171",
            ),
            "note": (
                "PLACEHOLDER — verified technologies and a live-demo URL are not yet "
                "available."
            ),
            "is_placeholder": False,
            "link": "https://github.com/htoor2026/ab-testing-movie-app",
            "link_label": "GitHub",
        },
        {
            "title": "Toronto Climate / Weather Analysis",
            "status": "Verified analysis",
            "purpose": "Long-term Toronto climate and time-series analysis.",
            "highlights": (
                "1953-05-04 through 2023-12-31",
                "+0.218°C annual mean warming per decade",
                "1991–2020 baseline mean: 8.8492°C",
            ),
            "note": None,
            "is_placeholder": False,
            "link": None,
            "link_label": None,
        },
        {
            "title": "Customer Churn Prediction",
            "status": "Details pending",
            "purpose": "PLACEHOLDER — verified project purpose is not yet available.",
            "highlights": (),
            "note": (
                "PLACEHOLDER — verified technologies, results, and public links are not "
                "yet available."
            ),
            "is_placeholder": True,
            "link": None,
            "link_label": None,
        },
        {
            "title": "Retail / Recommendation Intelligence",
            "status": "Details pending",
            "purpose": "PLACEHOLDER — verified project purpose is not yet available.",
            "highlights": (),
            "note": (
                "PLACEHOLDER — verified technologies, results, and public links are not "
                "yet available."
            ),
            "is_placeholder": True,
            "link": None,
            "link_label": None,
        },
        {
            "title": "End-to-End ML System",
            "status": "Verified focus",
            "purpose": "End-to-end ML workflow and engineering practices.",
            "highlights": (),
            "note": (
                "PLACEHOLDER — verified technologies, results, and public links are not "
                "yet available."
            ),
            "is_placeholder": False,
            "link": None,
            "link_label": None,
        },
    ),
    "results_intro": (
        "Verified evidence is shown only where quantitative results were supplied."
    ),
    "results": (
        {
            "title": "A/B Testing & Personalization",
            "summary": (
                "Controlled experiment comparing a popularity-based recommender with a "
                "personalized treatment."
            ),
            "metrics": (
                {"value": "28,000", "label": "Synthetic users"},
                {"value": "9.343%", "label": "Control CTR"},
                {"value": "10.188%", "label": "Treatment CTR"},
                {"value": "+0.846 pp", "label": "Absolute lift"},
                {"value": "+9.05%", "label": "Relative lift"},
                {"value": "0.0171", "label": "p-value"},
                {
                    "value": "+0.150 to +1.541 pp",
                    "label": "95% confidence interval",
                },
                {"value": "+1.595 pp", "label": "Returning-user lift"},
                {
                    "value": "+2.066 pp",
                    "label": "Treatment × returning-user interaction",
                },
                {"value": "+27.8 ms", "label": "Latency increase"},
            ),
            "decision_label": "Final decision",
            "decision": (
                "Do not roll out globally; personalize for returning users while keeping "
                "new users on the popularity-based recommender."
            ),
        },
        {
            "title": "Toronto Climate / Weather Analysis",
            "summary": "Long-term Toronto climate and time-series analysis.",
            "metrics": (
                {
                    "value": "1953-05-04 — 2023-12-31",
                    "label": "Dataset coverage",
                },
                {"value": "8.8492°C", "label": "1991–2020 baseline mean"},
                {"value": "+0.218°C", "label": "Annual mean trend per decade"},
                {"value": "+0.301°C", "label": "Winter trend per decade"},
                {"value": "+0.194°C", "label": "Spring trend per decade"},
                {"value": "+0.263°C", "label": "Summer trend per decade"},
                {"value": "+0.128°C", "label": "Fall trend per decade"},
            ),
            "decision_label": None,
            "decision": None,
        },
    ),
    "skills_intro": (
        "Tools and methods included from the verified portfolio skill set."
    ),
    "skills": (
        {
            "category": "Programming & Data",
            "items": ("Python", "SQL", "NumPy", "Pandas", "Matplotlib"),
        },
        {
            "category": "Machine Learning",
            "items": (
                "scikit-learn",
                "XGBoost",
                "TensorFlow / Keras",
                "Machine Learning",
                "Deep Learning",
                "Uplift Modeling",
            ),
        },
        {
            "category": "Experimentation & Statistics",
            "items": (
                "Statistics",
                "A/B Testing",
                "Hypothesis Testing",
                "Power Analysis",
                "Causal Inference",
                "Time Series",
            ),
        },
        {
            "category": "Engineering & Delivery",
            "items": (
                "Git",
                "Docker",
                "FastAPI",
                "MLflow",
                "ZenML",
                "Streamlit",
            ),
        },
    ),
    "about": {
        "intro": "Data Science, Machine Learning, and experimentation focus.",
        "paragraphs": (
            (
                "Harkamal Toor has a Computer Programming background and focuses on Data "
                "Science, Machine Learning, AI, and A/B testing."
            ),
            (
                "The portfolio emphasizes end-to-end problem solving: framing a question, "
                "working through data and modeling, evaluating evidence, and connecting "
                "results to business decisions."
            ),
        ),
    },
    "education_experience": {
        "intro": "Verified education and experience information.",
        "education": (
            {
                "credential": "Computer Programming Diploma",
                "institution": "Conestoga College",
                "dates": None,
            },
        ),
        "experience": (
            {
                "role": "PLACEHOLDER — verified experience details required.",
                "organization": None,
                "dates": None,
                "highlights": (),
            },
        ),
    },
    "resume": {
        "available": False,
        "file": None,
        "url": None,
        "intro": "Resume availability and download.",
        "message": (
            "PLACEHOLDER — an approved public resume PDF or URL has not been supplied."
        ),
    },
    "contact": {
        "intro": (
            "Connect through verified public professional profiles. PLACEHOLDER — a "
            "verified public email address has not been supplied."
        ),
        "location_label": "Location",
        "location": "Greater Toronto Area, Canada",
        "channels": (
            {
                "label": "Email",
                "url": None,
                "placeholder": "PLACEHOLDER — verified link required.",
            },
            {
                "label": "GitHub",
                "url": "https://github.com/htoor2026",
            },
            {
                "label": "LinkedIn",
                "url": "https://www.linkedin.com/in/harkamal-s/",
            },
            {
                "label": "X",
                "url": "https://x.com/HarryToor01",
            },
        ),
    },
    "footer": "Harkamal Toor · Greater Toronto Area, Canada",
}
