from job_matcher import run_job_matcher
from resume_analyser import analyze_resume
import json
import os

def view_career_history():
    import json
    import os

    filename = "career_history.json"

    if not os.path.exists(filename):
        print("No career history found yet.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        history_data = json.load(file)

    history = history_data.get("history", [])

    if not history:
        print("No career analyses saved yet.")
        return

    print("\n===== YOUR CAREER HISTORY =====")

    for i, record in enumerate(history, start=1):
        print(f"\nAnalysis {i}")
        print("Name:", record.get("Name", "Unknown"))
        print("Career:", record.get("Job", "Unknown"))
        print("Skills:", ", ".join(record.get("Skills", [])))
        print("Match:", record.get("Match Percentage", 0), "%")
        print("Missing skills:", ", ".join(
            record.get("Missing Skills", [])
        ))






def analyze_career():
    matched_skills = []
    missing_skills = []

matched_skills = []
missing_skills = []


if os.path.exists("data.json"): 
    with open("data.json", "r") as file:
        data = json.load(file)
else:
    data = {}

if os.path.exists("progress.json"):
    with open("progress.json","r") as file:
        progress = json.load(file)

else:
    progress = {"Completed skills": []}

if os.path.exists("skill_priority.json"):
    with open("skill_priority.json", "r") as file:
        skill_priority = json.load(file)

else:
    skill_priority = {}

if os.path.exists("roadmap.json"):
    with open("roadmap.json", "r") as file:
        roadmap = json.load(file)

else :
    roadmap = {}

if os.path.exists("jobs.json"):
    with open("jobs.json", "r") as file:
        jobs = json.load(file)
else:
    jobs = {}




Name = input("Enter your name: ")

skill = input("Enter your skills: ")


skill = skill.split(",")


skill = [s.strip().lower() for s in skill]



print("===== SELECT YOUR CAREER =====")

print('''
               1. AI Engineer
               2. Software Developer
               3. Data Scientist
               4. Web Developer
               5. Mobile App Developer
               6. Cybersecurity Analyst
               7. Cloud Solutions Architect
               8. DevOps Engineer
''')

choice = int(input("Enter your job: "))

job_list = list(jobs.keys())

if choice >= 1 and choice <= len(job_list):

    job = job_list[choice - 1]

    required_skills = jobs[job]




data["Name"] = Name
data["Skill"] = skill
data["Job"] = job

for required_skill in required_skills:

    if required_skill.lower() in skill:
        matched_skills.append(required_skill)

    else:
        missing_skills.append(required_skill)

match_percentage = (len(matched_skills) / len(required_skills)) * 100

history_file = "career_history.json"

if os.path.exists(history_file):
    with open(history_file, "r", encoding="utf-8") as file:
        history_data = json.load(file)
else:
    history_data = {"history": []}

record = {
    "Name": Name,
    "Job": job,
    "Skills": skill,
    "Match Percentage": round(match_percentage, 2),
    "Missing Skills": missing_skills.copy()
}

history_data["history"].append(record)

with open(history_file, "w", encoding="utf-8") as file:
    json.dump(history_data, file, indent=4)

print("Career analysis saved to history!")



with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data has been updated successfully.")

print("\nYour Name:", Name)
print("Your Skills:", skill)
print("Your Job:", job)
print("Required Skills:", required_skills)

topics = []
for missing_skill in missing_skills:
    if missing_skill in roadmap:
        topics.extend(roadmap[missing_skill])

print("\n----- CAREER ANALYSIS -----")

print("Name:", Name)
print("Job:", job)

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nJob Match:", round(match_percentage, 2), "%")

print("\nRecommended Skills to Learn:")

for i,skill_name in enumerate(missing_skills, start=1):
    print(f"{i}. {skill_name}")

if match_percentage == 100:
    print("\nYou have all the skills required for this job. You are eligible for this job.")

elif match_percentage >= 80:
    print("\n You have most of the skills required for this job. You are eligible for this job")

elif match_percentage >= 40:
    print("\n You have some of the skills required for this job. You need to learn more skills to be eligible for this job.")

elif match_percentage >= 10:
    print("\n You don't have most of the skills required for this job. You need to learn more skills to be eligible for this job.")


else:
    print("\n You don't have any of the skills required for this job. You need to learn more skills to be eligible for this job.")


print("\n----- LEARNING ROADMAP -----")

week = 1

for missing_skill in missing_skills:

    if missing_skill in roadmap:
        topic = roadmap[missing_skill]

    for topic in topics:
            print("Week", week, "→", topic)
            week += 1

print("\n===== SKILL PRIORITY =====")
for skill_name  in missing_skills:
    priority = skill_priority.get(skill_name, "Medium")
    print(skill_name, "→", priority, "priority")

print("\n===== PERSONALIZED LEARNING ROADMAP =====")
priority_order ={"High": 1,
                 "Medium": 2,
                 "Low": 3
                           }

sorted_skills = sorted(
    missing_skills,
    key=lambda skill: priority_order.get(
        skill_priority.get(skill, "Medium"), 2
    )
)

week = 1

for missing_skill in sorted_skills:

    priority = skill_priority.get(missing_skill, "Medium")

    print(f"\nWeek {week}: {missing_skill}")
    print("Priority:", priority)

    if missing_skill in roadmap:
        for topic in roadmap[missing_skill]:
            print("  →", topic)

    else:
        print("  No roadmap topics available yet.")

    week += 1

print("\n===== LEARNING PROGRESS TRACKER =====")
completed_skills = progress.get("Completed skills", [])
for skill_name in missing_skills:
    print(f"\nSkill: {skill_name}")
    answer = input("Have you completed this skill? (yes/no): ").strip().lower()
    

    if answer == "yes":
        if skill_name not in completed_skills:
            completed_skills.append(skill_name)
            print(f"Great! You have marked '{skill_name}' as completed.")

        else:
            print(f"{skill_name} is already marked as completed.")

with open("progress.json", "w", encoding="utf-8") as file:
    json.dump({"Completed skills": completed_skills}, file, indent=4)

progress = ("\n Progress saved successfully.")

total_skills = len(missing_skills)
completed_count = sum(
                1 for skill in missing_skills 
                if skill in completed_skills
                )
remaining_count = total_skills - completed_count
if total_skills > 0:
    progress_percentage = (
        completed_count / total_skills
    ) * 100
else:
    progress_percentage = 0

print("\n===== YOUR PROGRESS REPORT =====")
print("Total skills:", total_skills)
print("Completed skills:", completed_count)
print("Remaining skills:", remaining_count)
print("Progress:", round(progress_percentage, 2), "%")





report = f"""
===================================
       AI CAREER COPILOT
      CAREER READINESS REPORT
===================================

Name: {Name}
Selected Career: {job}




----- SKILL ANALYSIS -----
Total Required Skills: {len(required_skills)}
Matched Skills: {len(matched_skills)}
Missing Skills: {len(missing_skills)}
Skill Match: {round(match_percentage, 2)} %

----- LEARNING PROGRESS -----
Completed Skills: {completed_count}
Remaining Skills: {remaining_count}

----- SKILLS TO LEARN -----
"""

for skill_name in missing_skills:
    priority = skill_priority.get(skill_name, "Medium")
    report += f"{skill_name} - {priority} priority\n"

report += """
===================================
          REPORT COMPLETED
===================================
"""

print(report)
with open("career_report.txt", "w", encoding="utf-8") as file:
      file.write(report)

print("Career report saved to career_report.txt")

while True:
    print("\n===== AI CAREER COPILOT =====")
    print("1. Analyze Career Skills")
    print("2. View Career History")
    print("3. Match a Job Description")
    print("4. Analyze pdf Resume")
    print("5. Exit")
    

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        analyze_career()
    elif choice == "2":
        view_career_history()
    elif choice == "3":
        run_job_matcher()
    elif choice == "4":
        analyze_resume()
    elif choice == "5":
        print("Thank you for using AI Career Copilot!")
        break
    else:
        print("Invalid choice. Enter 1, 2, 3, 4, or 5.")