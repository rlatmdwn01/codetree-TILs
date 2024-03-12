def find_revisited_area(n, commands):
    position = 0
    visited = set()
    revisited = set()
    
    for command in commands:
        distance, direction = command.split()
        distance = int(distance)
        
        for _ in range(distance):
            if direction == "R":
                position += 1
            elif direction == "L":
                position -= 1
            
            if position in visited:
                revisited.add(position)
            visited.add(position)

    return len(revisited)

# 입력을 받습니다.
n = int(input())
commands = [input() for _ in range(n)]

# 결과를 출력합니다.
print(find_revisited_area(n, commands))