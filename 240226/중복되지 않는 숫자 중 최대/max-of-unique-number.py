N=int(input())
num_list=list(map(int,input().split()))

num_list.sort()

if num_list[-1]==num_list==[-2]:
    print(-1)

else:
    print(num_list[-1])