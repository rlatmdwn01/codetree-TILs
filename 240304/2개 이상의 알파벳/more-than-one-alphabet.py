word=input()
n=len(word)
str_list=list(word)

def two_alphabet(word):
    cnt=0
    for i in range(n-1):
        if str_list[i]==str_list[i+1]:
            cnt+=1

    if cnt+1==n:
        return False
    return True

if two_alphabet(word):
    print('Yes')
else:
    print('No')