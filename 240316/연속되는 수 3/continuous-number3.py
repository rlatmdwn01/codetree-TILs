n = int(input())
cnt = 0
result = 0
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)
    
for i in range(n):
    if arr[i]>0:
        cnt += 1
    
    else:
        result = max(cnt, result)
        cnt = 0
        
    result = max(cnt, result)

print(result)