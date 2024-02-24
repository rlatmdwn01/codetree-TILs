n=int(input())

num_list=list(map(int,input().split()))

new_list=[i**2 for i in num_list]

for i in new_list:
    print(i,end=' ')