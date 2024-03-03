str1,str2=input().split()

str1_list=list(str1)
str2_list=list(str2)
num1=""
num2=""

for i in str1_list:
    if i.isdigit()==True:
        num1+=i
    else:
        break

for j in str2_list:
    if j.isdigit()==True:
        num2+=j
    else:
        break

num1=int(num1)
num2=int(num2)

print(num1+num2)