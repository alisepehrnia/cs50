import math

app_name = "INTERPRETER"
app_description = "Calculate sum, subtract, multiply or divide of two decimals"

def generate_title(header_size, app_name):
    partition_size = math.ceil((header_size - len(app_name)) / 2)
    return " " * partition_size + app_name + " " * partition_size

print("=" * len(app_description))
print(generate_title(len(app_description), app_name))
print("=" * len(app_description))
print()
print(app_description)
print()
print("Help:")
print("\tinput format must be like: 'number1 operation number2'")
print("\t'opertation' could be either '+','-','*' or '/'")
print("\tTo exit the programe enter 'q'")
print()

while (True):
    try:
        inp = input("Enter your expression: ").lower()
        if inp == "q" or inp == "quit":
            break
        x, y, z = inp.split(" ")
    except KeyboardInterrupt:
        break
    except:
        print("Incorrect format. Try again")
        continue    

    x = float(x)
    z = float(z)

    if y == "+":
        print(f"{x + z:.2f}")
    elif y == "-":
        print(f"{x - z:.2f}")
    elif y == "*":
        print(f"{x * z:.2f}")
    elif y == "/":
        if z != 0:
            print(f"{x / z:.2f}")
        else:
            print("NaN")
    else:
        print("Opertaion not supported!")