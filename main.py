import random

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
