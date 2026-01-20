def main():
    time = input('What time is it? ')
    time = time.strip()
    z = convert(time)
    if z >=7 and z<=8:
        print('breakfast time')
    elif z >= 12 and z <= 13:
        print('lunch time')
    elif z >= 18 and z <= 19:
        print('dinner time')


def convert(time):
    x,y = time.split(':')
    x = float(x)
    y = float(y)
    return x + y/60.0



if __name__ == "__main__":
    main()
