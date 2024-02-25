# n개 원소
# q개 질의
# 1번 질의 a : a번째 원소 출력(배열 n)
# 2번 질의 a : 숫자 a가 있는지 판단 -> 있을 경우 몇 번 째 원소? -> 없을 경우 0 출력
# 3번 질의 a b : a번째 원소부터 b번째 원소까지 순서대로 출력

# 첫 줄 : n(배열길이) q
# 둘째줄 : n개의 원소
# 셋째 줄 : q개의 질의

n, q = map(int, input().split())
arr = list(map(int, input().split()))

# n = 3
# q = 1
# arr = [1, 8, 5]
for i in range(q) :
    questions = list(map(int, input().split()))
    #questions = [1, 1]
    q_type= questions[0]
    a = questions[1]

    if q_type == 1 :
        if a <= len(arr) :
            print(arr[a - 1])
        else :
            print(0)
    elif q_type == 2 :
        if a in arr :
            print(arr.index(a) + 1)
        else :
            print(0)
    else : 
        b = questions[2]
        for j in range(a-1, b) :
            print(arr[j], end = ' ')
            print()