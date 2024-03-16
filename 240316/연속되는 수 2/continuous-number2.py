n=int(input())
num_list=[]
for _ in range(n):
    num=int(input())
    num_list.append(num)

cnt=1
result=0
for i in range(1,n):
    if num_list[i]==num_list[i-1]:
        cnt+=1
    else:
        result=max(cnt,result)
        cnt=1
    result=max(cnt,result)

print(result)