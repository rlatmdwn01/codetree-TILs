A=input()
str_list=list(A)
sum_val=0

for i in str_list:
    if i.isdigit()==True:
        sum_val+=int(i)

print(sum_val)