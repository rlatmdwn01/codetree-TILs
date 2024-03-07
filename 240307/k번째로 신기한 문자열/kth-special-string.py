def find_kth_word(T, k, words):
    # 문자열 T로 시작하는 단어들을 추출합니다.
    starting_with_T = [word for word in words if word.startswith(T)]
    # 사전순으로 정렬합니다.
    starting_with_T.sort()
    # k번째 단어를 반환합니다.
    return starting_with_T[k - 1]

# 입력 처리
n, k, T = input().split()
n = int(n)
k = int(k)
words = [input() for _ in range(n)]

# 결과 출력
print(find_kth_word(T, k, words))