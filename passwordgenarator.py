'''password genarator'''
import random
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)
    for i in range(length))
    return password
print(generate_password())
