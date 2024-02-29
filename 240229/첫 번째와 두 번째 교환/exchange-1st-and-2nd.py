word=input()

n=word[0]
m=word[1]

w_list=list(word)

for i in range(len(w_list)):
    if w_list[i]==n:
        w_list[i]=m
    elif w_list[i]==m:
        w_list[i]=n

print(''.join(w_list))