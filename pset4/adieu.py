import inflect
p = inflect.engine()

list = []
while True:
    inp = input("Enter name: ")
    if inp == "":
        break
    list.append(inp)

print(f"Adieu, adieu, to {p.join(list)}")