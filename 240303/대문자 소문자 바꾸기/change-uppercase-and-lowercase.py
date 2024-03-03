word=input()
str_list=list(word)

for i in str_list:
    if 'A'<=i<='Z':
        print(i.lower(),end='')
    elif 'a'<=i<='z':
        print(i.upper(),end='')