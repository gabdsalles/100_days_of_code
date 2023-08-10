#Write your code below this line 👇

def prime_checker(number):
    isPrime = True
    
    if (number % 2 == 0):
        isPrime = False
    else:
        for i in range(3, number, 2):
            if (number % i == 0):
                isPrime = False

    if number == 2:
        isPrime = True
    
    if (isPrime):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
