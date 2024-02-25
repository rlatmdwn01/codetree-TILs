num_list=list(map(int,input().split()))
cnt_list=[0]*11


for i in num_list:
    if i!=0:
        cnt_list[int(i//10)]+=1
    else:
        break

for i in range(10,0,-1):
    print("{0} - {1}".format(i*10,cnt_list[i]))