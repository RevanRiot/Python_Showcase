# File: password_manager.py

import json
from cryptography.fernet import Fernet

# Generate a key and save it to a file (run this once to generate the key)
# key = Fernet.generate_key()
# with open("secret.key", "wb") as key_file:
#     key_file.write(key)

def load_key():
    """Loads the encryption key."""
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    """Encrypts the password."""
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    """Decrypts the password."""
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

def save_password(service, password, file="passwords.json"):
    """Saves an encrypted password."""
    key = load_key()
    encrypted_password = encrypt_password(password, key)
    try:
        with open(file, "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}

    passwords[service] = encrypted_password

    with open(file, "w") as f:
        json.dump(passwords, f, indent=4)
    print(f"Password for {service} saved.")

def retrieve_password(service, file="passwords.json"):
    """Retrieves and decrypts a password."""
    key = load_key()
    try:
        with open(file, "r") as f:
            passwords = json.load(f)
        if service in passwords:
            encrypted_password = passwords[service]
            return decrypt_password(encrypted_password, key)
        else:
            return "Service not found."
    except FileNotFoundError:
        return "No passwords stored yet."

if __name__ == "__main__":
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service_name = input("Enter service name: ")
            password = input("Enter password: ")
            save_password(service_name, password)
        elif choice == '2':
            service_name = input("Enter service name: ")
            print(f"Password: {retrieve_password(service_name)}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
