n,m=input().split()

n=int(n)
m=int(m)

num_list=[n,m]

for i in range(2,10):
    num_list.append(2*num_list[-2]+num_list[-1])

for j in num_list:
    print(j, end=' ')