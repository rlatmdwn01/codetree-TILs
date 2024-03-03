n,A=input().split()
cnt=0
n=int(n)

for _ in range(n):
    word=input()
    if word==A:
        cnt+=1

print(cnt)