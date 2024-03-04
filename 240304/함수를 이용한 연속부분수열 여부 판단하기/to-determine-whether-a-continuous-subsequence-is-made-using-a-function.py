def get_answer(A,B):
    for i in range(n1-n2-1):
        for j in range(n2):
            if A[i]==B[j]:
                return True
    return False

n1,n2=tuple(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

if get_answer(A,B):
    print('Yes')
else:
    print('No')