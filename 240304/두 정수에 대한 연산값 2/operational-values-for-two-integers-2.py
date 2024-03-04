a,b=input().split()
a=int(a)
b=int(b)

def sum_two_nums(a,b):
    if a>b:
        a=a*2
        b=b+10
    else:
        a=a+10
        b=b*2
    return a,b

arr=sum_two_nums(a,b)
for elem in arr:
    print(elem, end=' ')