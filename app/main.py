import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📄 AI Resume Analyzer")
st.markdown("""
Welcome to the **AI Resume Analyzer** — an NLP-powered tool that parses your resume,
scores it against real job profiles, identifies skill gaps, and recommends learning resources.

---
### How to use:
1. Go to **Analyze Resume** in the sidebar — upload your resume (PDF or DOCX)
2. Select a **target job profile** to benchmark against
3. View your **score, skill gaps, and course recommendations**
4. Explore **Insights** for analytics across submissions
""")

st.info("👈 Use the sidebar to navigate between pages.")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Supported Formats", "PDF & DOCX")
with col2:
    st.metric("Job Profiles", "10+")
with col3:
    st.metric("Skill Categories", "8")
