n=input()

word_list=["apple", "banana", "grape", "blueberry", "orange"]
cnt=0
for word in word_list:
    if word[2]==n or word[3]==n:
        print(word)
        cnt+=1

print(cnt)