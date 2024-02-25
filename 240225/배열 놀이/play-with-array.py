n,q=input().split()
n=int(n)
q=int(q)

num_list=list(map(int,input().split()))

for i in range (q):
    q_list=list(map(str,input().split()))


    if q_list[0]=='1':
        print(num_list[int(q_list[1])-1])
    elif q_list[0]=='2':
        if int(q_list[1]) in num_list:
            print(num_list.index(int(q_list[1]))+1)
        else:
            print(0)

    elif q_list[0]=='3':
        for j in range(int(q_list[1]),int(q_list[2])+1):
            print(num_list[j-1], end=' ')