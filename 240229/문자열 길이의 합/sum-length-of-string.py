n=int(input())
arr=[]

for word in range(n):
    word=input()
    arr.append(word)

sum_val=0
cnt=0

for word in arr:
    sum_val+=len(word)
    if 'a' in word:
        cnt+=1

print(sum_val,cnt)