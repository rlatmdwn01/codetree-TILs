while True:
    n=input()
    if n=='END':
        break
    else:
        for i in range(len(n)-1,-1,-1):
            print(n[i],end='')
        print()