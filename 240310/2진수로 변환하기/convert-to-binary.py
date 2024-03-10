n=int(input())
left_nums=[]

while True:
    if n<2:
        left_nums.append(n)
        break
    left_nums.append(n%2)
    n//=2


for digit in left_nums[::-1]:
    print(digit,end='')