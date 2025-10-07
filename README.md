# Custom-Encryption-System
A Python-based file encryption tool using XOR cipher with rotating key algorithm for secure data protection


Custom Encryption System
Description
A file encryption and decryption program built in Python that uses a custom XOR cipher with rotating key algorithm. This project implements a position-dependent encryption scheme to provide secure data protection for text files through mathematical operations.
Features

Custom XOR Encryption Algorithm: Uses XOR operations with a rotating key that changes based on character position
Position-Dependent Security: Each character is encrypted with a unique key calculated as (base_key + position) % 256
File-Based Operations: Reads plaintext files, encrypts them, and saves encrypted output
Reversible Decryption: Self-reversing algorithm mathematically guarantees perfect decryption
Interactive Menu Interface: User-friendly command-line interface with multiple options
Error Handling: Robust file I/O error handling for missing or invalid files

Technologies Used

Language: Python 3.x
Core Concepts:

XOR bitwise operations
File I/O operations
Modular arithmetic
Command-line interface design



How the Algorithm Works
Encryption Process

Read plaintext from input file
For each character at position i:

Calculate dynamic key: key = (42 + i) % 256
Encrypt character: encrypted_char = original_char XOR key


Write encrypted data to output file

Decryption Process
Since XOR is self-reversing (A XOR B XOR B = A), the same algorithm decrypts the file:

Read encrypted file
Apply the same XOR operation with the same position-based keys
Original text is perfectly restored

Why This Works

XOR has the property: plaintext XOR key XOR key = plaintext
Position-based rotation makes each character use a different key
Modulo 256 keeps values within valid byte range

How to Run
Prerequisites

Python 3.6 or higher installed on your system

Setup

Clone this repository:

bashgit clone https://github.com/ZishanSha/Custom-Encryption-System.git
cd Custom-Encryption-System

Create an input text file named input.txt with content you want to encrypt

Running the Program
bashpython main.py
Menu Options

Encrypt a file: Encrypts input.txt and saves to encrypted.txt
Decrypt a file: Decrypts encrypted.txt and saves to decrypted.txt
Exit: Closes the program

Example Usage
=== Encryption/Decryption Program ===
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter your choice: 1

File encrypted successfully!
Input: input.txt
Output: encrypted.txt
Project Structure
Custom-Encryption-System/
│
├── main.py                 # Main program with encryption logic
├── input.txt              # Sample plaintext file
├── encrypted.txt          # Generated encrypted output
├── decrypted.txt          # Generated decrypted output
└── README.md              # This file
What I Learned

Cryptography Fundamentals: Understanding XOR cipher operations and why they're useful for encryption
Algorithm Design: Creating a position-dependent encryption scheme that enhances basic XOR security
Mathematical Operations: Applying modular arithmetic to ensure values stay within valid ranges
File I/O in Python: Reading from and writing to files with proper error handling
User Interface Design: Building intuitive menu-driven command-line applications
Testing and Verification: Ensuring encryption/decryption processes work correctly and restore original data

Security Note
⚠️ Educational Purpose Only: This encryption system is designed for learning purposes and should NOT be used for securing sensitive real-world data. Production encryption should use established cryptographic libraries like PyCrypto, cryptography, or built-in hashlib modules.
The XOR cipher with a static base key (even with rotation) is vulnerable to:

Known-plaintext attacks
Frequency analysis (for longer texts)
Pattern recognition

For real applications, use industry-standard encryption like AES-256.
Future Improvements

 Add support for different file types (not just text)
 Implement user-defined encryption keys
 Add password protection for encrypted files
 Create a GUI interface using Tkinter
 Add file compression before encryption
 Implement stronger encryption algorithms (AES)

Course Information
Created as part of CPSC 253 - Cybersecurity Foundations at California State University, Fullerton
Author
Zishan A. Shaikh

GitHub: @ZishanSha
LinkedIn: ZishanShaikh
Email: ZishanSha@csu.fullerton.edu

License
This project is open source and available for educational purposes.

Last Updated: October 2025
