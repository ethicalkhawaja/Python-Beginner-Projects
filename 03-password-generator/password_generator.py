import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&*"

password = ""

for i in range(8):
    password = password + random.choice(letters)

for i in range(2):
    password = password + random.choice(numbers)

for i in range(2):
    password = password + random.choice(symbols)

print("Your password is:", password)
