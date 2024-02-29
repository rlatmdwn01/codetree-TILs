arr=[]

for _ in range(10):
    word=input()
    arr.append(word)

n=input()
cnt=0

for string in arr:
    if string[-1]==n:
        print(string,end='\n')
    else:
        cnt+=1
        if cnt==len(arr):
            print('None')