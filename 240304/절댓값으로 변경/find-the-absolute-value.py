n=int(input())
arr=list(map(int,input().split()))

def abs_num(arr):
    for i in range(n):
        if arr[i]<0:
            arr[i]=-arr[i]
        else:
            arr[i]=arr[i]

abs_num(arr)
for elem in arr:
    print(elem, end=' ')