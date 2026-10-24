camel_case_name = input("enter your camel case variable name: ")

for char in camel_case_name:
    if (char.islower()):
        print(char, end="")
    else:
        print("_" + char.lower(), end="")