word=input()
n=len(word)
arr=list(word)
cnt=n

while cnt>1:
    m=int(input())

    if m>n:
        arr.pop(-1)
        print(''.join(arr))
        cnt-=1
    else:
        arr.pop(m)
        print(''.join(arr))
        cnt-=1