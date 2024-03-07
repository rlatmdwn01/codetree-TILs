n=int(input())
str_list=[]

for _ in range(n):
    word=input()
    str_list.append(word)

str_list.sort()

for i in str_list:
    print(i)