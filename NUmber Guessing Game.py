import random

secret = random.randint(1, 10)

print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret:
    print("Correct! You won!")

else:
    print("Wrong!")
    print("The number was:", secret)