def match_skills(resume_skills: list[str], job_skills: list[str]) -> dict:

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    # Skills found in both resume and job
    matched_skills = sorted(resume_set.intersection(job_set))

    # Required by job but missing from resume
    missing_skills = sorted(job_set.difference(resume_set))

    # Present in resume but not required by job
    extra_skills = sorted(resume_set.difference(job_set))

    match_percentage = (len(matched_skills) / len(job_set)) * 100
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
        "match_percentage": round(match_percentage, 2)}