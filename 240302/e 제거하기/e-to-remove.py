word=input()
n=len(word)
cnt=1
str_list=list(word)

for i in range(n):
    if cnt==1:
        if str_list[i]=='e':
            str_list.pop(i)
            cnt-=1
    else:
        break

print(''.join(str_list))