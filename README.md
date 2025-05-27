# CodeAlpha_Task-Secure-Coding-review (Pyhton Login System)

*COMPANY* : CODEALPHA

*NAME* : PRIYA BABARE

*INTERN ID* : CA/MA1/7455

*DOMAIN* : CYBER  SECURITY 

*DURATION* : 4 WEEKS

# Project Overview

This project demonstrates a basic secure coding review by comparing an insecure and a secure version of a Python login system.

It was created as part of my internship task to understand and apply secure coding practices using Python. The main objective was to identify common security flaws in code and provide a secure alternative implementation. I developed a simple login system in two versions:

- The first version (`insecure_login.py`) is intentionally vulnerable and highlights bad practices such as hardcoded credentials and plain-text password input.
  
- The second version (`secure_login.py`) addresses these flaws by applying secure coding principles such as password hashing, secure password input, and proper credential storage.

Through this task, I conducted a manual code review, documented the vulnerabilities, and learned how even simple applications can be exploited if not coded securely. The project reflects the difference between poor and secure coding, promoting awareness and understanding of cybersecurity in software development.

This hands-on experience helped me understand:

- How attackers can exploit insecure code.
  
- How to improve code security with simple but effective techniques.
  
- Why secure coding is essential in real-world applications.

It’s a beginner-friendly project that showcases how small changes can make big improvements in application security.

# Files Included

- `insecure_login.py` – A basic login script with poor security (hardcoded credentials, no hashing).

- `secure_login.py` – A secure login system using `getpass` and `hashlib` to protect credentials.
  
- `code_review_findings.txt` – Notes and explanations about vulnerabilities and improvements.

#  Key Security Fixes

**Insecure Code**

- Hardcoded passwords.                     

- Plain text password input.

- No hashing.                             

- No validation or secure comparison.

**Secure Code**

- No hardcoded credentials.

- Hidden password input using `getpass`.

- Passwords hashed using `hashlib` (SHA-256).

- Safe comparison with stored hash.

# Output

The output shows the difference between insecure and secure coding practices in action, making it easy to understand the impact of secure code.

**Insecure Version**

![Image](https://github.com/user-attachments/assets/16208dd8-adbc-4054-a3b8-2467f8134e6c)

**Secure Version**

**Test Case 1 – Correct Credentials**

When you run it:



**Test Case 2 – Wrong Username or Password**

When you run it:




# What’s Happening Behind the Scenes:

- The password you enter is hashed using SHA-256.

- It compares the hashed version to the one stored in the `users` dictionary.

- If they match, you get access. If not, it denies login.


# How It Works

Both versions of the login system ask the user for a username and password.

- In the **insecure version**, credentials are hardcoded and compared directly.
  
- In the **secure version**, the password input is hidden using `getpass` and securely hashed using `hashlib`. The hash is then compared with a stored value to verify access.

This shows the difference in security and why even simple scripts should follow best practices.

# Tools & Concepts Used

- Python 3.
  
- `getpass` for secure input.
 
- `hashlib` for password hashing.
 
- Manual code review techniques.

# What I Learned

- Importance of secure coding practices.
  
- Basic vulnerabilities in login systems.
  
- How to hash and validate passwords securely.
 
- Reviewing and refactoring insecure code.
 
- Clear documentation and technical writing for cybersecurity.

# Conclusion

This project highlights the importance of writing secure code by demonstrating how small improvements like hiding passwords and using hashing can significantly enhance application security.
