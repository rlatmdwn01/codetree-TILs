def min_shift_to_match(a, b):
    if a == b:
        return 0
    
    len_a = len(a)
    len_b = len(b)
    
    # 문자열 A를 우측으로 한 칸씩 밀었을 때, 문자열 A와 B가 같아지는 경우를 찾음
    for shift in range(1, len_a + 1):
        shifted_a = a[-shift:] + a[:-shift]  # 문자열 A를 우측으로 shift 만큼 밀기
        if shifted_a == b:
            return shift
    
    return -1  # 불가능한 경우

# 입력
string_a = input().strip()
string_b = input().strip()

# 결과 출력
result = min_shift_to_match(string_a, string_b)
print(result)