A = []

def prefix_sum(A):
    # 수열 A의 누적 합을 계산하여 저장하는 배열 생성
    prefix = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]
    return prefix

def sum_in_range(prefix, a1, a2):
    # 구간 합 계산
    return prefix[a2] - prefix[a1 - 1]

# 입력
n, m = map(int, input().split())
A = list(map(int, input().split()))

# 수열 A의 누적 합 계산
prefix = prefix_sum(A)

# 구간 합 계산 및 출력
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum_in_range(prefix, a1, a2))