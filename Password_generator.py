import random
import string


def generate_password(num_characters=8, numbers=True, spl_char=True):
    '''
    Generates a random password based on specified criteria.

    Args:
      - num_characters (int): The length of the password (default is 8).
      - numbers (bool): Whether to include numbers in the password (default is True).
      - spl_char (bool): Whether to include special characters in the password (default is True).

    Returns:
      str: The generated password.
    '''
    alphabets = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters_set = alphabets
    if numbers:
        characters_set += digits
    if spl_char:
        characters_set += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_spl = False

    while not meets_criteria or len(pwd) < num_characters:

        new_char = random.choice(characters_set)
        pwd += new_char

        # Check for each character (efficient than checking the whole string)
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_spl = True

        # Set a flag using compound conditionals and contradiction
        meets_criteria = True  # Set as True initially to be proven False or True later

        if has_number:
            meets_criteria = has_number
        if has_spl:
            meets_criteria = has_spl and meets_criteria

    return pwd


if __name__ == "__main__":

    # User input for password criteria
    min_len = int(input("Enter minimum length of password you want: "))
    has_number = input("Password has Number (y/n): ").lower() == "y"
    has_spl = input("Password has Special Characters (y/n): ").lower() == "y"

    # Generate and print the password
    password = generate_password(min_len, has_number, has_spl)
    print("Generated Password:", password)
