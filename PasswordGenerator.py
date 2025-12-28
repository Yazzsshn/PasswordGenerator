import random
import string

def calculate_security_level(length, has_upper, has_digit, has_symbol):
    score = 0

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "LOW"
    elif score <= 4:
        return "MEDIUM"
    else:
        return "HIGH"


def generate_password():
    length = int(input("Enter password length: "))

    use_upper = input("Should it contain uppercase letters? (yes/no): ").lower() == "yes"
    use_digit = input("Should it contain numbers? (yes/no): ").lower() == "yes"
    use_symbol = input("Should it contain symbols? (yes/no): ").lower() == "yes"

    char_pool = string.ascii_lowercase

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_digit:
        char_pool += string.digits
    if use_symbol:
        char_pool += string.punctuation

    if not char_pool:
        print("You must select at least one character type.")
        return

    password = "".join(random.choice(char_pool) for _ in range(length))

    security_level = calculate_security_level(
        length, use_upper, use_digit, use_symbol
    )

    print("\nGenerated Password:")
    print(password)
    print("\nPassword Security Level:", security_level)


generate_password()
