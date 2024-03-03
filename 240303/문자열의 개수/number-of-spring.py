cnt=0
num_list=[]

while True:
    n=input()
    if n=='0':
        break
    else:
        if cnt%2==0:
            num_list.append(n)
            cnt+=1
        else:
            cnt+=1
print(cnt)
for j in num_list:
    print(j)