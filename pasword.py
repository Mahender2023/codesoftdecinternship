import string

password = input("Enter password: ")

if len(password) < 8:
    print("Invalid length of the password. Password must contain a minimum of 8 characters.")
else:
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    symbol = any(char in string.punctuation for char in password)

    if upper and lower and digit and symbol:
        print("Valid password")
    else:
        print("Password does not meet the requirements.")
