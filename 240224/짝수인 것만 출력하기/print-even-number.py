n=int(input())
num_list=list(map(int,input().split()))

new_list=[i for i in num_list if i%2==0]

for i in new_list:
    print(i,end=' ')