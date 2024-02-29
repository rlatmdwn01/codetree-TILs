word=input()
n=len(word)
new_word=""

for i in range(n):
    if i%2==1:
        new_word+=word[i]

for j in range(len(new_word)-1,-1,-1):
    print(new_word[j],end='')