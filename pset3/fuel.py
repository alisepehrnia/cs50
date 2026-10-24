import math

inp = input("Enter the fuel fraction: ")
x, y = inp.split('/')

try:
    x = int(x)
    y = int(y)
except:
    print("Wrong number!")

try:
    percentage = round(x / y * 100)
except:
    print("Wrong number!")
else:
    if percentage < 0 or percentage > 100:
        print("Wrong number!")
    elif percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")