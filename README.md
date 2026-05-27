# 📄 AI Resume Analyzer

An NLP-powered resume analysis tool that parses your resume, scores it against real job profiles, identifies skill gaps, and recommends courses to close them.

\[!\[Streamlit App](https://static.streamlit.io/badges/streamlit\_badge\_black\_white.svg)](https://ai-resume-analyzer-6wmrlgetny4zcvj8yvtvdc.streamlit.app)

\---

## 🚀 Live Demo

\[➡️ Try it live on Streamlit Cloud](https://ai-resume-analyzer-6wmrlgetny4zcvj8yvtvdc.streamlit.app)
*(Upload any PDF or DOCX resume — no signup needed)*

\---

## ✨ Features

|Feature|Description|
|-|-|
|📥 Resume Parsing|Supports PDF and DOCX formats via PyMuPDF and python-docx|
|🔍 Skill Extraction|Detects skills across 8 categories (ML/AI, Web Dev, Cloud, Databases, etc.)|
|📊 Resume Scoring|Scores 0–100 against 10+ job profiles with weighted rubric|
|🎯 Skill Gap Analysis|Shows exactly which required skills are missing|
|📚 Course Recommendations|Curated Coursera/Udemy/NPTEL links for missing skills|
|📈 Market Insights|Compare skill demand across multiple roles|

\---

## 🎯 Supported Job Profiles

* Machine Learning Engineer
* Data Scientist
* Full Stack Developer
* Backend Developer
* Data Analyst
* NLP Engineer
* Computer Vision Engineer
* Software Engineer (SDE)
* ML Intern / Fresher
* AI Research Assistant

\---

## 📊 How Scoring Works

|Component|Max Points|What It Measures|
|-|-|-|
|Required Skills Match|60|% of job's must-have skills found in resume|
|Bonus Skills|20|Nice-to-have skills that differentiate you|
|Action Verbs|10|Strong verbs: built, deployed, optimized, etc.|
|Content Richness|10|Resume detail and depth|

\---

## 🛠️ Tech Stack

|Layer|Technology|
|-|-|
|UI|Streamlit|
|PDF Parsing|PyMuPDF (fitz)|
|DOCX Parsing|python-docx|
|NLP|Regex + custom skill keyword bank|
|Scoring Engine|Weighted rule-based system|
|Language|Python 3.10+|

\---

## 📁 Project Structure

```
ai-resume-analyzer/
├── app/
│   ├── main.py                    # Entry point
│   ├── pages/
│   │   ├── 01\_analyze.py          # Resume upload \& analysis page
│   │   ├── 02\_insights.py         # Market insights \& skill comparison
│   │   └── 03\_about.py            # About page
│   ├── components/
│   │   ├── resume\_parser.py       # PDF \& DOCX text extraction
│   │   ├── scorer.py              # Resume scoring engine
│   │   └── recommender.py        # Course recommendation system
│   └── utils/
│       └── nlp\_utils.py           # Skill extraction, NLP helpers
├── data/
│   └── job\_descriptions/
│       └── profiles.py            # 10+ job profile definitions
├── .streamlit/
│   └── config.toml                # UI theme config
├── requirements.txt
├── .gitignore
└── README.md
```

\---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/varshithachinta/ai-resume-analyzer.git
cd ai-resume-analyzer

# 2. Create virtual environment
python -m venv venv
venv\\Scripts\\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app/main.py
```

Open `http://localhost:8501` in your browser.

\---

## 📸 Screenshots

*(Add screenshots after deploying)*

\---

## 🔮 Future Improvements

* \[ ] BERT-based semantic skill matching (beyond keyword matching)
* \[ ] MySQL backend to store and track submissions over time
* \[ ] Resume suggestions: auto-rewrite weak bullet points
* \[ ] ATS (Applicant Tracking System) simulation mode
* \[ ] Resume template generator

\---

## 👩‍💻 Author

**Varshitha Chinta**  
B.Tech CSE, Andhra University College of Engineering for Women  
ML Intern @ Kalam Dream Labs | Published Researcher | Cognizant × Aston Martin F1 Ideathon Winner

* 🔗 [GitHub](https://github.com/varshithachinta)
* 💼 [LinkedIn](https://linkedin.com/in/varshithachinta)
* 📧 varshithachinta444@gmail.com

