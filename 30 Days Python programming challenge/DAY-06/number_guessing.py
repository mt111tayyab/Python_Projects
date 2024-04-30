import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)

# Keep asking the user to guess until they get it right
while True:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == target_number:
        print("Congratulations! You guessed the number correctly!")
        break
    else:
        print("Sorry, that's not the correct number. Try again.")
