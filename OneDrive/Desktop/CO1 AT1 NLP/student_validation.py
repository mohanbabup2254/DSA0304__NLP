import re

# -----------------------------
# Validation Functions
# -----------------------------

def validate_register_number(reg_no):
    # Example: REG2023001 (REG + 4 digits year + 3 digits)
    pattern = r'^REG\d{7}$'
    return bool(re.match(pattern, reg_no))

def validate_email(email):
    # Example: student@university.edu
    pattern = r'^[a-zA-Z0-9._%+-]+@university\.edu$'
    return bool(re.match(pattern, email))

def validate_course_code(course):
    # Example: CSE101, MAT202
    pattern = r'^[A-Z]{3}\d{3}$'
    return bool(re.match(pattern, course))

def validate_semester(sem):
    # Semester between 1 and 8
    pattern = r'^[1-8]$'
    return bool(re.match(pattern, sem))

def validate_mobile(mobile):
    # 10-digit mobile number (with optional country code)
    pattern = r'^(\+?\d{1,3})?\d{10}$'
    return bool(re.match(pattern, mobile))

# -----------------------------
# Main Program
# -----------------------------

def main():
    print("=== University Registration System ===")

    reg_no = input("Enter Register Number: ")
    email = input("Enter Institutional Email: ")
    course = input("Enter Course Code: ")
    semester = input("Enter Semester (1-8): ")
    mobile = input("Enter Mobile Number: ")

    print("\n--- Validation Results ---")

    valid_reg = validate_register_number(reg_no)
    print("Register Number:", "✅ Valid" if valid_reg else "❌ Invalid")

    valid_email = validate_email(email)
    print("Email:", "✅ Valid" if valid_email else "❌ Invalid (must end with @university.edu)")

    valid_course = validate_course_code(course)
    print("Course Code:", "✅ Valid" if valid_course else "❌ Invalid (format: ABC123)")

    valid_sem = validate_semester(semester)
    print("Semester:", "✅ Valid" if valid_sem else "❌ Invalid (1-8 only)")

    valid_mobile = validate_mobile(mobile)
    print("Mobile:", "✅ Valid" if valid_mobile else "❌ Invalid (10 digits)")

    # Final Status
    print("\n--- Registration Status ---")
    if all([valid_reg, valid_email, valid_course, valid_sem, valid_mobile]):
        print("🎉 Registration Successful!")
    else:
        print("⚠️ Registration Failed. Please correct the errors.")

# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    main()