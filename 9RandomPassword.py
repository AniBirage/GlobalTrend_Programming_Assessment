import random
import string


def generate_random_password(length):  # Function to Generate a random password with specified length
    lowercase_letters = string.ascii_lowercase  # Lowercase Letters
    uppercase_letters = string.ascii_uppercase  # Uppercase Letters
    digits = string.digits  # Digits
    special_characters = string.punctuation  # Special Characters

    all_characters = (
        lowercase_letters + uppercase_letters + digits + special_characters
    )  # Combine all Character Sets

    password = "".join(
        random.choice(all_characters) for _ in range(length)
    )  # Generate Password
    return password


if __name__ == "__main__":
    try:
        password_length = int(
            input("Enter the length of the password: ")
        )  # Get Password Length
        generated_password = generate_random_password(password_length)
        print(f"Generated Password: {generated_password}")  # Print Generated Password
    except ValueError:
        print(
            "Error: Please enter a valid integer for password length."
        )  # Handle Invalid Input
