n=int(input())
num_list=list(map(int,input().split()))

num_list.sort()
for i in range(n):
    print(num_list[i],end=' ')

print()

num_list.sort(reverse=True)
for i in range(n):
    print(num_list[i],end=' ')