num_list=list(map(int,input().split()))
new_list=[]

for i in num_list:
    if i!=0:
        if i%2==1:
            i=i+3
            print(i,end=' ')
        else:
            i=int(i//2)
            print(i,end=' ')

    else:
        break