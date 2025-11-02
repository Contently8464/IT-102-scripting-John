#Create a SHA-512 password generator

#By John Gurney
import passlib
from passlib.hash import sha512_crypt
import string
import secrets
#create a method to prompt yes or no

def prompt_yes_no(msg: str) -> bool:
    while True:
        r = input(f"{msg} [y/n]: ").strip().lower()
        if r in ("y", "yes"):
            return True
        if r in ("n", "no"):
            return False
        print("Please enter y or n.")
#take count of pasword
count_in = input("How many passwords to generate? (default 5): ").strip()
count = int(count_in) if count_in.isdigit() and int (count_in) > 0 else 5
#take in amount of length of passwords user may want
length_in = input("Length of each password (min 8, default 12): ").strip()
length = int(length_in) if length_in.isdigit() and int(length_in) >= 8 else 12
#Defining user inputs of what is required of the password
use_upper = prompt_yes_no("Include UPPERCASE LETTERS?")
use_lower = prompt_yes_no("Include lowercase letters?")
use_digits = prompt_yes_no("Include Digits?")
use_special = prompt_yes_no("Include special characters?")

if not any((use_upper, use_lower, use_special, use_digits)):
    print("No character classes were chosen, defaukting to lower class + digits")
    use_lower = True
    use_digits = True

#CReate a pool of characters, string, digits, special characters
pool = ""

if use_upper:
    pool += string.ascii_uppercase
if use_lower:
    pool += string.ascii_lowercase
if use_digits:
    pool += string.digits
if use_special:
    pool += "!@#$%^&*(){}[],.<>?"

#define header of our generated passwords
print("\n====== GENERATED PASSWORDS and SHA512-Crypt hashes =====\n")

for _ in range(count):
    chars = []
    if use_upper:
        chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        chars.append(secrets.choice(string.digits))
    if use_special:
        chars.append(secrets.choice("!@#$%^&*(){}[],.<>?"))

    while len(chars) < length:
        chars.append(secrets.choice(pool))

    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]
   
    password = "".join(chars)
    hashed = sha512_crypt.hash(password)
   
    print(f"Password: {password}")
    print(f"sha512 : {hashed}\n")