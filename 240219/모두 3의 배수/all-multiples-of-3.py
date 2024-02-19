empty_list=[]
satisfied=False

for _ in range(1,6):
    n=int(input())
    if n%3==0:
        empty_list.append(n)
    if len(empty_list)==5:
        satisfied=True

if satisfied==True:
    print(1)
else:
    print(0)