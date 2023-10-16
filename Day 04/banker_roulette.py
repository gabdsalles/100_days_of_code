# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#random_number = random.randint(0, len(names)-1)
#print(f"{names[random_number]} is going to buy the meal today!")

person_paying = random.choice(names)
print(person_paying + " is going to buy the meal today!")