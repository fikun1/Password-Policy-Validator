import re

def check_password_policy(password):
    """
    Checks if a password meets common security criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character
    """

    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length (min 8 chars)": length_error,
        "Uppercase letter": uppercase_error,
        "Lowercase letter": lowercase_error,
        "Number": digit_error,
        "Special character": special_char_error
    }

    if not any(errors.values()):
        return "PASS"
    else:
        failed_criteria = [k for k, v in errors.items() if v]
        return f"FAIL: {', '.join(failed_criteria)}"

if __name__ == "__main__":
    password = input("Enter the password to check: ")
    result = check_password_policy(password)
    print(f"Result: {result}")

