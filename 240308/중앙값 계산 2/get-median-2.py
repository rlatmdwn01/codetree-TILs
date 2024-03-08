import heapq

def find_median(n, numbers):
    min_heap = []  # 중앙값을 찾기 위한 최소 힙
    max_heap = []  # 중앙값을 찾기 위한 최대 힙
    result = []

    for i in range(n):
        num = numbers[i]
        # 최소 힙과 최대 힙에 숫자를 번갈아가며 넣습니다.
        if i % 2 == 0:
            heapq.heappush(max_heap, -num)  # 최대 힙에는 음수로 저장하여 최대값을 얻을 수 있도록 합니다.
            if min_heap and -max_heap[0] > min_heap[0]:
                max_val = -heapq.heappop(max_heap)
                min_val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_val)
                heapq.heappush(min_heap, max_val)
        else:
            heapq.heappush(min_heap, num)
            if -max_heap[0] > min_heap[0]:
                max_val = -heapq.heappop(max_heap)
                min_val = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -min_val)
                heapq.heappush(min_heap, max_val)
        # 중앙값을 결과에 추가합니다.
        if i % 2 == 0:
            result.append(str(-max_heap[0]))
    return ' '.join(result)

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(find_median(n, numbers))