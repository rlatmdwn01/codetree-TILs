n1, n2 = list(map(int, input().split()))
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

cnt = arr_a.count(arr_b[0])
idx = 0
true_false = False

for _ in range(cnt):
    # a배열 중 b[0] 원소부터 len(b) 만큼의 원소를 집어넣기 위한 배열 초기화
    arr_a1 = []
    # a배열 중 b[0] 원소의 index를 찾음
    for elem in arr_a[idx:]:
        if elem == arr_b[0]:
            break
        idx += 1
    # a배열 중 b[0] 원소부터 len(b) 만큼의 원소들을 a1배열에 집어넣음
    for elem in arr_a[idx:idx + len(arr_b)]:
        arr_a1.append(elem)
    # 생성한 a1배열과 b 배열이 일치하는지 확인
    if arr_a1 == arr_b:
        true_false = True
        break
    # a배열 중 앞쪽 b[0] 원소와는 불일치 했으므로 뒤쪽에 있는 b[0] 원소를 더 찾음
    idx += 1

print("Yes" if true_false else "No")