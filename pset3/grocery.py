
items = {}

while True:
    item = input("Enter your item: ").lower()
    if item == "":
        break
    if item in items:
        items[item] += 1
    else:
        items[item] = 1

for item in sorted(items):
    print(f"{items[item]} {item.upper()}")