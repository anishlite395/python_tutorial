# Build a Password Checker.
# Ask the user:
# Enter password:
# Then check whether the password is correct.
# For example, you could choose:
# correct_password = "python123"
# If the user enters the correct password:
# Access granted!
# Welcome!
# Otherwise:
# Access denied!
# Wrong password.

password = input("Enter the password: ")

correct_password = "goku"

if password == correct_password:
    print("Access Granted!")
    print("Welcome!")

else:
    print("Access Denied!")
    print("Wrong Password.")