def calculator(i,j,k):
    i=int(i)
    k=int(k)
    if j=='+':
        return i+k
    elif j=='-':
        return i-k
    elif j=='/':
        return int(i/k)
    elif j=='*':
        return i*k
    else:
        return False

a,b,c=input().split()
if b=='+' or b=='-' or b=='/' or b=='*':
    print("{0} {1} {2} = {3}".format(a,b,c,calculator(a,b,c)))
else:
    print(calculator(a,b,c))