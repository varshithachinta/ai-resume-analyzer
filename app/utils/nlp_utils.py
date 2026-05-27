import re
from typing import List, Dict

# Comprehensive skill keyword bank
SKILL_BANK = {
    "programming_languages": [
        "python", "javascript", "java", "c++", "c", "sql", "r", "typescript",
        "go", "rust", "scala", "kotlin", "swift", "php", "ruby", "matlab"
    ],
    "ml_ai": [
        "machine learning", "deep learning", "neural network", "nlp",
        "natural language processing", "computer vision", "tensorflow", "keras",
        "pytorch", "scikit-learn", "sklearn", "xgboost", "lightgbm", "bert",
        "transformers", "hugging face", "opencv", "yolo", "cnn", "rnn", "lstm",
        "random forest", "logistic regression", "svm", "clustering", "k-means",
        "feature engineering", "model training", "hyperparameter tuning",
        "pandas", "numpy", "matplotlib", "seaborn", "scipy"
    ],
    "web_development": [
        "html", "css", "react", "next.js", "angular", "vue", "node.js",
        "express", "flask", "fastapi", "django", "rest api", "graphql",
        "streamlit", "bootstrap", "tailwind", "jquery", "ajax"
    ],
    "databases": [
        "mysql", "postgresql", "sqlite", "mongodb", "redis", "elasticsearch",
        "sql", "nosql", "database design", "orm", "sqlalchemy"
    ],
    "cloud_devops": [
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
        "ci/cd", "git", "github", "linux", "bash", "terraform", "jenkins",
        "github actions", "heroku", "vercel", "railway", "render"
    ],
    "data_tools": [
        "jupyter", "tableau", "power bi", "excel", "bigquery", "spark",
        "hadoop", "airflow", "dbt", "looker", "data visualization"
    ],
    "soft_skills": [
        "leadership", "communication", "teamwork", "problem solving",
        "project management", "agile", "scrum", "mentoring"
    ],
    "other": [
        "api", "microservices", "system design", "algorithms", "data structures",
        "object oriented", "functional programming", "testing", "unit testing"
    ]
}

def extract_text_chunks(text: str) -> Dict[str, str]:
    """
    Split resume text into logical sections.
    Returns dict with section names as keys.
    """
    sections = {}
    text_lower = text.lower()

    section_patterns = {
        "education": r"(education|academic|qualification)",
        "experience": r"(experience|work|employment|internship)",
        "skills": r"(skill|technical|competenc)",
        "projects": r"(project|portfolio|work sample)",
        "achievements": r"(achievement|award|honor|certification|cert)"
    }

    lines = text.split("\n")
    current_section = "general"
    sections[current_section] = []

    for line in lines:
        line_lower = line.lower().strip()
        matched = False
        for section_name, pattern in section_patterns.items():
            if re.search(pattern, line_lower) and len(line.strip()) < 40:
                current_section = section_name
                sections[current_section] = []
                matched = True
                break
        if not matched:
            sections.setdefault(current_section, []).append(line)

    return {k: "\n".join(v) for k, v in sections.items()}


def extract_skills(text: str) -> Dict[str, List[str]]:
    """
    Extract skills from resume text using keyword matching.
    Returns dict of category -> list of found skills.
    """
    text_lower = text.lower()
    found = {}

    for category, keywords in SKILL_BANK.items():
        matched = []
        for kw in keywords:
            # match whole word or phrase
            pattern = r'\b' + re.escape(kw) + r'\b'
            if re.search(pattern, text_lower):
                matched.append(kw)
        if matched:
            found[category] = matched

    return found


def extract_email(text: str) -> str:
    match = re.search(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}', text)
    return match.group(0) if match else "Not found"


def extract_phone(text: str) -> str:
    match = re.search(r'(\+?\d[\d\s\-]{8,13}\d)', text)
    return match.group(0).strip() if match else "Not found"


def extract_name_heuristic(text: str) -> str:
    """
    Heuristic: assume name is in first 3 non-empty lines.
    """
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    for line in lines[:3]:
        # Name lines are usually short and contain only letters/spaces
        if re.match(r'^[A-Za-z ]{3,40}$', line):
            return line
    return "Not detected"


def extract_years_of_experience(text: str) -> int:
    """
    Try to extract years of experience from text.
    """
    patterns = [
        r'(\d+)\+?\s*years?\s*of\s*experience',
        r'(\d+)\+?\s*years?\s*experience',
        r'experience\s*of\s*(\d+)\+?\s*years?'
    ]
    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return int(match.group(1))
    return 0


def count_action_verbs(text: str) -> int:
    """
    Count strong action verbs — signals good resume writing.
    """
    action_verbs = [
        "built", "developed", "designed", "implemented", "deployed",
        "optimized", "improved", "created", "led", "managed", "analyzed",
        "trained", "published", "achieved", "delivered", "automated",
        "collaborated", "engineered", "researched", "contributed"
    ]
    text_lower = text.lower()
    return sum(1 for v in action_verbs if v in text_lower)
