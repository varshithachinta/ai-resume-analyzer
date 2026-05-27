"""
Job profiles defining required skills for each role.
Each profile has: required_skills, bonus_skills, weight_by_category
"""

JOB_PROFILES = {
    "Machine Learning Engineer": {
        "description": "Build and deploy ML models at scale. Focus on model development, MLOps, and production systems.",
        "required_skills": [
            "python", "machine learning", "deep learning", "scikit-learn",
            "tensorflow", "pytorch", "pandas", "numpy", "sql", "git"
        ],
        "bonus_skills": [
            "mlops", "docker", "kubernetes", "spark", "feature engineering",
            "xgboost", "lightgbm", "hyperparameter tuning", "bert", "nlp"
        ],
        "weight": {
            "ml_ai": 0.45,
            "programming_languages": 0.20,
            "data_tools": 0.15,
            "cloud_devops": 0.10,
            "databases": 0.05,
            "other": 0.05
        }
    },
    "Data Scientist": {
        "description": "Analyze complex data, build predictive models, and communicate insights to stakeholders.",
        "required_skills": [
            "python", "machine learning", "pandas", "numpy", "matplotlib",
            "sql", "statistics", "scikit-learn", "jupyter"
        ],
        "bonus_skills": [
            "r", "tableau", "power bi", "deep learning", "nlp",
            "feature engineering", "a/b testing", "seaborn", "scipy"
        ],
        "weight": {
            "ml_ai": 0.40,
            "programming_languages": 0.20,
            "data_tools": 0.20,
            "databases": 0.10,
            "cloud_devops": 0.05,
            "other": 0.05
        }
    },
    "Full Stack Developer": {
        "description": "Build end-to-end web applications covering frontend UI, backend APIs, and database design.",
        "required_skills": [
            "javascript", "html", "css", "react", "node.js",
            "rest api", "sql", "git", "python"
        ],
        "bonus_skills": [
            "typescript", "next.js", "docker", "postgresql", "mongodb",
            "tailwind", "graphql", "aws", "ci/cd", "testing"
        ],
        "weight": {
            "web_development": 0.40,
            "programming_languages": 0.20,
            "databases": 0.15,
            "cloud_devops": 0.15,
            "other": 0.10
        }
    },
    "Backend Developer": {
        "description": "Design and build server-side applications, APIs, and database systems.",
        "required_skills": [
            "python", "sql", "rest api", "flask", "git",
            "postgresql", "mysql", "docker"
        ],
        "bonus_skills": [
            "fastapi", "django", "node.js", "redis", "microservices",
            "kubernetes", "aws", "system design", "ci/cd", "testing"
        ],
        "weight": {
            "programming_languages": 0.25,
            "web_development": 0.25,
            "databases": 0.20,
            "cloud_devops": 0.20,
            "other": 0.10
        }
    },
    "Data Analyst": {
        "description": "Transform raw data into actionable insights using analytics and visualization tools.",
        "required_skills": [
            "sql", "python", "excel", "pandas", "matplotlib",
            "data visualization", "jupyter"
        ],
        "bonus_skills": [
            "tableau", "power bi", "r", "seaborn", "bigquery",
            "looker", "statistical analysis", "a/b testing"
        ],
        "weight": {
            "data_tools": 0.35,
            "programming_languages": 0.25,
            "databases": 0.25,
            "ml_ai": 0.10,
            "other": 0.05
        }
    },
    "NLP Engineer": {
        "description": "Build language understanding systems, chatbots, and text processing pipelines.",
        "required_skills": [
            "python", "nlp", "natural language processing", "bert",
            "transformers", "scikit-learn", "pandas", "numpy"
        ],
        "bonus_skills": [
            "pytorch", "tensorflow", "hugging face", "spacy", "nltk",
            "text classification", "named entity recognition", "sentiment analysis",
            "llm", "gpt", "rest api"
        ],
        "weight": {
            "ml_ai": 0.55,
            "programming_languages": 0.20,
            "web_development": 0.10,
            "cloud_devops": 0.10,
            "other": 0.05
        }
    },
    "Computer Vision Engineer": {
        "description": "Build image/video analysis systems using deep learning and classical CV techniques.",
        "required_skills": [
            "python", "opencv", "cnn", "deep learning", "tensorflow",
            "pytorch", "numpy", "computer vision"
        ],
        "bonus_skills": [
            "yolo", "object detection", "image segmentation", "keras",
            "hugging face", "cuda", "docker", "scikit-learn"
        ],
        "weight": {
            "ml_ai": 0.60,
            "programming_languages": 0.20,
            "cloud_devops": 0.10,
            "other": 0.10
        }
    },
    "Software Engineer (SDE)": {
        "description": "General software engineering role covering algorithms, system design, and full-stack development.",
        "required_skills": [
            "python", "java", "c++", "data structures", "algorithms",
            "sql", "git", "object oriented"
        ],
        "bonus_skills": [
            "system design", "docker", "kubernetes", "rest api",
            "testing", "agile", "ci/cd", "javascript", "linux"
        ],
        "weight": {
            "programming_languages": 0.30,
            "other": 0.25,
            "web_development": 0.15,
            "cloud_devops": 0.15,
            "databases": 0.15
        }
    },
    "ML Intern / Fresher": {
        "description": "Entry-level ML role. Recruiters look for strong fundamentals and project evidence.",
        "required_skills": [
            "python", "machine learning", "pandas", "numpy",
            "scikit-learn", "jupyter", "git"
        ],
        "bonus_skills": [
            "deep learning", "tensorflow", "pytorch", "sql", "matplotlib",
            "nlp", "feature engineering", "kaggle", "flask"
        ],
        "weight": {
            "ml_ai": 0.40,
            "programming_languages": 0.25,
            "data_tools": 0.20,
            "databases": 0.10,
            "other": 0.05
        }
    },
    "AI Research Assistant": {
        "description": "Research-oriented role requiring strong theoretical foundation and publication experience.",
        "required_skills": [
            "python", "deep learning", "pytorch", "tensorflow",
            "research", "nlp", "numpy", "machine learning"
        ],
        "bonus_skills": [
            "published paper", "latex", "bert", "transformers",
            "experiment tracking", "hugging face", "cuda", "statistics"
        ],
        "weight": {
            "ml_ai": 0.60,
            "programming_languages": 0.20,
            "other": 0.15,
            "cloud_devops": 0.05
        }
    }
}
