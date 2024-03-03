# 문자열을 입력받습니다.
a = input()
b = input()
	
leng = len(a)
cnt = 0
	
# 문자열 a를 우측으로 한 칸씩 밀어보면서 문자열 b와 같아지는지 확인합니다.
for i in range(leng):
    # 문자열을 오른쪽으로 한 칸 쉬프트합니다.
    a = a[leng - 1] + a[:leng - 1]

    cnt += 1
    
    # 문자열이 같을 경우 민 횟수를 출력합니다.
    if a == b:
        print(cnt)
        break

    # 만약 불가능하다면 -1을 출력합니다.
    if i == leng - 1: print("-1")