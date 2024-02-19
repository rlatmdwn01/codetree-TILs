empty_list=[]
satisfied=False

for _ in range(1,6):
    n=int(input())
    empty_list.append(n)
    for i in empty_list:
        if i%3==0:
            satisfied=True

if satisfied==True:
    print(1)
else:
    print(0)