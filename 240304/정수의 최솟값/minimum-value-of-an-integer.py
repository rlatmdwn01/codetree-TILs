def min_val(a,b,c):
    num_list=[a,b,c]
    return min(num_list)

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

min_val=min_val(a,b,c)

print(min_val)