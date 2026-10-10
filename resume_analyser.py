
from pypdf import PdfReader
import os

KNOWN_SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "data analysis",
    "excel",
    "communication",
    "git",
    "flask",
    "django"
]


def analyze_resume():
    print("\n===== PDF RESUME ANALYZER =====")

    pdf_path = input(
        "Enter the PDF resume path: "
    ).strip().strip('"')

    if not os.path.isfile(pdf_path):
        print("File not found. Please check the path.")
        return

    if not pdf_path.lower().endswith(".pdf"):
        print("Please select a PDF file.")
        return

    try:
        reader = PdfReader(pdf_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            print(
                "No readable text found. "
                "The PDF may be a scanned image."
            )
            return

        resume_text = text.lower()

        found_skills = []

        for skill in KNOWN_SKILLS:
            if skill in resume_text:
                found_skills.append(skill)

        print("\n===== RESUME ANALYSIS =====")
        print("Pages:", len(reader.pages))
        print("Skills found:", found_skills)

        if found_skills:
            print("\nYou can use these skills in your career analysis:")
            print(", ".join(found_skills))
        else:
            print("No known skills were detected.")

    except Exception as error:
        print("Could not read the PDF:", error)
