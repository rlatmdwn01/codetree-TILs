n=int(input())

arr=[]

for i in range(n):
    word=input()
    arr.append(word)

m=input()
cnt=0
new_list=[]

for word in arr:
    if word[0]==m:
        cnt+=1
        new_list.append(word)

sum_val=0

for word in new_list:
    sum_val+=len(word)
j=len(new_list)

print(cnt,"%.2f"%(sum_val/j))