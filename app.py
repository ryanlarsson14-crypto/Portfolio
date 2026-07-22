import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ryan Brown | Performance Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #0e3150;
        color: white;
        border: none;
    }
    .stButton>button:hover { background-color: #2e7bcf; color: white; }
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

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists("Ryan_Brown_Photo.jpeg"):
        st.image("Ryan_Brown_Photo.jpeg", use_container_width=True)
        
    st.title("Ryan Brown")
    st.markdown("📍 Christchurch, Bournemouth")
    st.markdown("📞 07934440537")
    st.markdown("✉️ [Ryanlarsson14@gmail.com](mailto:Ryanlarsson14@gmail.com)")
    
    st.write("---")
    st.markdown("### Socials")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/ryan-brown-data)")
    st.markdown("[💻 GitHub](https://github.com/ryanlarsson14-crypto)")
    
    st.write("---")
    st.subheader("Download My CV")
    
    # DATA CV
    try:
        with open("Data_Analyst_and_Scientist_CV.pdf", "rb") as f:
            st.download_button("📊 Download Data CV", f, file_name="Ryan_Brown_Data_CV.pdf")
    except:
        st.warning("Data CV file not found.")

    # SPORT CV
    try:
        with open("Sports Performance Analysis CV.pdf", "rb") as f:
            st.download_button("🏃 Download Sport CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
    except:
        st.warning("Sport CV file not found.")

# --- MAIN HEADER ---
st.title("Performance Analyst & Data Scientist")
st.markdown("### *Bridging the gap between athletic performance and data-driven strategy.*")

# --- SKILLS SECTION ---
st.write("---")
cols = st.columns(4)
skills = [
    ["Python (Pandas)", "Streamlit", "SQL"],
    ["Power BI (DAX)", "Tableau", "Excel VBA"],
    ["Hudl Sportscode", "GPS Load Mgmt", "ACWR"],
    ["Statistical Modeling", "Z-Score Analysis", "Machine Learning"]
]
for i, col in enumerate(cols):
    for skill in skills[i]:
        col.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 The Hub (Python)", "📊 Power BI Dashboards", "🎥 Video Analysis & BOS", "👨‍💻 About Me"])

with tab1:
    st.header("The Data Pipeline: From Raw to Refined")
    st.write("A demonstration of my automated cleaning process for high-performance datasets.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 1. Unclean Data")
        if os.path.exists("images/Unclean Data.png"):
            st.image("images/Unclean Data.png", caption="Raw, disorganized athlete data.")
        
    with col2:
        st.markdown("### 2. The Python Solution")
        if os.path.exists("images/Cleaning Function.png"):
            st.image("images/Cleaning Function.png", caption="My custom script to automate ETL.")

    with col3:
        st.markdown("### 3. Clean Output")
        if os.path.exists("images/Clean Data.png"):
            st.image("images/Clean Data.png", caption="Standardized data ready for analysis.")

    st.write("---")
    st.subheader("Project Demo")
    # HUB VIDEO
    st.video("https://youtu.be/_AYWoKyvQTo")

with tab2:
    st.header("Performance Readiness Dashboards")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # POWER BI VIDEO
        st.video("https://youtu.be/oGp9sHEOP0U")
    with col2:
        st.write("""
        **Visualizing the Story:**
        - Interactive Power BI dashboards tracking fatigue and workload trends.
        - Calculated **ACWR** to predict and prevent injury.
        - Strategic debriefs for **BU Men’s 2nd Football Team**.
        """)

with tab3:
    st.header("Tactical Workflow & National Rankings")
    
    st.subheader("Hudl Sportscode: Tactical Workflow Design")
    c1, c2 = st.columns([1.5, 1])
    with c1:
        if os.path.exists("images/Code Window.png"):
            st.image("images/Code Window.png", caption="Dissertation: Custom Football Coding Window")
    with c2:
        st.write("""
        **Dissertation Focus:**
        - Designed a personalized performance analysis workflow.
        - Translated tactical events into actionable performance markers (WITTW model).
        """)

    st.write("---")
    st.subheader("British Obstacle Sports (BOS) Ranking System")
    # RANKINGS VIDEO
    st.video("https://youtu.be/2pnC_YBjekI")

with tab4:
    st.header("The Human Side of Data")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.write("""
        I’ve lived in Bournemouth my whole life and am fascinated by the "why" behind performance. 
        My Master's at Bournemouth University allowed me to weaponize sporting passion with Python and SQL. 
        
        I don't just provide numbers; I provide answers. I treat business data with the same scrutiny as an elite athlete's GPS profile.
        """)
    with col_b:
        st.info("""
        - ⚽ **Celtic FC Fan**
        - 🎓 **MSc Sports Performance Analysis**
        - 🎾 **Football, Tennis & Pickleball**
        """)

# --- FOOTER ---
st.write("---")
st.caption("Built by Ryan Brown | © 2026")
