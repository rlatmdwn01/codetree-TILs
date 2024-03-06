def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_recursive(arr, n):
    if n == 1:
        return arr[0]
    else:
        return lcm(arr[n-1], lcm_recursive(arr, n-1))

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 최소공배수 구하기
result = lcm_recursive(numbers, n)

# 결과 출력
print(result)