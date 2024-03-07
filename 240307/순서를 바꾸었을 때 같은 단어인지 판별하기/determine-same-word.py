word1=input()
word2=input()

str1_list=list(word1)
str2_list=list(word2)

str1_list.sort()
str2_list.sort()

if str1_list==str2_list:
    print('Yes')
else:
    print('No')