binary=input()

#2진수를 10진수로
binary=list(binary)
n=len(binary)
num = 0

for i in range(n):
    num = num * 2 + int(binary[i])

#10진수를 2진수로
left_nums=[]
num*=17

while True:
    if num<2:
        left_nums.append(num)
        break
    left_nums.append(num%2)
    num//=2


for digit in left_nums[::-1]:
    print(digit,end='')