num_list=list(map(int,input().split()))

num_list.sort()

new_small_list=[]
new_big_list=[]

for i in num_list:
    if i>500:
        new_small_list.append(i)
    else:
        new_big_list.append(i)

print(max(new_big_list),min(new_small_list))