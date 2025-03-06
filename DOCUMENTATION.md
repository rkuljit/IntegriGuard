IntegriGuard – System File Integrity Checker

Overview

IntegriGuard is a Python-based tool designed to monitor and verify the integrity of system files. It helps detect unauthorized modifications by calculating and comparing file hashes, providing a proactive approach to system security.

Features

SHA-256 Hashing: Uses secure SHA-256 hashing to generate unique file fingerprints.

Integrity Verification: Compares the current hash of a file against a known hash to check for modifications.

User-Friendly Interface: Simple command-line prompts for file path and original hash input.

Quick Results: Immediate feedback on whether the file integrity is verified or compromised.

Installation

Clone the Repository:

git clone https://github.com/yourusername/IntegriGuard.git
cd IntegriGuard

Set Up a Virtual Environment (Optional but Recommended):

python3 -m venv venv
source venv/bin/activate

Install Dependencies:No external libraries are required; the tool relies on Python's standard library.

Usage

Navigate to the Project Directory:

cd IntegriGuard/src

Run the Program:

python main.py

Follow the Prompts:

Enter the file path you want to check.

Provide the original SHA-256 hash for comparison.

Example

Enter the file path to check: /path/to/your/file.txt
Enter the original SHA-256 hash: abc123...
File integrity compromised!

How It Works

File Hashing: Reads the file in binary mode and calculates its SHA-256 hash.

Hash Comparison: Matches the current file hash against the user-provided original hash.

Result Output: Displays whether the file’s integrity is intact or compromised.

Security Considerations

Hash Storage: Store original hashes in a secure, read-only location.

File Permissions: Restrict access to critical files and logs.

Regular Audits: Periodically recheck file integrity to catch tampering early.

Future Enhancements

Automated Monitoring: Scheduled checks with logging.

Multi-File Support: Batch processing for multiple files.

GUI Interface: A graphical interface for easier use.

Contributing

Contributions are welcome! Feel free to fork the repository, submit pull requests, or suggest improvements via GitHub Issues.