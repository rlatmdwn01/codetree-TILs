def min_max_group_sum(N, numbers):
    numbers.sort()  # 입력된 숫자들을 정렬합니다.
    max_sum = 0
    for i in range(N):
        max_sum = max(max_sum, numbers[i] + numbers[2*N-1-i])  # 각 그룹의 합 중 최댓값을 업데이트합니다.
    return max_sum

# 입력 처리
N = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(min_max_group_sum(N, numbers))