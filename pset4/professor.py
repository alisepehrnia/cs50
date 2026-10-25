
import random

def gen_number():
    return random.randint(10 * (n - 1), 10 * n - 1)

while True:
    try:
        n = int(input("Enter a number between 1 and 3: "))
        if 1 <= n <= 3:
            break
        continue
    except:
        continue

correct_answers = 0
for _ in range(10):
    x = gen_number()
    y = gen_number()
    wrong_answers = 0
    while True:
        if wrong_answers >= 3:
            print(f"> {x} + {y} = {x + y}")
            break
        try:
            answer = int(input(f"{x} + {y} = "))
            if (answer == x + y):
                correct_answers += 1
                print("Correct")
                break
            wrong_answers += 1
            continue
        except:
            print("EEE")
            continue

print(f"Score: {correct_answers}/10")