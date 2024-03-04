A=input()
n=len(A)
str_list=list(A)

def palindrome(A):
    for i in range(int(n//2)):
        if str_list[i]==str_list[n-1-i]:
            return True
    return False


if palindrome(A):
    print('Yes')
else:
    print('No')