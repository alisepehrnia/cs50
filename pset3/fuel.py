valid = False
while not valid:
    inp = input("Enter the fuel fraction: ")
    try:
        x, y = inp.split('/')
        x = int(x)
        y = int(y)
        percentage = round(x / y * 100)
    except:
        print("Wrong number!")
    else:
        if percentage < 0 or percentage > 100:
            print("Wrong number!")
        else:
            valid = True
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")