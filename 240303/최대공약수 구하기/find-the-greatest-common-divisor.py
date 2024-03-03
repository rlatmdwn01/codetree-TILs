def min_num(n,m):
    num_list=[]
    if n>m:
        for i in range(1,m+1):
            if n%i==0 and m%i==0:
                num_list.append(i)

    else:
        for i in range(1,n+1):
            if n%i==0 and m%i==0:
                num_list.append(i)

    print(max(num_list))

n,m=tuple(map(int,input().split()))
min_num(n,m)