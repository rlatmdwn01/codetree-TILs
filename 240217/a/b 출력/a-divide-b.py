arr = input().split( )
a = int(arr[0])
b = int(arr[1])
i = a//b
print(f'{i}.', end = '')
for _ in range(20):
    if i * b == a:
        print(0, end = '')
    elif i == 0:
        a *= 10
        print(a//b, end = '')
        i = a//b
    else:
        a = (a - i * b)*10
        print(a//b, end= '')
        i = a//b