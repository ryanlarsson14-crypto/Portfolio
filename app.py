import streamlit as st
import os

# --- MEDIA SETTINGS (PASTE YOUR YOUTUBE LINKS HERE) ---
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

project_choice = st.selectbox(
    "Choose a project to view details:", 
    ["Python - Data Cleaning", "MDT Support Hub Website", "Power BI Athlete Performance Dashboard", "Internship Placement Power BI Leaderboard", "Hudl Sportscode"]
)

st.markdown(f"### {project_choice}")

if project_choice == "Python - Data Cleaning":
    st.write("""
    Built an automated Python workflow to clean, merge, and process weekly performance data. 
    This pipeline integrates **S&C, physiology, medical, and coaching datasets** into a unified structure, 
    reducing manual processing time and ensuring data integrity through automated quality control.
    """)
    
    # Workflow Presentation
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("##### 1. Raw / Unclean Data")
        if os.path.exists("Unclean Data.png"): st.image("Unclean Data.png")
        
        st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)
        
        st.markdown("##### 2. The Python Cleaning Function")
        if os.path.exists("Cleaning Function.png"): st.image("Cleaning Function.png")
        
        st.markdown('<div class="arrow">⬇️</div>', unsafe_allow_html=True)
        
        st.markdown("##### 3. Standardized Clean Output")
        if os.path.exists("Clean Data.png"): st.image("Clean Data.png")

elif project_choice == "MDT Support Hub Website":
    st.write("""
    Engineered a centralized, password-protected web application using **Streamlit** to serve as a 
    real-time decision-support hub for a Multi-Disciplinary Team (MDT). This system ingests pitch, gym, and 
    medical records to provide "Smart Recommendations" for athlete readiness.
    """)
    st.video(URL_MDT_HUB)

elif project_choice == "Power BI Athlete Performance Dashboard":
    st.write("""
    Designed a performance readiness dashboard tailored specifically for Sport Scientists. Using advanced 
    **DAX calculations**, this tool assesses six-week performance trends and highlights potential 
    injury concerns through interactive trend analysis and z-score distributions.
    """)
    st.video(URL_PBI_DASHBOARD)

elif project_choice == "Internship Placement Power BI Leaderboard":
    st.write("""
    Developed during my placement with **British Obstacle Sports** to gamify performance and track 
    developmental milestones. This project involved maintaining accuracy across multiple UK national 
    leagues and providing a visual platform for athlete standing and rankings.
    """)
    st.video(URL_LEADERBOARD)

elif project_choice == "Hudl Sportscode":
    st.write("""
    Designed a personalized performance analysis workflow in a professional football environment. 
    Based on the **"What It Takes To Win" (WITTW)** model, this custom code window allows for 
    rapid tactical event logging and immediate feedback for coaching staff.
    """)
    if os.path.exists("Code Window.png"):
        st.image("Code Window.png", caption="Custom Hudl Sportscode Window Design")

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
    try:
        with open("Data_Analyst_and_Scientist_CV.pdf", "rb") as f:
            st.download_button("📊 Data Analyst / Scientist CV", f, file_name="Ryan_Brown_Data_CV.pdf")
    except: st.error("Data CV File Missing")
    try:
        with open("Sports Performance Analysis CV.pdf", "rb") as f:
            st.download_button("🏃 Sports Performance Analysis CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
    except: st.error("Sport CV File Missing")

st.caption("Built by Ryan Brown | © 2026 | Christchurch, Bournemouth (UK)")
