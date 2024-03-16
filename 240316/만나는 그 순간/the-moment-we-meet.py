N, M = map(int, input().split())

pathA = []
pathB = []

for i in range(N):
    direction, length = input().split()
    length = int(length)
    pathA.append((direction, length))

for i in range(M):
    direction, length = input().split()
    length = int(length)
    pathB.append((direction, length))


def get_trace(path):
    ret = []
    cur = 0
    for direction, length in path:
        if direction == 'L':
            for _ in range(length):
                cur -= 1
                ret.append(cur)
        if direction == 'R':
            for _ in range(length):
                cur += 1
                ret.append(cur)
    return ret


traceA = get_trace(pathA)
traceB = get_trace(pathB)

total_length = len(traceA)
ans = -1
for i in range(total_length):
    if traceA[i] == traceB[i]:
        ans = i + 1
        break

print(ans)