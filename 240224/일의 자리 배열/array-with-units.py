n,m=input().split()
n=int(n)
m=int(m)

num_list=[n,m]

for i in range(2,10):
    if (num_list[-1]+num_list[-2])%20==0:
        num_list.append(num_list[-1]+num_list[-2])
    else:
        num_list.append((num_list[-1]+num_list[-2])%10)

for i in num_list:
    print(i, end=' ')