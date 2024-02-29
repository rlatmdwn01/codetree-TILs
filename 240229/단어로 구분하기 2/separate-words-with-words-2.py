word=tuple(input().split())

n=len(word)

if n%2==0:
    for i in range(n):
        if i%2==0:
            print(word[i], end='\n')

else:
    for i in range(n):
        if i%2==0:
            print(word[i], end='\n')