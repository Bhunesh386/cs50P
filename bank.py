x = input('Greeting: ').strip().lower()
a = x[0]
b = x[:5]
if b == 'hello':
    print('$0')
elif a == 'h':
    print('$20')
else:
    print('$100')
