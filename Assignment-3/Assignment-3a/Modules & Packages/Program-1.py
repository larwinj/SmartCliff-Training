import random
import string
def generate_password(length):
    # letters(upper+lower),digits,punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

n = int(input("Enter the length of the password: "))

print("Generated password:", generate_password(n))