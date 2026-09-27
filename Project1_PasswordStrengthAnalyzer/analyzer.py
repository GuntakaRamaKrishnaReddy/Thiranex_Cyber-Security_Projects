import string
import secrets


# Commonly used / weak passwords
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "abc123",
    "iloveyou",
    "monkey",
    "dragon",
}


def analyze_password(password):
    score = 0
    suggestions = []

    # -----------------------------
    # 1. Length Check
    # -----------------------------
    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        suggestions.append("Increase the password length to at least 12 characters.")
    else:
        suggestions.append("Use at least 8 characters, preferably 12 or more.")

    # -----------------------------
    # 2. Lowercase Check
    # -----------------------------
    has_lowercase = any(char.islower() for char in password)

    if has_lowercase:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # -----------------------------
    # 3. Uppercase Check
    # -----------------------------
    has_uppercase = any(char.isupper() for char in password)

    if has_uppercase:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # -----------------------------
    # 4. Number Check
    # -----------------------------
    has_number = any(char.isdigit() for char in password)

    if has_number:
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # -----------------------------
    # 5. Special Character Check
    # -----------------------------
    special_characters = string.punctuation

    has_special = any(char in special_characters for char in password)

    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # -----------------------------
    # 6. Common Password Check
    # -----------------------------
    password_lower = password.lower()

    is_common = password_lower in COMMON_PASSWORDS

    if is_common:
        suggestions.append(
            "Avoid common or easily guessable passwords."
        )
        score = max(0, score - 2)

    # -----------------------------
    # 7. Repeated Character Check
    # -----------------------------
    has_repeated_characters = False

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            has_repeated_characters = True
            break

    if has_repeated_characters:
        suggestions.append(
            "Avoid repeating the same character multiple times."
        )
        score = max(0, score - 1)

    # -----------------------------
    # 8. Sequential Character Check
    # -----------------------------
    sequential_patterns = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "abc",
        "bcd",
        "cde",
        "qwe",
        "wer",
        "ert",
    ]

    has_sequence = any(
        pattern in password_lower
        for pattern in sequential_patterns
    )

    if has_sequence:
        suggestions.append(
            "Avoid predictable sequences such as 123 or abc."
        )
        score = max(0, score - 1)

    # -----------------------------
    # 9. Determine Strength
    # -----------------------------
    if length == 0:
        strength = "Very Weak"
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "length": length,
        "lowercase": has_lowercase,
        "uppercase": has_uppercase,
        "number": has_number,
        "special": has_special,
        "common": is_common,
        "repeated": has_repeated_characters,
        "sequence": has_sequence,
        "score": score,
        "strength": strength,
        "suggestions": suggestions,
    }


def generate_password(length=16):
    """Generate a strong random password."""

    if length < 8:
        length = 8

    characters = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + "!@#$%^&*"
)

    while True:
        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        # Make sure generated password satisfies all basic requirements
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password


def display_analysis(result):
    print("\n" + "=" * 45)
    print("        PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    print(f"\nPassword Length       : {result['length']}")
    print(
        f"Lowercase Characters : "
        f"{'Yes' if result['lowercase'] else 'No'}"
    )
    print(
        f"Uppercase Characters : "
        f"{'Yes' if result['uppercase'] else 'No'}"
    )
    print(
        f"Numbers              : "
        f"{'Yes' if result['number'] else 'No'}"
    )
    print(
        f"Special Characters   : "
        f"{'Yes' if result['special'] else 'No'}"
    )
    print(
        f"Common Password      : "
        f"{'Yes' if result['common'] else 'No'}"
    )
    print(
        f"Repeated Characters  : "
        f"{'Yes' if result['repeated'] else 'No'}"
    )
    print(
        f"Predictable Sequence : "
        f"{'Yes' if result['sequence'] else 'No'}"
    )

    print("\n" + "-" * 45)
    print(f"Score                 : {result['score']} / 8")
    print(f"Strength              : {result['strength']}")
    print("-" * 45)

    if result["suggestions"]:
        print("\nSuggestions:")

        for suggestion in result["suggestions"]:
            print(f"  -> {suggestion}")
    else:
        print("\nNo major issues detected.")

    print("=" * 45)


def main():
    print("=" * 45)
    print("      PASSWORD STRENGTH ANALYZER")
    print("=" * 45)

    password = input("\nEnter your password: ")

    # Analyze password
    result = analyze_password(password)

    # Display analysis
    display_analysis(result)

    # Offer stronger password
    print("\nWould you like a stronger password suggestion?")
    choice = input("Enter Y for Yes or N for No: ").strip().lower()

    if choice == "y":
        generated = generate_password(16)

        print("\nSuggested Strong Password:")
        print(generated)

    print("\nThank you for using Password Strength Analyzer!")


if __name__ == "__main__":
    main()
