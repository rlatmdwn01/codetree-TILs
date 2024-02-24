num_list=list(map(int,input().split()))

new_list=[]

for i in num_list:
    if i!=0:
        new_list.append(i)
    else:
        break


for j in new_list[::-1]:
    print(j,end=" ")