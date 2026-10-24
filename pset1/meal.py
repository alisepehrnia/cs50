def main():
    inp = input("What time is it? ")
    time = convert(inp)
    print(f"Converted time in 24-hr format: {time}")
    if 7 <= time <= 8:
        print("Time for breakfast!")
    elif 12 <= time <= 13:
        print("Time for lunch!")
    elif 18 <= time <= 19:
        print("Time for dinner!")
    else:
        print("NO MEAL!")

def convert(time):
    hour, minute_and_format = time.split(":")
    hour = int(hour)
    minute, format = minute_and_format.split(" ")
    minute = int(minute)
    if format == "p.m." and 1 <= hour < 12:
        hour += 12
    return hour + minute / 60

if __name__ == "__main__":
    main()