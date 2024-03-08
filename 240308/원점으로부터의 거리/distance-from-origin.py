class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.distance = abs(x) + abs(y)

# 입력 처리
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append(Point(x, y, i + 1))

# 거리에 따라 정렬
points.sort(key=lambda p: (p.distance, p.index))

# 결과 출력
for point in points:
    print(point.index)