n=int(input())
num_list=list(map(int,input().split()))

prev_max_idx=n

while True:
    max_idx=0
    for i in range(1,prev_max_idx):
        if num_list[i]>num_list[max_idx]:
            max_idx=i
    
    print(max_idx+1,end=" ")

    if max_idx==0:
        break

    prev_max_idx=max_idx