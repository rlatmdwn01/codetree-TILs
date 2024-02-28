str1=input()
str2=input()

empty_list=[]

for i in str1:
    if i!=' ':
        empty_list.append(i)

for i in str2:
    if i!=' ':
        empty_list.append(i)

for i in empty_list:
    print(i, end='')