n=int(input())

num_list=[1,n]

for i in range(2,21):
    num_list.append(num_list[-2]+num_list[-1])

for i in num_list:
    print(i, end=' ')
    if i>100:
        break