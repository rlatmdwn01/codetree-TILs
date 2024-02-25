num_list=list(map(int,input().split()))

cnt_list=[0]*7

for i in num_list:
    cnt_list[i]+=1

for i in range(1,7):
    print("{0} - {1}".format(i,cnt_list[i]))