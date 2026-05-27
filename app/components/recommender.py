from typing import List, Dict

# Course recommendations mapped to skills
COURSE_RECOMMENDATIONS = {
    "machine learning": {
        "title": "Machine Learning Specialization",
        "platform": "Coursera (Andrew Ng)",
        "url": "https://www.coursera.org/specializations/machine-learning-introduction",
        "level": "Beginner–Intermediate"
    },
    "deep learning": {
        "title": "Deep Learning Specialization",
        "platform": "Coursera (deeplearning.ai)",
        "url": "https://www.coursera.org/specializations/deep-learning",
        "level": "Intermediate"
    },
    "python": {
        "title": "Python for Everybody",
        "platform": "Coursera (University of Michigan)",
        "url": "https://www.coursera.org/specializations/python",
        "level": "Beginner"
    },
    "sql": {
        "title": "SQL for Data Science",
        "platform": "Coursera (UC Davis)",
        "url": "https://www.coursera.org/learn/sql-for-data-science",
        "level": "Beginner"
    },
    "nlp": {
        "title": "Natural Language Processing Specialization",
        "platform": "Coursera (deeplearning.ai)",
        "url": "https://www.coursera.org/specializations/natural-language-processing",
        "level": "Intermediate"
    },
    "natural language processing": {
        "title": "Natural Language Processing Specialization",
        "platform": "Coursera (deeplearning.ai)",
        "url": "https://www.coursera.org/specializations/natural-language-processing",
        "level": "Intermediate"
    },
    "docker": {
        "title": "Docker & Kubernetes: The Practical Guide",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/docker-kubernetes-the-practical-guide/",
        "level": "Intermediate"
    },
    "react": {
        "title": "The Complete React Developer Course",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/react-2nd-edition/",
        "level": "Beginner–Intermediate"
    },
    "tensorflow": {
        "title": "TensorFlow Developer Professional Certificate",
        "platform": "Coursera (deeplearning.ai)",
        "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
        "level": "Intermediate"
    },
    "pytorch": {
        "title": "PyTorch for Deep Learning Bootcamp",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/pytorch-for-deep-learning-in-python-bootcamp/",
        "level": "Intermediate"
    },
    "aws": {
        "title": "AWS Certified Cloud Practitioner",
        "platform": "AWS Training",
        "url": "https://aws.amazon.com/training/learn-about/cloud-practitioner/",
        "level": "Beginner"
    },
    "data structures": {
        "title": "Data Structures and Algorithms — NPTEL",
        "platform": "NPTEL (IIT)",
        "url": "https://nptel.ac.in/courses/106102064",
        "level": "Intermediate"
    },
    "algorithms": {
        "title": "Algorithms Specialization",
        "platform": "Coursera (Stanford)",
        "url": "https://www.coursera.org/specializations/algorithms",
        "level": "Intermediate"
    },
    "system design": {
        "title": "Grokking the System Design Interview",
        "platform": "Educative.io",
        "url": "https://www.educative.io/courses/grokking-the-system-design-interview",
        "level": "Advanced"
    },
    "tableau": {
        "title": "Tableau 2024 A-Z: Hands-On Tableau Training",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/tableu/",
        "level": "Beginner"
    },
    "power bi": {
        "title": "Microsoft Power BI Desktop for Business Intelligence",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/",
        "level": "Beginner"
    },
    "kubernetes": {
        "title": "Kubernetes for the Absolute Beginners",
        "platform": "Udemy",
        "url": "https://www.udemy.com/course/learn-kubernetes/",
        "level": "Beginner"
    },
    "bert": {
        "title": "Hugging Face NLP Course",
        "platform": "Hugging Face (Free)",
        "url": "https://huggingface.co/learn/nlp-course",
        "level": "Intermediate"
    },
    "transformers": {
        "title": "Hugging Face NLP Course",
        "platform": "Hugging Face (Free)",
        "url": "https://huggingface.co/learn/nlp-course",
        "level": "Intermediate"
    }
}

def get_recommendations(missing_skills: List[str]) -> List[Dict]:
    """
    Return course recommendations for missing skills.
    """
    recommendations = []
    seen_titles = set()

    for skill in missing_skills:
        skill_lower = skill.lower()
        if skill_lower in COURSE_RECOMMENDATIONS:
            course = COURSE_RECOMMENDATIONS[skill_lower]
            if course["title"] not in seen_titles:
                recommendations.append({
                    "skill": skill,
                    **course
                })
                seen_titles.add(course["title"])

    return recommendations
