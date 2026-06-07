# password Strength checker

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak : password must have 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "Weak : password must have atleast one digit"
    
    if not any(char.isupper() for char in password):
        return "Weak : password must have atleast one uppercase character"
    
    if not any(char.islower() for char in password):
        return "Weak : password must have atleast one lowercase character"
    
    if not re.search(r'[!@#$%&*~^><.]', password):
        return "Medium Password : It must also contain atleast one special character"
    
    return "Strong Password : Your password is strong!"

def password_checker():
    print("Welcone to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit):")
        if password.lower() == 'exit':
            print("Thank You for using our tool")
            break
    
        result = check_password_strength(password)
        print(result)
    

# Running the tool

if __name__ == "__main__":
    password_checker()