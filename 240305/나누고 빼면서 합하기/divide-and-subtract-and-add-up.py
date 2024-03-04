n,m=input().split()
n=int(n)
m=int(m)
A_list=list(map(int,input().split()))

def divide_and_sum(n,m):
    sum_val=0
    while m>=1:
        if m==1:
            sum_val+=A_list[0]
            break
        else:
            if m%2==1:
                sum_val+=A_list[m-1]
                m-=1
            else:
                sum_val+=A_list[m-1]
                m=int(m//2)

    return sum_val

print(divide_and_sum(n,m))