def is_subsequence(A, B):
    n = len(A)
    m = len(B)
    
    # 수열 B의 각 원소가 수열 A에 있는지 확인
    j = 0
    for i in range(n):
        if j == m:
            break
        if A[i] == B[j]:
            j += 1
    
    # 수열 B의 모든 원소가 수열 A에 있는 경우, 수열 B는 수열 A의 연속 부분 수열이다.
    return j == m

# 입력
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
if is_subsequence(A, B):
    print("Yes")
else:
    print("No")