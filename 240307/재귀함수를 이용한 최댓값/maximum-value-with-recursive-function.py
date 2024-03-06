def find_max_recursive(arr, n):
    # 리스트에 하나의 원소만 남았을 때 그 값을 반환합니다.
    if n == 1:
        return arr[0]
    else:
        # 현재 원소와 재귀적으로 찾은 나머지 리스트의 최댓값을 비교하여 반환합니다.
        return max(arr[n-1], find_max_recursive(arr, n-1))

# 입력 처리
n = int(input())
elements = list(map(int, input().split()))

# 최댓값 찾기
max_value = find_max_recursive(elements, n)

# 결과 출력
print(max_value)