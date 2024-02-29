A=input()
B=input()

n1=len(A)
n2=2
cnt=0

for i in range(n1-1):
    if A[i]==B[0] and A[i+1]==B[1]:
        cnt+=1

print(cnt)