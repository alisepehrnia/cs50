
import random

n = -1
while n <= 0:
    try:
        n = int(input("Enter level (n): "))
    except:
        n = -1
        continue

guess = -1
rand = random.randint(1, n)
while guess <= 0 and guess != rand:
    try:
        guess = int(input(f"Guess the number between 1 and {n}: "))
        if guess <= 0:
            continue
    except:
        guess = -1
        continue
    else:
        if guess < rand:
            print("Too small!")
        elif guess > rand:
            print("Too large!")
        else:
            print("Just right!")