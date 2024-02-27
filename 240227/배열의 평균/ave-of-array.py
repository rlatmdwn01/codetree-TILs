arr2d=[
    list(input().split())
    for _ in range(2)
]

#가로 평균
for i in range(2):
    sum_val=0
    for j in range(4):
        sum_val+=int(arr2d[i][j])
    print((sum_val/4),end=' ')

print()

#세로 평균
for i in range(4):
    sum_val=0
    for j in range(2):
        sum_val+=int(arr2d[j][i])
    print((sum_val)/2,end=' ')

print()

#전체 평균
sum_val=0
for i in range(4):
    for j in range(2):
        sum_val+=int(arr2d[j][i])
print(sum_val/8)