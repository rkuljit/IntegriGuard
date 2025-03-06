import hashlib
import os

def calculate_file_hash(filepath):
    """Calculate the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as file:
            buffer = file.read()
            hasher.update(buffer)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def verify_integrity(file_path, original_hash):
    """Check if the file's current hash matches the original hash."""
    current_hash = calculate_file_hash(file_path)
    if current_hash is None:
        return "File not found."
    return "Integrity verified!" if current_hash == original_hash else "File integrity compromised!"

def main():
    file_path = input("Enter the file path to check: ")
    original_hash = input("Enter the original SHA-256 hash: ")

    result = verify_integrity(file_path, original_hash)
    print(result)

if __name__ == "__main__":
    main()