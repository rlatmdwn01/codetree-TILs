def print_num(n):
    i=1
    for _ in range(n):
        for j in range(n):
            if i==10:
                i=1
                print(i,end=' ')
                i+=1
            else:
                print(i,end=' ')
                i+=1
        print()
n=int(input())
print_num(n)