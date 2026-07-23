import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ryan Brown | Performance Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    /* Main Background & Text */
    .stApp {
        background-color: #FCF9F2;
        color: #000000;
        font-family: 'serif';
    }

    /* Headlines */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: #000000 !important;
    }

    /* Sidebar - Dark Emerald Green */
    [data-testid="stSidebar"] {
        background-color: #043927 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Custom Education Box (Thin Emerald Border) */
    .edu-box {
        border: 1px solid #043927;
        padding: 20px;
        border-radius: 2px;
        color: #000000;
        background-color: transparent;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 2px;
        height: 3em;
        background-color: #043927;
        color: #FCF9F2;
        border: 1px solid #043927;
        font-family: 'Playfair Display', serif;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #FCF9F2;
        color: #043927;
        border: 1px solid #043927;
    }

    /* Anchor Link Offset */
    span[id] {
        scroll-margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("# Navigation")
    st.markdown("---")
    st.markdown("### [About Me](#about-me)")
    st.markdown("### [My Work](#my-work)")
    st.markdown("### [Contact Details](#contact-details)")
    st.write("---")
    st.caption("Ryan Brown | Christchurch, Bournemouth")

# --- SECTION 1: ABOUT ME ---
st.markdown('<span id="about-me"></span>', unsafe_allow_html=True)
st.title("Ryan Brown")
st.markdown("### *Performance Analyst & Data Scientist*")
st.markdown("📍 Christchurch, Bournemouth (UK)")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### **Professional Profile**")
    st.write("""
    I am an MSc Sports Performance Analysis student with a background in Sport & Exercise Science, 
    specializing in the design of performance analysis workflows and the integration of multi-disciplinary 
    data. My expertise lies in translating complex metrics into actionable insights—not only for elite 
    coaching and sport science teams but also for commercial business environments, where I apply 
    data-driven strategies to solve real-world organizational challenges.
    """)
    
    st.markdown("#### **Experience & Placements**")
    st.write("""
    - **British Obstacle Sports (BOS) | Data Science & Visualisation Analyst:** 
      Analysed competition datasets across UK national leagues to support accurate athlete rankings. 
      Designed Power BI dashboards for online publication and produced monthly performance summaries 
      for the Technical Committee.
    - **BU Men’s 2nd Football Team | Performance Analyst:** 
      Designed and implemented match coding templates in Hudl Sportscode aligned with team KPIs. 
      Developed post-match Power BI dashboards to support tactical debriefs and training design.
    """)

with col2:
    st.markdown("#### **Education History**")
    st.markdown("""
        <div class="edu-box">
            <strong>Bournemouth University</strong><br>
            MSc Sports Performance Analysis<br>
            (Current)<br><br>
            <strong>University of Portsmouth</strong><br>
            BSc (Hons) Sport & Exercise Science<br>
            (2024)
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# --- SECTION 2: MY WORK ---
st.markdown('<span id="my-work"></span>', unsafe_allow_html=True)
st.title("📂 My Work")

project_choice = st.selectbox(
    "Choose a project to view details:", 
    [
        "Python - Data Cleaning", 
        "MDT Support Hub Website", 
        "Power BI Athlete Performance Dashboard", 
        "Internship Placement Power BI Leaderboard", 
        "Hudl Sportscode"
    ]
)

st.markdown(f"### {project_choice}")

if project_choice == "Python - Data Cleaning":
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.write("""
        Built an automated Python workflow to clean, merge, and process weekly performance data. 
        - Integrating **S&C, physiology, medical, and coaching datasets** into a unified structure.
        - Applying structured **quality control processes**, including error checking and variable naming.
        - Developing cross-disciplinary visualisations using **Machine Learning** to link training load to readiness.
        """)
    with c2:
        st.warning("Media coming soon")

elif project_choice == "MDT Support Hub Website":
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.write("""
        Engineered a centralized, password-protected web application using **Streamlit** to serve as a 
        real-time decision-support hub for a Multi-Disciplinary Team (MDT).
        - Developed data pipelines to ingest **GPS (Pitch), Gym (S&C), Wellness, and Medical/Injury** records.
        - Programmed complex algorithms including **ACWR (Acute:Chronic Workload Ratios)** and Efficiency Indices.
        """)
    with c2:
        st.warning("Media coming soon")

elif project_choice == "Power BI Athlete Performance Dashboard":
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.write("""
        Designed a performance readiness dashboard tailored specifically for Sport Scientists.
        - Applied advanced **DAX calculations** and interactive filtering to assess athlete readiness.
        - Analysed six-week performance trends to highlight potential injury concerns.
        """)
    with c2:
        st.warning("Media coming soon")

elif project_choice == "Internship Placement Power BI Leaderboard":
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.write("""
        Developed during my placement to gamify performance and track developmental milestones.
        - Analysed competition datasets from multiple UK leagues to support accurate athlete standings.
        - Maintained data accuracy and version control while collaborating with remote stakeholders.
        """)
    with c2:
        st.warning("Media coming soon")

elif project_choice == "Hudl Sportscode":
    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.write("""
        Designed and justified a personalized performance analysis workflow in a professional football environment.
        - Developed a **"What It Takes To Win" (WITTW)** performance model.
        - Conducted intra- and inter-rater reliability testing to ensure data validity.
        """)
    with c2:
        st.warning("Media coming soon")

st.write("---")

# --- SECTION 3: CONTACT DETAILS ---
st.markdown('<span id="contact-details"></span>', unsafe_allow_html=True)
st.title("✉️ Contact Details")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Reach Out")
    st.write(f"**Email:** [Ryanlarsson14@gmail.com](mailto:Ryanlarsson14@gmail.com)")
    st.write(f"**LinkedIn:** [View Profile](https://www.linkedin.com/in/ryan-brown-460bb3344)")

with col_b:
    st.markdown("### My CV")
    # DATA CV
    try:
        with open("Data_Analyst_and_Scientist_CV.pdf", "rb") as f:
            st.download_button("📊 Data Analyst / Scientist CV", f, file_name="Ryan_Brown_Data_CV.pdf")
    except:
        st.error("Data CV File Missing")

    # SPORT CV
    try:
        with open("Sports Performance Analysis CV.pdf", "rb") as f:
            st.download_button("🏃 Sports Performance Analysis CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
    except:
        st.error("Sport CV File Missing")

# --- FOOTER ---
st.write("---")
st.caption("Built by Ryan Brown | © 2026 | Christchurch, Bournemouth (UK)")
