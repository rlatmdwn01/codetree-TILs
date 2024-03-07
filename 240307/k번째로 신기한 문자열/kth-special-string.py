n,k,T=input().split()
n=int(n)
k=int(k)
str_list=[]

for i in range(n):
    word=input()
    if T in word:
        str_list.append(word)

str_list.sort()

print(str_list[k-1])