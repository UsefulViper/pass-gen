import random
import string

def generate_password(length=8, uppercase=True, lowercase=True, numbers=True, special=True):
    """
    Generates a password with customizable options for length, complexity, and character types.
    
    Args:
        length (int): Length of the password. Minimum length is 8.
        uppercase (bool): Include uppercase letters.
        lowercase (bool): Include lowercase letters.
        numbers (bool): Include numbers.
        special (bool): Include special characters.
    
    Returns:
        str: Generated password.
    """
    
    uppercase_chars = string.ascii_uppercase if uppercase else ""
    lowercase_chars = string.ascii_lowercase if lowercase else ""
    number_chars = string.digits if numbers else ""
    special_chars = string.punctuation if special else ""
    
    
    possible_chars = uppercase_chars + lowercase_chars + number_chars + special_chars
    
    
    length = max(length, 8)
    
    
    if not possible_chars:
        raise ValueError("At least one character type must be selected.")
    
    
    password = ''.join(random.choice(possible_chars) for _ in range(length))
    
    
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')
    
    return password


if __name__ == "__main__":
    password = generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special=True)
    print(f"Generated Password: {password}")
