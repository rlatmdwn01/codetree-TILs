n=int(input())
cnt=0

for i in range(n):
    for j in range(i+1):
        if 65+cnt>ord('Z'):
            cnt=0
        print(chr(65+cnt),end="")
        cnt+=1
    print()