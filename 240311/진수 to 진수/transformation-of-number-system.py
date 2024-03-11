def convert_base(n, base):
    # 10진수 수를 base진수로 변환하는 함수
    result = ''
    while n > 0:
        remainder = n % base
        result = str(remainder) + result
        n //= base
    return result

# 입력 받기
a, b = map(int, input().split())
n = int(input())

# a진수를 10진수로 변환
decimal_value = int(str(n), a)

# 10진수를 b진수로 변환
result = convert_base(decimal_value, b)

# 결과 출력
print(result)