num_list=list(map(int,input().split()))
new_list=[]

for i in num_list:
    if i!=0:
        new_list.append(i)
    else:
        break

print(new_list[-1]+new_list[-2]+new_list[-3])