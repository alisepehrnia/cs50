inp = input("Enter your text: ")
output = inp
VOWELS = ['a',"e","i","o","u"]

for vowel in VOWELS:
    output = output.replace(vowel, "").replace(vowel.upper(), "")

print(output)