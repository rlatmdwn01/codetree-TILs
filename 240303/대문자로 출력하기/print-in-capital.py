word=input()
str_list=list(word)

for i in str_list:
    if i.isalpha()==True:
        print(i.upper(),end='')