password = input("Enter password: ")

has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

if len(password) >= 8 and has_digit and has_upper:
    print("Password is valid")
else:
    print("Password is invalid")

    if len(password) < 8:
        print("Minimum 8 characters required")
    if not has_digit:
        print("Include at least one digit")
    if not has_upper:
        print("Include at least one uppercase letter")