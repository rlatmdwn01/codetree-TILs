def max_sign_subarray_length(n, numbers):
    max_length = 0
    current_length = 0
    prev_sign = None

    for number in numbers:
        if number == 0:
            current_length = 0
            prev_sign = None
        else:
            if prev_sign is None or (number > 0 and prev_sign > 0) or (number < 0 and prev_sign < 0):
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 1
            prev_sign = number

    return max_length

# 입력 받기
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 결과 출력
print(max_sign_subarray_length(n, numbers))