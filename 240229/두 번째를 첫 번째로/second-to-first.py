word=input()
change=word[0]
normal=word[1]
word_list=list(word)
n=len(word_list)

for i in range(1,n):
    if word_list[i]==normal:
        word_list[i]=change

print(''.join(word_list))