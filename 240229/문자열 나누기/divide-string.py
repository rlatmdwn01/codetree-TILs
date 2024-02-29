n=int(input())

num_list=list((input().split()))

new_str="".join(num_list)

for i in range(len(new_str)):
    if (i+1)%5!=0:
        print(new_str[i],end='')
    else:
        print(new_str[i])