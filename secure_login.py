import getpass # Hides password input when typing
import hashlib # For password hashing

# Simulated secure user database (username: hashed_password)
users = {
    "admin": hashlib.sha256("StrongPassword123!".encode()).hexdigest()
}

def login():
    # Take username from user input
    username = input("Enter username: ")
    # Take password securely (hidden input)
    password = getpass.getpass("Enter password (input hidden): ")

    # Hash the password entered by user
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Compare hashed input password with stored hash
    if username in users and users[username] == hashed_password:
        print("Login successful!") # Access granted
    else:
        print("Invalid credentials.") # Access denied

# Run the login function
login()
