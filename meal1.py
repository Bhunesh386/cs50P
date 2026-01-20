def main():
    time = input(' that is the time rn? ')
    time = time.strip().lower()
    z = convert(time)
    if time.endswith('a.m.'):
        if z >= 7 and z <= 8:
            print('breakfast time')
        else:
            print('')
    elif time.endswith('p.m.'):
        if z >= 12 and 2 < 13 or z <= 2 or z > 0:
            print('lunch time')
        elif z >= 6 and z <= 7:
            print('dinner time')
    else:
        if z >=7 and z<=8:
            print('breakfast time')
        elif z >= 12 and z <= 13:
            print('lunch time')
        elif z >= 18 and z <= 19:
            print('dinner time')
def convert(time):
    x, y = time.split(':')
    y = y[0:1]
    x = int(x)
    y = int(y)
    z = x + y/60.0
    return z


main()
