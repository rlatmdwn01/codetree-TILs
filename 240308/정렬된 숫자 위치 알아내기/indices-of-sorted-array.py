n=int(input())
lst = list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    a.append((lst[i],i+1))
a.sort(key=lambda x:(x[0],x[1]))
for i in range(n):
    b.append((a[i][1], i+1))
b.sort(key=lambda x:x[0])
print(" ".join(str(i[1]) for i in b))