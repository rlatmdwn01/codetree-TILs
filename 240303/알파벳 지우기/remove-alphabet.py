word1=input()
word2=input()

str1_list=list(word1)
str2_list=list(word2)

num1=""
num2=""

for i in str1_list:
    if i.isdigit()==True:
        num1+=i

for j in str2_list:
    if j.isdigit()==True:
        num2+=j

print(int(num1)+int(num2))