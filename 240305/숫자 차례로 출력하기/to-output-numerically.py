def print_numbers_from_1_to_N(curr, N):
    if curr > N:
        return
    print(curr, end=" ")
    print_numbers_from_1_to_N(curr + 1, N)

def print_numbers_from_N_to_1(curr, N):
    if curr < 1:
        return
    print(curr, end=" ")
    print_numbers_from_N_to_1(curr - 1, N)

# 입력
N = int(input())

# 첫 번째 재귀 함수 호출하여 1부터 N까지 출력
print_numbers_from_1_to_N(1, N)
print()

# 두 번째 재귀 함수 호출하여 N부터 1까지 출력
print_numbers_from_N_to_1(N, N)