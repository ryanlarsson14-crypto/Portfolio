import streamlit as st
import os

# --- MEDIA SETTINGS (Replace YOUR_VIDEO_ID with your actual YouTube IDs) ---
URL_MDT_HUB = "https://youtu.be/_AYWoKyvQTo"
URL_PBI_DASHBOARD = "https://youtu.be/oGp9sHEOP0U"
URL_LEADERBOARD = "https://youtu.be/2pnC_YBjekI"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ryan Brown | Performance Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    .stApp { background-color: #FCF9F2; color: #000000; font-family: 'serif'; }
    h1, h2, h3, h4 { font-family: 'Playfair Display', serif; color: #000000 !important; }

    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #043927 !important; }
    [data-testid="stSidebar"] * { color: white !important; }

    /* Education Box */
    .edu-box { border: 3px solid #043927; padding: 20px; border-radius: 2px; color: #000000; }

    /* Buttons */
    .stButton>button {
        width: 100%; border-radius: 2px; height: 3em; background-color: transparent;
        color: #043927; border: 2px solid #043927; font-family: 'Playfair Display', serif; transition: 0.4s;
    }
    .stButton>button:hover { background-color: #043927; color: #FCF9F2; }

    /* Slicer (Selectbox) */
    div[data-baseweb="select"] > div { background-color: #043927 !important; color: white !important; border: none !important; }
    div[data-testid="stSelectbox"] label p { color: #000000 !important; }
    div[data-baseweb="select"] * { color: white !important; }

    /* Workflow Arrows */
    .arrow { font-size: 50px; text-align: center; color: #043927; margin: 10px 0; }
    
    span[id] { scroll-margin-top: 50px; }
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
    - **BU Men’s 2nd Football Team | Performance Analyst:** 
      Designed and implemented match coding templates in Hudl Sportscode aligned with team KPIs. 
    """)

with col2:
    st.markdown("#### **Education History**")
    st.markdown("""<div class="edu-box"><strong>Bournemouth University</strong><br>MSc Sports Performance Analysis<br>(Current)<br><br><strong>University of Portsmouth</strong><br>BSc (Hons) Sport & Exercise Science<br>(2024)</div>""", unsafe_allow_html=True)

st.write("---")

# --- SECTION 2: MY WORK ---
st.markdown('<span id="my-work"></span>', unsafe_allow_html=True)
st.title("📂 My Work")

# --- THE SLICER ---
# The CSS below handles the color. Just ensure this stays in your <style> block:
st.markdown("""
<style>
    /* Emerald Green Slicer */
    div[data-baseweb="select"] > div { 
        background-color: #043927 !important; 
        color: white !important; 
    }
    div[data-baseweb="select"] span { 
        color: white !important; 
    }
</style>
""", unsafe_allow_html=True)

project_choice = st.selectbox(
    "Choose a project to view details:", 
    ["Python - Data Cleaning", "MDT Support Hub Website", "Power BI Athlete Performance Dashboard", "Internship Placement Power BI Leaderboard", "Hudl Sportscode"]
)

st.markdown(f"### {project_choice}")
if project_choice == "Python - Data Cleaning":
    st.write("Built an automated Python workflow to clean, merge, and process weekly performance data.")
    st.markdown("""
    - Integrated S&C, physiology, medical, psychology, and coaching datasets into a unified and repeatable data structure.
    - Applied structured quality control processes including error checking and consistent variable naming.
    - Developed cross-disciplinary visualisations using machine learning to link training load, readiness, and risk indicators.
    """)
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("##### 1. Raw / Unclean Data")
        st.image("images/Unclean Data.png")
        st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)
        
        st.markdown("##### 2. The Python Cleaning Function")
        st.image("images/Cleaning Function.png")
        st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)
        
        st.markdown("##### 3. Standardized Clean Output")
        st.image("images/Clean Data.png")

elif project_choice == "MDT Support Hub Website":
    st.write("Engineered a centralized, password-protected web application using Streamlit to serve as a real-time decision-support hub for a Multi-Disciplinary Team (MDT).")
    st.markdown("""
    - Developed automated data pipelines to ingest and normalize disparate datasets, including GPS (Pitch), Gym (S&C), Wellness, and Medical/Injury records.
    - Programmed complex performance algorithms, including Acute:Chronic Workload Ratios (ACWR) and weighted "Athlete Readiness" scores.
    - Designed bespoke UI/UX interfaces for specific stakeholders to provide tailored tactical and physiological insights.
    """)
    st.video(URL_MDT_HUB)

elif project_choice == "Power BI Athlete Performance Dashboard":
    st.write("Designed a performance readiness dashboard tailored to a sport scientist audience.")
    st.markdown("""
    - Applied structured data modelling, DAX calculations, and interactive filtering.
    - Analysed six-week performance trends to assess athlete readiness and highlight potential concerns.
    - Delivered tailored insights to coaches and sport scientists, defending analytical decisions in a live panel setting.
    """)
    st.video(URL_PBI_DASHBOARD)

elif project_choice == "Internship Placement Power BI Leaderboard":
    st.write("Data Science & Visualisation Analyst placement focused on national athletic standings.")
    st.markdown("""
    - Analysed competition datasets from multiple UK national obstacle course racing leagues to support accurate athlete rankings.
    - Designed clear and engaging data visualisations/dashboards using Power BI and Excel for online publication.
    - Maintained data accuracy and version control while collaborating remotely with stakeholders across sport operations.
    """)
    st.video(URL_LEADERBOARD)

elif project_choice == "Hudl Sportscode":
    st.write("Designed and justified a personalised performance analysis workflow aligned with coaching philosophy.")
    st.markdown("""
    - Developed and validated a “What It Takes to Win” performance model aligned with coaching priorities.
    - Conducted intra- and inter-rater reliability testing using Hudl Sportscode and Excel.
    - Produced coding windows, structured reports, and video playlists to support match feedback and tactical discussions.
    """)
    st.image("images/Code Window.png")

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
    # No header or extra styling here to ensure it stays clean
    
    # Data CV
    try:
        with open("Data_Analyst_and_Scientist_CV.pdf", "rb") as f:
            st.download_button("📊 Data Analyst / Scientist CV", f, file_name="Ryan_Brown_Data_CV.pdf")
    except: 
        st.error("Data CV File Missing")
    
    # Sport CV
    try:
        with open("Sports Performance Analysis CV.pdf", "rb") as f:
            st.download_button("🏃 Sports Performance Analysis CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
    except: 
        st.error("Sport CV File Missing")

st.caption("Built by Ryan Brown | © 2026 | Christchurch, Bournemouth (UK)")
