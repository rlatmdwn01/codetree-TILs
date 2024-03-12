n = int(input())
checked_index = [0] * 200001
current_index = 100000
color_checked = ['N'] *200001 

def move(step, direction, current_index):
    if direction == 'R':
        for i in range(current_index, current_index+step):
            color_checked[i] = 'B'
            checked_index[i]+=1
        return current_index+step-1
    
    elif direction == "L":
        for i in range(current_index, current_index - step, -1):
            color_checked[i] = 'W'
            checked_index[i]+=1
        return current_index - step +1

instructions =[]
for _ in range(n):
    step, direction = tuple(input().split())
    instructions.append((int(step), direction))

for step, direction in instructions:
    current_index = move(step, direction, current_index)


for i in range(len(checked_index)):
    if checked_index[i] >= 4:
        color_checked[i] = "G"

print(color_checked.count("W"), color_checked.count("B"), color_checked.count("G"))