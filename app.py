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
    .cv-desc { font-size: 12px; color: #666; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists("ryan_photo.jpg"):
        st.image("ryan_photo.jpg", use_container_width=True)
    else:
        st.info("📷 Upload 'ryan_photo.jpg' to GitHub")
        
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
    st.markdown("**Data Science & Business**")
    st.markdown('<p class="cv-desc">Targeted at Data Analyst & BI roles.</p>', unsafe_allow_html=True)
    try:
        with open("CV_Data.pdf", "rb") as f:
            st.download_button("📊 Download Data CV", f, file_name="Ryan_Brown_Data_CV.pdf")
    except:
        st.warning("Upload 'CV_Data.pdf'")

    st.write("") 

    # SPORT CV
    st.markdown("**Sports Performance**")
    st.markdown('<p class="cv-desc">Targeted at Elite Sport & Academy roles.</p>', unsafe_allow_html=True)
    try:
        with open("CV_Sport.pdf", "rb") as f:
            st.download_button("🏃 Download Sport CV", f, file_name="Ryan_Brown_Sport_CV.pdf")
    except:
        st.warning("Upload 'CV_Sport.pdf'")

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
    ["Statistical Modeling", "Z-Score Analysis", "R"]
]
for i, col in enumerate(cols):
    for skill in skills[i]:
        col.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 The Hub (Python)", "📊 Power BI Dashboards", "🎥 Video Analysis & BOS", "👨‍💻 About Me"])

with tab1:
    st.header("Multi-Disciplinary Intelligence Hub")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.write("""
        **The Challenge:** High-performance data (GPS, Wellness, Medical) was siloed across different platforms.
        
        **The Solution:** I developed a Python-based ecosystem that:
        - Ingests disparate datasets automatically.
        - Calculates **Z-Scores** and **ACWR** to flag injury risks.
        - Translates raw data into 'Smart Recommendations' for MDT staff.
        """)
        st.code("# Logic for Athlete Flagging\nif readiness_score < threshold:\n    st.warning('Flag for MDT Review')", language='python')
    
    with col2:
        # VIDEO 1: THE HUB
        st.video("https://youtu.be/_AYWoKyvQTo") 

with tab2:
    st.header("Performance Readiness Dashboards")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # VIDEO 2: POWER BI
        st.video("https://youtu.be/oGp9sHEOP0U")
    with col2:
        st.write("""
        **Visualizing the Story:**
        Interactive Power BI dashboards designed to track longitudinal fatigue and workload trends.
        
        **Key Features:**
        - Post-event tactical debriefs for **BU Men’s 2nd Football Team**.
        - Data-driven case studies for senior directors.
        - Integration of technical findings into clear, concise coaching feedback.
        """)

with tab3:
    st.header("Tactical Workflow & National Rankings")
    
    # Top Section: Dissertation / Hudl
    st.subheader("Hudl Sportscode: Tactical Workflow Design")
    c1, c2 = st.columns([1, 1])
    with c1:
        if os.path.exists("images/hudl_window.png"):
            st.image("images/hudl_window.png", caption="Dissertation: Custom Football Coding Window")
        else:
            st.info("📷 Upload 'hudl_window.png' to images folder")
    with c2:
        st.write("""
        **Dissertation Focus:**
        Designed and justified a personalized performance analysis workflow aligned with coaching philosophy.
        - Conducted intra- and inter-rater reliability testing.
        - Translated tactical events into actionable performance markers.
        """)

    st.write("---")
    
    # Bottom Section: British Obstacle Sports
    st.subheader("British Obstacle Sports (BOS) Ranking System")
    col_v, col_t = st.columns([1.2, 1])
    with col_v:
        # VIDEO 3: BOS / RANKINGS
        st.video("https://youtu.be/2pnC_YBjekI")
    with col_t:
        st.write("""
        **Standardizing National Data:**
        Collaborated with the UK governing body to clean disparate race results and create a unified national ranking system.
        - Managed large-scale competition datasets.
        - Published interactive leaderboards for athlete standings.
        """)

with tab4:
    st.header("The Human Side of Data")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.write("""
        I’ve lived in Bournemouth my whole life and have always been driven by competition. Whether it's playing football, 
        training in the gym, or trying my hand at pickleball, I'm fascinated by the "why" behind performance.
        
        **The Hybrid Analyst:**
        My Master's at Bournemouth University was the turning point. I realized that my passion for sport and my analytical mindset were the same thing. 
        I don't just want to provide numbers; I want to provide answers.
        
        I treat business data with the same scrutiny as an elite athlete's GPS profile—looking for the 1% gains that drive success.
        """)
    with col_b:
        st.info("""
        **Quick Facts:**
        - ⚽ **Celtic FC Fan**
        - 🎓 **MSc Sports Performance Analysis**
        - 🎾 **Football, Tennis & Pickleball**
        - 🛠️ **Tools:** Python, SQL, Power BI, Sportscode
        """)

# --- FOOTER ---
st.write("---")
st.caption("Built by Ryan Brown | © 2026 Performance Data Portfolio")
