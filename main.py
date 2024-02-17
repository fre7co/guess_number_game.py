import random

tokens = 10
while tokens > 0:
    print("Choose level of difficulty: (1, 2, 3)")
    level = input("Enter level: ")
    if level not in {'1', '2', '3'}:
        print("Invalid level")
        break

    try:
        level = int(level)
    except ValueError:
        print("Please enter a number")
        continue

    random_number = random.randint(1, 10 ** level)
    print(f"Guess a number between 1 and {10 ** level}")
    try:
        guess = int(input())
    except ValueError:
        print(f"Please enter a number between 1 and {10 ** level}")
        continue

    if guess == random_number:
        tokens += 10 ** level
        print(f"You won! Your amount of tokens is now {tokens}")
    else:
        tokens -= 10 ** (-level)
        print(f"You lost! The correct number was {random_number}. Your amount of tokens is now {tokens}")

print("You have no more tokens on your balance. Game over")
