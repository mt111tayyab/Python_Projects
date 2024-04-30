import re

def is_strong_password(password):
    # Check if password contains at least one letter, one number, and one special character
    return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

# Ask the user for a password
password = input("Enter a password: ")

# Check if the password is strong
if is_strong_password(password):
    print("The password is strong.")
else:
    print("The password is weak. It must contain at least 8 characters, including one letter, one number, and one special character.")
