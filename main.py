import json
import os



matched_skills = []
missing_skills = []


if os.path.exists("data.json"): 
    with open("data.json", "r") as file:
        data = json.load(file)
else:
    data = {}

if os.path.exists("skill_priority.json"):
    with open("skill_priority.json", "r") as file:
        roadmap = json.load(file)

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
    
