arr=[]

for _ in range(10):
    word=input()
    arr.append(word)

n=input()

for string in arr:
    if string[-1]==n:
        print(string,end='\n')
    else:
        print('None')