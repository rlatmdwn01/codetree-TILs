a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=a*b*c

def sum_num(n):
    if n<10:
        return n
    return sum_num(n//10)+(n%10)

print(sum_num(d))