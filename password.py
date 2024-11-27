import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    while True:
        try:
            pass_length = int(input("Enter desired password length (minimum 6): "))
            if pass_length < 6:
                print("Password length must be at least 6. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    upper = input("Include uppercase letters? (yes/no): ").strip().lower()
    nums = input("Include numbers? (yes/no): ").strip().lower()
    special = input("Include special characters? (yes/no): ").strip().lower()
    
    char_pool = string.ascii_lowercase
    
    if upper == 'yes':
        char_pool += string.ascii_uppercase
    if nums == 'yes':
        char_pool += string.digits
    if special == 'yes':
        char_pool += string.punctuation

    if len(char_pool) == 0:
        print("You must select at least one character type. Exiting.")
        return

    password = ''.join(random.choice(char_pool) for _ in range(pass_length))
    print(f"Generated password: {password}")

if __name__ == "__main__":
    generate_password()
