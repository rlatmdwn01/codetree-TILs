n=int(input())
num1_list=list(map(int,input().split()))
num2_list=list(map(int,input().split()))

num1_list.sort()
num2_list.sort()

if num1_list==num2_list:
    print('Yes')
else:
    print('No')