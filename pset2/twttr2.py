inp = input("Enter your text: ")
VOWELS = ['a',"e","i","o","u"]

for char in inp:
    if char in VOWELS or char.upper() in VOWELS:
        continue
    print(char, end="")