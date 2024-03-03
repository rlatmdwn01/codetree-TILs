word=input()
str_list=list(word)

for i in str_list:
    if i.isalpha()==True or i.isdigit()==True:
        print(i.lower(),end='')