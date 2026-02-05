#takes input of rocery lst, counts occurrences, and prints sorted grocery list
list = {}
while True:
    try:
        x = input()
        if x == "":
            break
        x = x.strip().upper()
        list[x] = list.get(x, 0) + 1
    except EOFError:
        break



n = len(list)
for i, item in enumerate(sorted(list.keys())):
    print(f"{list[item]} {item}")
