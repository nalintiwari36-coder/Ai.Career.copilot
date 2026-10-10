
def match_job_description(user_skills, required_skills):
    user_skills = [
        skill.strip().lower()
        for skill in user_skills
    ]

    required_skills = [
        skill.strip().lower()
        for skill in required_skills
    ]

    matched = []
    missing = []

    for skill in required_skills:
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(required_skills) == 0:
        percentage = 0
    else:
        percentage = (
            len(matched) / len(required_skills)
        ) * 100

    return matched, missing, round(percentage, 2)


def run_job_matcher():
    print("\n===== JOB DESCRIPTION MATCHER =====")

    user_input = input(
        "Enter your skills separated by commas: "
    )

    job_input = input(
        "Enter required skills from the job description, "
        "separated by commas: "
    )

    user_skills = user_input.split(",")
    required_skills = job_input.split(",")

    matched, missing, percentage = match_job_description(
        user_skills, required_skills
    )

    print("\nMatched skills:", matched)
    print("Missing skills:", missing)
    print("Job match:", percentage, "%")

    print("\nSkills to learn next:")
    for skill in missing:
        print("-", skill)
