import random

min_number = 1
max_number = 100
secret_number = random.randint(min_number, max_number)
tries = 0

while True:
    try: 
        guess = int(input(f"Guess the number from {min_number} to {max_number}: "))
        if guess < min_number or guess > max_number:
            print(f"Please enter a number from {min_number} to {max_number}")
        elif guess > secret_number:
            tries += 1
            print("Too high, Try again")
        elif guess < secret_number:
            tries += 1
            print("Too low, Try again")
        else:
            tries += 1
            print(f"Congratulations, you got it in {tries} tries")
            break
    except ValueError:
        print("invalid!, Please enter a numerical value")
        continue