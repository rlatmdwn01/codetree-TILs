num_list=list(map(int,input().split()))

cnt_list=[0]*10

for i in num_list:
    if i!=0:
        if i>9:
            cnt_list[int(i//10)]+=1
        

    else:
        break

for i in range(1,10):
    print("{0} - {1}".format(i,cnt_list[i]))