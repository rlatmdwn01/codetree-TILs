num_list=[[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    num_list[0][i]=1

for i in range(5):
    num_list[i][0]=1

for i in range(1,5):
    for j in range(1,5):
        num_list[i][j]=num_list[i-1][j]+num_list[i][j-1]
        

for i in range(5):
    for j in range(5):
        print(num_list[i][j],end=' ')
    print()