# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
	
# b부터 a까지 감소하며 짝수의 구구단을 출력합니다.
for i in range(1, 10):
	for j in range(b, a-1, -1):
		if j % 2 == 0:
			print(f"{j} * {i} = {i * j}", end="")
			if j != a:
				print(" / ", end="");
	print()