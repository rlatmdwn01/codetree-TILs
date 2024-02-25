cnt_list=[0]*4

for _ in range(3):
    a,b=input().split()
    b=int(b)
    if a=='Y' and b>=37:
        cnt_list[0]+=1
    elif a=='N' and b>=37:
        cnt_list[1]+=1
    elif a=='Y' and b<37:
        cnt_list[2]+=1
    elif a=='N' and b<37:
        cnt_list[3]+=1

for i in range(4):
    print("{0}".format(cnt_list[i]),end=' ')

if cnt_list[0]>=2:
    print("E")