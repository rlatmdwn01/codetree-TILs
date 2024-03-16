n=int(input())
num_list=[]
plus_list=[]
minus_list=[]
cnt=1
result=0

for _ in range(n):
    i=int(input())
    num_list.append(i)

for num in num_list:
    if num<0:
        minus_list.append(num)
    else:
        plus_list.append(num)

if len(minus_list)>len(plus_list):
    print(len(minus_list))

else:
    print(len(plus_list))