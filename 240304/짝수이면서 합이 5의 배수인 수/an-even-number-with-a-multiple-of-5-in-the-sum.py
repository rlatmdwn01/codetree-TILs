def is_magic_number(N):
    return N%2==0 and (int(N//10)+int(N%10))%5==0

N=int(input())
if is_magic_number(N):
    print('Yes')
else:
    print('No')