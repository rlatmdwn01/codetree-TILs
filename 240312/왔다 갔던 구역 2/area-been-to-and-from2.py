def find_revisited_area(n, commands):
    position = 0
    visited = set()
    revisited = set()

    for command in commands:
        distance, direction = command.split()
        distance = int(distance)
        
        # 이동 방향에 따라 위치를 업데이트하고 방문한 위치를 기록합니다.
        for _ in range(distance):
            if direction == "R":
                position += 1
            elif direction == "L":
                position -= 1
            
            # 현재 위치가 이미 방문한 위치라면 revisited에 추가합니다.
            if position in visited:
                revisited.add(position)
            visited.add(position)

    return len(revisited)

# 입력을 받습니다.
n = int(input())
commands = [input() for _ in range(n)]

# 결과를 출력합니다.
print(find_revisited_area(n, commands))