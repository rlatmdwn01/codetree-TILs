N,B=input().split()
N=int(N)
B=int(B)
left_nums=[]


if B==4:
    while True:
        if N<4:
            left_nums.append(N)
            break
        left_nums.append(N%4)
        N//=4

elif B==8:
    while True:
        if N<8:
            left_nums.append(N)
            break
        left_nums.append(N%8)
        N//=8

for digit in left_nums[::-1]:
    print(digit,end='')