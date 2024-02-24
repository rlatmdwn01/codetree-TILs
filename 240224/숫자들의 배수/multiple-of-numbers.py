n=int(input())

num_list=[i*n for i in range(1,11)]
cnt=0

for i in num_list:
    print(i,end=' ')
    if i%5==0:
        cnt+=1
    if cnt==2:
        break