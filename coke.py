due = 50
while due > 0:
    pay = int(input("Insert Coin: "))
    if pay in [25, 10, 5]:
        due = due - pay
        if due > 0:
            print("Amount Due:", due)
        elif due < 0:
            print("Change Owed:",-due)
        elif due == 0:
            print("Change Owed: 0")
    else:
        print("Amount Due:", due)



