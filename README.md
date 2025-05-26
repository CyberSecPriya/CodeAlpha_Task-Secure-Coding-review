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
