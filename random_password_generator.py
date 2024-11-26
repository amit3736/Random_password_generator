import random
import string
import os

def generate_password(length):
    """Generates a random password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation

    # Use os.urandom for a more secure random source
    random_bytes = os.urandom(length)
    password = ''.join(random.choice(characters) for _ in random_bytes)

    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be positive.")
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError as e:
        print("Invalid input:", e)
