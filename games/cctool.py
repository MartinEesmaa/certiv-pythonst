# Caesar Cipher Tool
# Note: Encryption only
# Programmed by Martin Eesmaa (2025)
# License: MIT
# Source code: https://github.com/MartinEesmaa/certiv-pythonst
# Script language version: Python 3
# Filename: cctool.py
# Date: 14.10.2025

"""
This activity shows to encrypt plaintext using a Caesar Cipher.
It allows for up to 26 uppercase letters of the English alphabet.

This will shift the letters in the plaintext (unencrypted message)
so that they are remapped to new letters in the ciphertext (encrypted message).

Code requirements are met to:
- Accept the plaintext string
- Prepare/convert plaintext as required
- Accept cipher key
- Generate cipher
- Capture and report potential errors
- Generate ciphertext
"""

print("\nWelcome to the Caesar Cipher Game!")
print("Note: Encryption only\n")
print("Programmed by Martin Eesmaa (2025)\n")

while True:
    plaintext = input("Enter the plaintext message: ").strip()
    if plaintext:
        break
    print("Plaintext cannot be empty including spaces. Please type a valid message.\n")

while True:
    key_input = input("Enter the cipher key (1-25, default is 3 for ROT-3): ").strip()
    if key_input == "":
        key = 3
        break
    try:
        key = int(key_input)
        if 1 <= key <= 25:
            break
        else:
            print("Cipher key must be between 1 and 25. Please try again.")
    except ValueError:
        print("Invalid input! Please type a number for the cipher key.")

# Prepare the plaintext and check for special characters
prepared_text = ""
special_found = False
for char in plaintext:
    if char.isalpha() or char == '.' or char == ' ' or char.isdigit():
        prepared_text += char
    else:
        special_found = True

if special_found:
    print("\033[33mWarning: Special characters are not compatible and will be ignored.\033[0m")

if not prepared_text:
    print("No characters typed in. Exiting.")
    exit()

ciphertext = ""
for char in prepared_text:
    if char.isupper():
        shifted = (ord(char) - ord('A') - key) % 26 + ord('A')
        ciphertext += chr(shifted)
    elif char.islower():
        shifted = (ord(char) - ord('a') - key) % 26 + ord('a')
        ciphertext += chr(shifted)
    elif char == '.' or char == ' ' or char.isdigit():
        ciphertext += char

print(f"\nPrepared plaintext (only letters and digits): {prepared_text}")
print(f"Cipher key: ROT-{key}")
print(f"Ciphertext: {ciphertext}")
print("\nThank you for using the Caesar Cipher Tool for encryption!\n")