arr = [[0]*2001 for _ in range(2001)]
area = 0

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1+1000, x2+1000):
    for j in range(y1+1000, y2+1000):
        arr[i][j] += 1
x3, y3, x4, y4 = map(int, input().split())
for i in range(x3+1000, x4+1000):
    for j in range(y3+1000, y4+1000):
        arr[i][j] += 1

x5, y5, x6, y6 = map(int, input().split())
for i in range(x5+1000, x6+1000):
    for j in range(y5+1000, y6+1000):
        arr[i][j] -= 1

for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            area += 1

print(area)