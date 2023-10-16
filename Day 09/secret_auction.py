from art import logo
import os
 
def clear():
    os.system('cls')

auction_dictionary = {}
control = "yes"

def find_highest_bid():
    winner = ""
    bid = 0
    for person in auction_dictionary:
        if auction_dictionary[person] > bid:
            bid = auction_dictionary[person]
            winner = person

    print(f"The winner is {winner} with a bid of ${bid}")

print(logo)

while (control == "yes"):
    print("\nWelcome to the secret auction program.\n")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction_dictionary[name] = bid
    control = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

find_highest_bid()