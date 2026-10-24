coins_sum = 0
TOTAL_COST = 50

while True:
    coin = input("Insert coin: ")

    try:
        coin = int(coin)
    except:
        continue

    if coin != 25 and coin != 10 and coin != 5:
        print("Invalid coin!")
    else:
        coins_sum += coin

    due_or_owe = TOTAL_COST - coins_sum

    if (due_or_owe > 0):
        print(f"Amount Due: {due_or_owe}")
    else:
        print(f"Charge Owed: {-due_or_owe}")
        print("Tank you for buying!")
        break