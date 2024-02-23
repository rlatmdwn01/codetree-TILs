n=int(input())
empty_list=[]

for i in range(1,n+1):
    for j in range(2,i):
        if i%j!=0:
            empty_list.append(str(i))

empty_list.append('2')
empty_list.sort()
result=" ".join(empty_list)
print(result)