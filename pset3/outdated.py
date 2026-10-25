monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def validate_date(day, month, year):
    return not (month < 1 or month > 12 or day < 1 or day > 31 or year < 1 or year > 9999)

while True:
    bad_date = input("Enter date in 'MM/DD/YY' or 'month D,YYYY' ")
    if bad_date.count("/") == 2:
        try:
            month, day, year = bad_date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if not validate_date(day, month, year):
                continue
            break
        except:
            print("Bad Format!")
            continue
    else:
        try:
            month_name, day, year = bad_date.split(' ')
            day = int(day.strip(','))
            month = int(monthes.index(month_name)) + 1
            year = int(year)
            if not validate_date(day, month, year):
                continue
            break
        except:
            print("Bad Format!")
            continue

print(f"{year:04d}-{month:02d}-{day:02d}")