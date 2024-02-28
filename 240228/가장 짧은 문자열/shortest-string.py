str1=input()
str2=input()
str3=input()

length1=len(str1)
length2=len(str2)
length3=len(str3)

len_list=[]

len_list.append(length1)
len_list.append(length2)
len_list.append(length3)

print(max(len_list)-min(len_list))