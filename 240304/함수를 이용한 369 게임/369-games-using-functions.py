def write_3(n):
    return '3' in list(str(n)) or '6' in list(str(n)) or '9' in list(str(n))

def judge_3(n):
    return n%3==0 or write_3(n)

cnt=0

a,b=input().split()
a=int(a)
b=int(b)
for i in range(a,b+1):
    if judge_3 (i):
        cnt+=1

print(cnt)