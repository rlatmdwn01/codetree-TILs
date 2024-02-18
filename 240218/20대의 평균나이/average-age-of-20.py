sum_val=0
cnt=0

while True:
    n=int(input())
    if 19<n<30:
        sum_val+=n
        cnt+=1
    else:
        print("%.2f"%(sum_val/cnt))
        break