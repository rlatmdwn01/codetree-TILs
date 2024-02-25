a,b=input().split()
a=int(a)
b=int(b)

cnt_list=[0]*(b+1)

while a>1:
    a=int(a//b)
    c=int(a%b)
    cnt_list[c]+=1

sum_val=0
for i in cnt_list:
    sum_val+=i**2

print(sum_val)