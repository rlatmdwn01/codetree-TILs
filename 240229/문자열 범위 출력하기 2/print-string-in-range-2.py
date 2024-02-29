word=input()
n=int(input())

if len(word)<n:
    print(word)

else:
    for i in range(len(word)-1,len(word)-n-1,-1):
        print(word[i],end='')