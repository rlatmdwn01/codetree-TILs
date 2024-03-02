A,B=input().split()

sum_val=ord(A)+ord(B)

if ord(A)>ord(B):
    print(sum_val,ord(A)-ord(B))
else:
    print(sum_val,ord(B)-ord(A))