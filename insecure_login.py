# insecure_login.py
# This is a basic login system with poor security practices

def login():
    username = input("Enter username: ") # Hardcoded username and password (bad practice)
    password = input("Enter password: ")

# Checking if the input matches the hardcoded values

    if username == "admin" and password == "admin123":
        print("Login successful!")
    else:
        print("Invalid credentials.")

login()
