n=int(input())

num_list=[1,n]

print(1, end=' ')
print(n, end=' ')

for i in range(2,11):
    num_list.append(num_list[-2]+num_list[-1])
    print(num_list[-1], end=' ')
    if num_list[-1]>100:
        break