import random

# Step 1: Ask for user's name
name = input("Welcome agent. What is your name? ")

# Step 3: Lists of adjectives and animals
adjectives = ["Sneaky", "Fuzzy", "Brave", "Silent", "Swift", "Shadowy"]
animals = ["Otter", "Panther", "Fox", "Eagle", "Tiger", "Wolf"]

# Step 5: Randomly choose a codename
codename = random.choice(adjectives) + " " + random.choice(animals)

# Step 6: Randomly choose a lucky number from 1 to 99
lucky_number = random.randint(1, 99)

# Step 7: Display the result
print(f"\nAgent {name}, your codename is '{codename}' and your lucky number is {lucky_number}.")
