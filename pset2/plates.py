def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("👍 Valid")
    else:
        print("👎 Invalid")


def is_valid(s):
    c1 = is_length_valid(s)
    c2 = s.isalnum()
    c3 = is_started_with_two_letters(s)
    c4 = not first_num_zero(s)
    c5 = not_number_in_middle(s)
    print("Summary")
    print('-' * 10)
    print(f"Length between 2 & 6 characters:\t{c1}")
    print(f"Just alphabet and Numbers:\t\t{c2}")
    print(f"Started with two letters:\t\t{c3}")
    print(f"First number not '0':\t\t\t{c4}")
    print(f"Numbers come at the end:\t\t{c5}")
    print()
    return c1 and c2 and c3 and c4 and c5
    
def is_length_valid(s):
    return len(s) >= 2 and len(s) <= 6

def is_started_with_two_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

def first_num_zero(s):
    for char in s:
        if char.isnumeric():
            if char == '0':
                return True
            return False
    return False

def not_number_in_middle(s):
    return s[2:].isnumeric() or s[3:].isnumeric() or s[4:].isnumeric() or s.isalpha()

main()