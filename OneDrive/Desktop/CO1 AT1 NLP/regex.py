import re

# -----------------------------
# Sample Resume Text (replace with file input if needed)
# -----------------------------
resume_text = """
John Doe
Email: johndoe@gmail.com
Phone: +91-9876543210

Experienced Software Engineer with 3 years of experience in Python, SQL, and Machine Learning.
Worked on NLP-based projects and backend systems.
"""

# -----------------------------
# Functions for Extraction
# -----------------------------

def extract_name(text):
    # Assume name is first line
    lines = text.strip().split("\n")
    return lines[0].strip()

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_phone(text):
    pattern = r'(\+?\d{1,3}[-\s]?)?\d{10}'
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_skills(text):
    skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
    found_skills = []
    for skill in skills_list:
        if re.search(rf'\b{skill}\b', text, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

def extract_experience(text):
    pattern = r'(\d+)\s+years?'
    match = re.search(pattern, text, re.IGNORECASE)
    return int(match.group(1)) if match else 0

# -----------------------------
# Process Resume
# -----------------------------

def process_resume(text):
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    summary = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": skills,
        "Experience (Years)": experience
    }

    return summary

# -----------------------------
# Eligibility Check
# -----------------------------

def is_eligible(candidate):
    return (
        candidate["Experience (Years)"] >= 2 and
        "Python" in candidate["Skills"]
    )

# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    candidate = process_resume(resume_text)

    print("\n--- Candidate Summary ---")
    for key, value in candidate.items():
        print(f"{key}: {value}")

    print("\n--- Eligibility ---")
    if is_eligible(candidate):
        print("✅ Candidate is ELIGIBLE")
    else:
        print("❌ Candidate is NOT eligible")