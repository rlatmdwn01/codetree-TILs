def get_answer(A,B):
    for i in range(n1-n2-1):
        if A[i]==B[0] and A[i+1]==B[1] and A[i+2]==B[2]:
            return True
    return False

n1,n2=tuple(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

if get_answer(A,B):
    print('Yes')
else:
    print('No')