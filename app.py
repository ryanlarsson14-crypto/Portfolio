import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ryan Brown | Performance Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS (Enhanced for Professional Look) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    [data-testid="stSidebar"] { background-color: #0e1117; }
    .stRadio>div{ gap: 10px; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #0e3150;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #2e7bcf; border: 1px solid #white; }
    .project-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0e3150;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .skill-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 15px;
        background-color: #e1e4e8;
        color: #0366d6;
        font-weight: bold;
        margin: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("📌 Navigation")
    selection = st.radio("Go to:", ["About Me", "My Work", "Contact Details"])
    st.write("---")
    st.caption("Ryan Brown | Portfolio v2.0")

# --- SECTION 1: ABOUT ME ---
if selection == "About Me":
    st.title("👋 About Me")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        ### Performance Analyst & Data Scientist
        **Location:** Christchurch, Bournemouth (UK)
        
        I am a data-driven specialist focused on bridging the gap between raw athletic metrics and elite-level strategy. 
        With a background spanning high-performance team environments and national governing bodies, I transform complex 
        datasets into actionable tactical advantages.
        
        **Educational History:**
        *   **MSc Sports Performance Analysis** | Bournemouth University
        *   Specialized in automated ETL pipelines and tactical workflow design.
        
        **Previous Experience:**
        *   **BU Sport:** Delivered performance insights and workload management for university elite squads.
        *   **British Obstacle Sports (BOS):** Developed national ranking systems and data-driven competition structures.
        """)
    
    with col2:
        st.info("""
        **Hobbies & Interests**
        * ⚽ **Celtic FC Fan**
        * 🎾 **Football, Tennis & Pickleball**
        * 🐍 **Python Enthusiast**
        """)

# --- SECTION 2: MY WORK (With Slicer) ---
elif selection == "My Work":
    st.title("📂 Project Showcase")
    st.markdown("Select a project below to view the technical breakdown and results.")
    
    # THE SLICER
    project_choice = st.selectbox(
        "Select Project:", 
        [
            "Python - Data Cleaning", 
            "MDT Support Hub Website", 
            "Power BI Athlete Performance Dashboard", 
            "Internship Placement Power BI Leaderboard", 
            "Hudl Sportscode"
        ]
    )
    
    st.write("---")

    if project_choice == "Python - Data Cleaning":
        st.header("Python - Data Cleaning")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            **The Challenge:** Raw athlete data is often messy, inconsistent, and time-consuming to process manually.
            **The Solution:** I built an automated ETL (Extract, Load, Transform) pipeline using Python.
            
            *   **Tools:** Pandas, NumPy.
            *   **Outcome:** Reduced data processing time by 90%, ensuring clean data for immediate analysis.
            """)
        with col2:
            # Placeholder for Image/Video
            st.info("Please provide the image/video link for the Data Cleaning script.")
            # Example: st.image("images/cleaning_script.png")

    elif project_choice == "MDT Support Hub Website":
        st.header("MDT Support Hub Website")
        st.markdown("""
        **Project Overview:** A centralized hub for Multi-Disciplinary Teams (MDT) to access athlete data in real-time.
        
        *   **Key Features:** Automated reporting, injury tracking, and tactical databases.
        *   **Impact:** Streamlined communication between coaches, physios, and analysts.
        """)
        # Placeholder for Video
        st.info("Please provide the video demo for the MDT Support Hub.")

    elif project_choice == "Power BI Athlete Performance Dashboard":
        st.header("Power BI Athlete Performance Dashboard")
        st.markdown("""
        **Project Overview:** A comprehensive visual suite tracking ACWR (Acute:Chronic Workload Ratio) and fatigue markers.
        
        *   **Visuals:** Heatmaps, trend lines, and Z-score distribution.
        *   **Strategic Use:** Used to flag athletes at high risk of injury before sessions.
        """)
        # Placeholder for Video
        st.info("Please provide the video for the Power BI Dashboard.")

    elif project_choice == "Internship Placement Power BI Leaderboard":
        st.header("Internship Placement Power BI Leaderboard")
        st.markdown("""
        **Project Overview:** Developed during my placement to gamify performance and track developmental milestones.
        
        *   **Objective:** To increase athlete engagement and provide objective feedback on training standards.
        """)
        # Placeholder for Image/Video
        st.info("Please provide assets for the Internship Leaderboard.")

    elif project_choice == "Hudl Sportscode":
        st.header("Hudl Sportscode Tactical Workflow")
        st.markdown("""
        **Project Overview:** Custom coding window design for tactical analysis.
        
        *   **Methodology:** Integrated the WITTW (What It Takes To Win) model into a functional coding interface.
        *   **Outcome:** Enhanced the speed of post-match debriefs for coaching staff.
        """)
        # Placeholder for Image/Video
        st.info("Please provide the image/video for the Hudl Sportscode workflow.")

# --- SECTION 3: CONTACT DETAILS ---
elif selection == "Contact Details":
    st.title("✉️ Contact & Documentation")
    
    st.markdown("### Ryan Brown")
    st.markdown("**Email:** [Ryanlarsson14@gmail.com](mailto:Ryanlarsson14@gmail.com)")
    st.markdown("**LinkedIn:** [linkedin.com/in/ryan-brown-data](https://www.linkedin.com/in/ryan-brown-data)")
    
    st.write("---")
    st.subheader("Curriculum Vitae")
    
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("#### Data Analysis Focus")
        try:
            with open("Data_Analyst_and_Scientist_CV.pdf", "rb") as f:
                st.download_button("📂 Download Data Analyst / Scientist CV", f, file_name="Ryan_Brown_Data_CV.pdf")
        except:
            st.error("Data CV file not found. Please ensure the filename matches exactly.")

    with c2:
        st.markdown("#### Sports Performance Focus")
        try:
            with open("Sports Performance Analysis CV.pdf", "rb") as f:
                st.download_button("🏃 Download Sports Performance Analysis CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
        except:
            st.error("Sports CV file not found. Please ensure the filename matches exactly.")

# --- FOOTER ---
st.write("---")
st.caption("Built by Ryan Brown | © 2026 | Christchurch, Bournemouth")
