from typing import Dict, List, Tuple
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.nlp_utils import extract_skills, count_action_verbs, extract_years_of_experience
from data.job_descriptions.profiles import JOB_PROFILES


def score_resume(resume_text: str, job_profile_name: str) -> Dict:
    """
    Score a resume against a selected job profile.

    Returns a dict with:
    - total_score (0-100)
    - category_scores
    - matched_required
    - missing_required
    - matched_bonus
    - skill_gap
    - strengths
    - feedback
    """
    profile = JOB_PROFILES.get(job_profile_name)
    if not profile:
        return {"error": f"Job profile '{job_profile_name}' not found."}

    # Extract skills from resume
    found_skills = extract_skills(resume_text)
    all_found = []
    for skills_list in found_skills.values():
        all_found.extend(skills_list)
    all_found_lower = [s.lower() for s in all_found]

    # Check required skills
    required = profile["required_skills"]
    matched_required = [s for s in required if s.lower() in all_found_lower]
    missing_required = [s for s in required if s.lower() not in all_found_lower]

    # Check bonus skills
    bonus = profile["bonus_skills"]
    matched_bonus = [s for s in bonus if s.lower() in all_found_lower]

    # Base score: required skills coverage (60 points max)
    required_score = (len(matched_required) / len(required)) * 60 if required else 0

    # Bonus score: bonus skills (20 points max)
    bonus_score = min((len(matched_bonus) / max(len(bonus), 1)) * 20, 20)

    # Action verbs score (10 points max)
    action_count = count_action_verbs(resume_text)
    action_score = min(action_count * 1.5, 10)

    # Resume length / content richness (10 points max)
    word_count = len(resume_text.split())
    length_score = min((word_count / 400) * 10, 10)

    total_score = required_score + bonus_score + action_score + length_score
    total_score = round(min(total_score, 100), 1)

    # Category-level breakdown
    weights = profile.get("weight", {})
    category_scores = {}
    for cat, weight in weights.items():
        cat_skills = found_skills.get(cat, [])
        cat_score = min(len(cat_skills) * 8, 100) * weight
        category_scores[cat] = round(cat_score, 1)

    # Strengths: categories where user has 3+ skills
    strengths = [cat for cat, skills in found_skills.items() if len(skills) >= 3]

    # Skill gap: required skills missing
    skill_gap = missing_required

    # Feedback messages
    feedback = _generate_feedback(
        total_score, matched_required, missing_required,
        matched_bonus, action_count, word_count
    )

    return {
        "total_score": total_score,
        "grade": _score_to_grade(total_score),
        "category_scores": category_scores,
        "matched_required": matched_required,
        "missing_required": missing_required,
        "matched_bonus": matched_bonus,
        "skill_gap": skill_gap,
        "strengths": strengths,
        "all_found_skills": found_skills,
        "feedback": feedback,
        "action_verbs_count": action_count,
        "word_count": word_count
    }


def _score_to_grade(score: float) -> str:
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Strong"
    elif score >= 55:
        return "Good"
    elif score >= 40:
        return "Fair"
    else:
        return "Needs Improvement"


def _generate_feedback(score, matched_req, missing_req, matched_bonus, action_count, word_count) -> List[str]:
    feedback = []

    if len(matched_req) == 0:
        feedback.append("⚠️ No required skills matched. Make sure your resume explicitly mentions your technical skills.")
    elif len(missing_req) == 0:
        feedback.append("✅ You have all required skills for this role — excellent match!")
    else:
        feedback.append(f"✅ You matched {len(matched_req)} of {len(matched_req)+len(missing_req)} required skills.")

    if missing_req:
        top_missing = missing_req[:3]
        feedback.append(f"📌 Top skills to add: {', '.join(top_missing)}")

    if action_count < 5:
        feedback.append("💡 Use more action verbs (built, developed, optimized, deployed) to strengthen your resume.")
    else:
        feedback.append(f"✅ Good use of action verbs — {action_count} detected.")

    if word_count < 200:
        feedback.append("📝 Your resume seems short. Add more detail about your projects and experience.")
    elif word_count > 800:
        feedback.append("📝 Consider keeping your resume concise — under 600 words is ideal for freshers.")

    if len(matched_bonus) >= 3:
        feedback.append(f"⭐ Bonus: You also have {len(matched_bonus)} nice-to-have skills for this role.")

    return feedback
