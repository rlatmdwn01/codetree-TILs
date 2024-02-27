n,m=input().split()
n=int(n)
m=int(m)

num_list=[[0 for _ in range(m)]
for _ in range(n)
]

intial_num=1

for i in range(n):
    for j in range(m):
        num_list[i][j]=intial_num
        intial_num+=1

for i in range(n):
    for j in range(m):
        print(num_list[i][j], end=' ')
    print()