# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = (name1 + name2).lower()

true_count = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_count = names.count("l") + names.count("o") + names.count("v") + names.count("e")

score = int(str(true_count) + str(love_count))

if score >= 90 or score <= 10:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")