import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.resume_parser import parse_resume
from components.scorer import score_resume
from components.recommender import get_recommendations
from utils.nlp_utils import extract_name_heuristic, extract_email, extract_phone
from data.job_descriptions.profiles import JOB_PROFILES

st.set_page_config(page_title="Analyze Resume", page_icon="🔍", layout="wide")

st.title("🔍 Analyze Your Resume")
st.markdown("Upload your resume and select a target job profile to get your score and recommendations.")

# --- Sidebar: Job Profile Selection ---
st.sidebar.header("⚙️ Settings")
job_profile = st.sidebar.selectbox(
    "Select Target Job Profile",
    options=list(JOB_PROFILES.keys()),
    index=8  # defaults to ML Intern / Fresher
)

profile_info = JOB_PROFILES[job_profile]
st.sidebar.markdown(f"**{job_profile}**")
st.sidebar.caption(profile_info["description"])
st.sidebar.markdown("**Required skills:**")
st.sidebar.caption(", ".join(profile_info["required_skills"][:6]) + "...")

# --- Main: Upload ---
uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"],
    help="Only PDF and DOCX formats are supported."
)

if uploaded_file:
    with st.spinner("Parsing resume..."):
        resume_text = parse_resume(uploaded_file)

    if not resume_text or resume_text.startswith("Error") or resume_text.startswith("Could not"):
        st.error(f"Failed to parse resume: {resume_text}")
        st.stop()

    if len(resume_text.strip()) < 50:
        st.warning("Resume text seems very short. Make sure your PDF is not image-based/scanned.")

    # --- Basic Info Extraction ---
    st.subheader("📋 Extracted Information")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = extract_name_heuristic(resume_text)
        st.metric("Name (detected)", name)
    with col2:
        email = extract_email(resume_text)
        st.metric("Email", email)
    with col3:
        phone = extract_phone(resume_text)
        st.metric("Phone", phone)

    st.divider()

    # --- Score ---
    with st.spinner("Analyzing resume..."):
        result = score_resume(resume_text, job_profile)

    if "error" in result:
        st.error(result["error"])
        st.stop()

    # --- Score Display ---
    st.subheader(f"📊 Score vs. {job_profile}")

    score = result["total_score"]
    grade = result["grade"]

    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        color = "#2ecc71" if score >= 70 else "#f39c12" if score >= 50 else "#e74c3c"
        st.markdown(f"""
        <div style='background:{color};padding:20px;border-radius:12px;text-align:center;'>
            <h1 style='color:white;margin:0;'>{score}</h1>
            <p style='color:white;margin:0;font-size:18px;'>/ 100</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style='background:#2c3e50;padding:20px;border-radius:12px;text-align:center;'>
            <h2 style='color:white;margin:0;'>{grade}</h2>
            <p style='color:#aaa;margin:0;'>Grade</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("**Feedback:**")
        for fb in result["feedback"]:
            st.markdown(fb)

    st.divider()

    # --- Skills Breakdown ---
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("✅ Matched Required Skills")
        if result["matched_required"]:
            for skill in result["matched_required"]:
                st.markdown(f"✅ `{skill}`")
        else:
            st.warning("No required skills matched — add them explicitly to your resume.")

    with col_right:
        st.subheader("❌ Missing Required Skills")
        if result["missing_required"]:
            for skill in result["missing_required"]:
                st.markdown(f"❌ `{skill}`")
        else:
            st.success("You have all required skills for this role!")

    st.divider()

    # --- Bonus Skills ---
    if result["matched_bonus"]:
        st.subheader("⭐ Bonus Skills Detected")
        bonus_cols = st.columns(4)
        for i, skill in enumerate(result["matched_bonus"]):
            bonus_cols[i % 4].markdown(f"⭐ `{skill}`")
        st.divider()

    # --- All Skills Found ---
    with st.expander("📂 All Skills Detected in Your Resume"):
        for category, skills in result["all_found_skills"].items():
            if skills:
                st.markdown(f"**{category.replace('_', ' ').title()}:** {', '.join(skills)}")

    st.divider()

    # --- Course Recommendations ---
    st.subheader("📚 Recommended Courses for Skill Gaps")
    recommendations = get_recommendations(result["missing_required"])

    if recommendations:
        for rec in recommendations:
            with st.container():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{rec['title']}**")
                    st.caption(f"Platform: {rec['platform']} | Level: {rec['level']} | For skill: `{rec['skill']}`")
                with col2:
                    st.link_button("View Course →", rec["url"])
                st.divider()
    else:
        st.info("No specific course recommendations — you have a strong skill match already!")

    # --- Raw Text (debug) ---
    with st.expander("🔎 Raw Extracted Resume Text (for debugging)"):
        st.text_area("Resume Text", resume_text, height=300)

else:
    st.info("👆 Upload your resume above to get started.")

    # Sample preview
    st.markdown("---")
    st.markdown("#### What you'll get:")
    cols = st.columns(3)
    with cols[0]:
        st.markdown("**📊 Resume Score**\nOut of 100, with grade (Excellent/Strong/Good/Fair)")
    with cols[1]:
        st.markdown("**🎯 Skill Gap Analysis**\nExact skills you're missing for your target role")
    with cols[2]:
        st.markdown("**📚 Course Recommendations**\nCurated Coursera/Udemy links to close your gaps")
