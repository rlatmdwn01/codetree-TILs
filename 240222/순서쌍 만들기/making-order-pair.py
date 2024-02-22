n=int(input())

for i in range(n,0,-1):
    for j in range(n,0,-1):
        print('({0},{1})'.format(i,j),end=' ')
    print()