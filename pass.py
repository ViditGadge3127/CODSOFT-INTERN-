import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_characters = string.punctuation if include_special else ''

    # Combine the character sets based on user preferences
    all_characters = lowercase + uppercase + digits + special_characters
    
    if not all_characters:
        raise ValueError("No character sets selected. At least one character set must be included.")
    
    # Generate the password using the selected character sets
    password = [random.choice(all_characters) for _ in range(length)]

    # Ensure the password includes at least one character from each selected set
    if include_uppercase:
        password[random.randint(0, length-1)] = random.choice(uppercase)
    if include_digits:
        password[random.randint(0, length-1)] = random.choice(digits)
    if include_special:
        password[random.randint(0, length-1)] = random.choice(special_characters)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Main function to get user input and display the generated password
def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, include_uppercase, include_digits, include_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
