n, q = map(int, input().split())

dnjsth = list(map(int, input().split()))

for _ in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        print(dnjsth[lst[1]-1])
    elif lst[0] == 2:
        if lst[1] in dnjsth:
            for j in dnjsth:
                if j == lst[1]:
                    print(dnjsth.index(j)+1)
                    break
        else:
            print('0')
    elif lst[0] == 3:
        for i in range(lst[1]-1, lst[2]):
            print(dnjsth[i], end=' ')