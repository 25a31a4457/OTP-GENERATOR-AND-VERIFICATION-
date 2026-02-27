# 🔐 OTP Generation & Verification System (Python)

A console-based One-Time Password (OTP) Generation and Verification System built using Python.  
This project demonstrates secure random number generation and basic authentication flow implementation.

---

## 🚀 Features

- Secure 6-digit OTP generation
- Cryptographically strong randomness using the `secrets` module
- Menu-driven console interface (Generate / Verify / Exit)
- OTP verification with validation logic
- Handles invalid and empty inputs
- Continuous verification until correct OTP is entered

---

## 🛠 Tech Stack

- Language: Python 3
- Libraries: 
  - secrets
  - string

---

## 🧠 Concepts Applied

- Secure token generation
- Authentication flow logic
- Control flow (if-elif-else)
- Loops and conditional statements
- Functions and global state handling
- Input validation and error handling

---

## ⚙️ How It Works

1. User selects the "Generate OTP" option.
2. System generates a secure 6-digit OTP using `secrets.choice()`.
3. User selects the "Verify OTP" option.
4. System validates user input against the generated OTP.
5. Verification continues until the correct OTP is entered.

---

## 🔒 Why Use the `secrets` Module?

The `secrets` module is used instead of the `random` module because it provides
cryptographically secure random number generation, making it suitable for
authentication and security-sensitive applications.

---

## 📈 Future Enhancements

- OTP expiration timer
- Limited retry attempts
- Email/SMS-based OTP integration
- Hash-based OTP comparison instead of plain-text matching
- Database integration for user management

---

## 📂 Project Type

Mini Project – Beginner Level  
Focus Area: Authentication Systems & Secure Coding Basics

---

## 👨‍💻 Author

Maruthi Guruprasad
Aspiring Software Developer | Python Enthusiast

