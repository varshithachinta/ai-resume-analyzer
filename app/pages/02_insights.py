import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.job_descriptions.profiles import JOB_PROFILES

st.set_page_config(page_title="Insights", page_icon="📈", layout="wide")

st.title("📈 Market Insights")
st.markdown("Explore skill demand across different job profiles to understand what the market is looking for.")

# --- Skill demand across profiles ---
st.subheader("🔥 Most In-Demand Skills by Role")

selected_roles = st.multiselect(
    "Select job profiles to compare",
    options=list(JOB_PROFILES.keys()),
    default=["Machine Learning Engineer", "Data Scientist", "Full Stack Developer"]
)

if selected_roles:
    # Build comparison table
    all_skills = set()
    for role in selected_roles:
        all_skills.update(JOB_PROFILES[role]["required_skills"])

    st.markdown("#### Required Skills Comparison")
    cols = st.columns(len(selected_roles))

    for i, role in enumerate(selected_roles):
        with cols[i]:
            st.markdown(f"**{role}**")
            for skill in JOB_PROFILES[role]["required_skills"]:
                st.markdown(f"• `{skill}`")

    st.divider()

    st.subheader("⭐ Bonus Skills That Set You Apart")
    b_cols = st.columns(len(selected_roles))
    for i, role in enumerate(selected_roles):
        with b_cols[i]:
            st.markdown(f"**{role}**")
            for skill in JOB_PROFILES[role]["bonus_skills"][:6]:
                st.markdown(f"• `{skill}`")

st.divider()

# --- Skills that appear in multiple roles ---
st.subheader("🌐 Universal Skills (appear across most roles)")
skill_frequency = {}
for role, profile in JOB_PROFILES.items():
    for skill in profile["required_skills"]:
        skill_frequency[skill] = skill_frequency.get(skill, 0) + 1

# Sort by frequency
sorted_skills = sorted(skill_frequency.items(), key=lambda x: x[1], reverse=True)
top_universal = [(s, c) for s, c in sorted_skills if c >= 3]

if top_universal:
    cols = st.columns(4)
    for i, (skill, count) in enumerate(top_universal[:12]):
        cols[i % 4].metric(skill.title(), f"{count} roles")

st.divider()

st.subheader("💡 Career Path Guide for Freshers")

paths = {
    "If you know Python + ML basics": "→ Apply for: ML Intern, Data Scientist, AI Research Assistant",
    "If you know Python + Web (Flask/Django)": "→ Apply for: Backend Developer, Full Stack Developer",
    "If you know Python + NLP (spaCy/BERT)": "→ Apply for: NLP Engineer, ML Engineer",
    "If you know Python + OpenCV + CNN": "→ Apply for: Computer Vision Engineer, ML Engineer",
    "If you know SQL + Excel + Python": "→ Apply for: Data Analyst, Business Analyst"
}

for condition, advice in paths.items():
    st.markdown(f"**{condition}**")
    st.markdown(f"  {advice}")
    st.markdown("")
