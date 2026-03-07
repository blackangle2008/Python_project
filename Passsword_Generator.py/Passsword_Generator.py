import random
import string

# ---------- PASSWORD STRENGTH CHECK ----------
def check_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score == 3 or score == 4:
        return "Medium ⚠️"
    else:
        return "Strong 🔥"


# ---------- GENERATE PASSWORD ----------
def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    char_pool = ""
    password = []

    if use_upper:
        char_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if use_lower:
        char_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if use_numbers:
        char_pool += string.digits
        password.append(random.choice(string.digits))

    if use_symbols:
        char_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if char_pool == "":
        return None

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return "".join(password)


# ---------- MAIN PROGRAM ----------
print("🔐 Advanced Password Generator")

length = int(input("Enter password length: "))

use_upper = input("Include Uppercase? (y/n): ").lower() == 'y'
use_lower = input("Include Lowercase? (y/n): ").lower() == 'y'
use_numbers = input("Include Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_lower, use_numbers, use_symbols)

if password is None:
    print("❌ Select at least one character type!")
else:
    print("\n✅ Generated Password:", password)
    print("📊 Strength:", check_strength(password))

    # Save to file option
    save = input("Save password to file? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
        print("💾 Saved to passwords.txt")