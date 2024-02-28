word1,word2=input().split()

length1=len(word1)
length2=len(word2)

if length1>length2:
    print(word1,length1)
elif length2>length1:
    print(word2,length2)
else:
    print('same')