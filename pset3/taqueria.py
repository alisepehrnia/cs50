dishes = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

print("Select your item with Enter key. press Ctrl+D to stop ordering.")

print(50 * "-")
for dish in dishes:
    print(f"{dish.title()} - {dishes[dish]}$")
print(50 * "-")
print()

total = 0
while True:
    print("Enter your order:")
    try:
        order = input("").title()
        total += dishes[order]
    except EOFError:
        break
    except KeyError:
        print("Dish not found!")
    else:
        print(f"Total Order So Far: {total:.2f}$")