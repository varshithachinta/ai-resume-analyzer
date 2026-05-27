import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About AI Resume Analyzer")

st.markdown("""
## What is this?

**AI Resume Analyzer** is an NLP-powered tool that helps job seekers — especially freshers and students —
understand how well their resume matches a target job profile.

Unlike generic resume checkers, this tool:
- Parses the **actual text** of your resume (PDF or DOCX)
- Uses **keyword extraction** across 8 skill categories
- Benchmarks against **10+ real job profiles** (ML Engineer, Data Scientist, SDE, and more)
- Shows **exactly which skills you're missing** — not vague advice
- Recommends **specific courses** from Coursera, Udemy, NPTEL to close your gaps

---

## How the Scoring Works

| Component | Max Points | What it measures |
|-----------|-----------|-----------------|
| Required Skills Match | 60 | % of job's must-have skills in your resume |
| Bonus Skills | 20 | Nice-to-have skills that make you stand out |
| Action Verbs | 10 | Strong verbs like built, deployed, optimized |
| Content Richness | 10 | Resume detail and substance |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend / UI | Streamlit |
| Resume Parsing | PyMuPDF (PDF), python-docx (DOCX) |
| NLP / Skill Extraction | Regex-based keyword matching, custom skill bank |
| Scoring | Rule-based weighted scoring engine |
| Recommendations | Curated course database |
| Language | Python 3.10+ |

---

## Built by

**Varshitha Chinta** — Final year B.Tech CSE student, Andhra University.

- 🔗 [GitHub](https://github.com/varshithachinta)
- 💼 [LinkedIn](https://linkedin.com/in/varshithachinta)
""")
