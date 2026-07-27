import re

# Validation Functions

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def validate_password(password):
    # Minimum 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    return re.match(pattern, password)


def validate_mobile(mobile):
    # Must be exactly 10 digits
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile)


# Main Program
def main():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    mobile = input("Enter Mobile Number: ")

    print("\n--- Validation Results ---")

    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")

    if validate_password(password):
        print("Valid Password")
    else:
        print("Invalid Password")

    if validate_mobile(mobile):
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")


if __name__ == "__main__":
    main()