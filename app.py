import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ryan Brown | Data Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
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

# --- SIDEBAR ---
with st.sidebar:
    if os.path.exists("your_photo.jpg"):
        st.image("your_photo.jpg", width=200)
    else:
        st.info("📷 (Place your_photo.jpg in the directory)")
        
    st.title("Ryan Brown")
    st.markdown("📍 Christchurch, Bournemouth")
    st.markdown("📞 07934440537")
    st.markdown("✉️ [Ryanlarsson14@gmail.com](mailto:Ryanlarsson14@gmail.com)")
    
    st.write("---")
    st.markdown("### Socials")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/ryan-brown-data)")
    st.markdown("[💻 GitHub](https://github.com/ryanlarsson14-crypto)")
    
    st.write("---")
    # Proper Download Button logic
    try:
        with open("Your_CV_File.pdf", "rb") as f:
            st.download_button("📄 Download CV", f, file_name="Ryan_Brown_CV.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.warning("Please add 'Your_CV_File.pdf' to the folder.")

# --- MAIN HEADER ---
st.title("Data Analyst & Performance Specialist")
st.markdown("### *Bridging the gap between athletic performance and data-driven strategy.*")

# --- SKILLS SECTION ---
st.write("---")
cols = st.columns(4)
skills = [
    ["Python", "Pandas/NumPy", "Streamlit"],
    ["SQL", "Power BI", "Tableau"],
    ["Performance Analysis", "GPS Data", "Load Mgmt"],
    ["Statistical Modeling", "Data Cleaning", "R"]
]
for i, col in enumerate(cols):
    for skill in skills[i]:
        col.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🚀 The Hub (Python)", "📊 Power BI", "🏃 British Obstacle Sports", "👨‍💻 About Me"])

with tab1:
    st.header("Multi-Disciplinary Intelligence Hub")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("""
        **The Challenge:** High-performance athletes generate huge amounts of data across different silos (Catapult GPS, Wellness Surveys, Medical reports).
        
        **The Solution:** I developed a Python-based ecosystem using Streamlit that:
        - Ingests CSV/Excel exports automatically.
        - Calculates 'Z-Scores' for wellness to flag outliers.
        - Visualizes workload (ACWR) to prevent injury.
        
        **Impact:** Reduced data processing time for staff by ~80%.
        """)
        st.code("# Example Logic\nif acwr > 1.5:\n    st.warning('High Injury Risk Detected')", language='python')
    
    with col2:
        # Placeholder for your video or image
        st.info("Project Screenshot/Video Demo goes here")

with tab2:
    st.header("Performance Readiness Dashboards")
    st.write("Interactive Power BI dashboards designed to track athlete fatigue and workload trends.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://via.placeholder.com/600x400.png?text=Power+BI+Dashboard+1", caption="Athlete Fatigue Trends")
    with c2:
        st.image("https://via.placeholder.com/600x400.png?text=Power+BI+Dashboard+2", caption="Team Workload Comparison")

with tab3:
    st.header("British Obstacle Sports Ranking")
    st.write("""
    Collaborating with the UK governing body to standardize national competition data. 
    I focus on cleaning disparate race results and creating a unified Elo-style ranking system.
    """)
    st.markdown("- **Goal:** Fair national selection criteria.")
    st.markdown("- **Tools:** Python (Pandas), Google Sheets API.")

with tab4:
    st.header("The Human Side")
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.write("""
        I’ve lived in Bournemouth my whole life and am a firm believer in the 'healthy body, healthy mind' philosophy. 
        Whether it's football, the gym, or the growing world of pickleball, I'm always looking for a competitive edge.
        
        **The Transition to Data:**
        My Master's at Bournemouth University was the turning point. I realized that the same passion I have for 
        Celtic FC could be applied to analyzing why things happen on the pitch (and in the office). 
        I don't just want to provide numbers; I want to provide answers.
        """)
    with col_b:
        st.write("⚽ **Celtic FC Fan**")
        st.write("🎓 **Bournemouth University Alumni**")
        st.write("🎾 **Pickleball Enthusiast**")

# --- FOOTER ---
st.write("---")
st.caption("Built by Ryan Brown using Streamlit | 2024")
