#Module
import random

# Create a function
def generate_password(length):

#Create the Character Set (String)
    characters="abcdefghijklmnopqrstuvwxyz"

# Create an Empty Password
    password = ""

# Generate Characters with a Loop
    for _ in range(length):

# Pick Random Numbers
        password += random.choice(characters)

# Return the password
    return password

#Test Function
print(generate_password(8))
print(generate_password(12))


