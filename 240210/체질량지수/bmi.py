a,b=map(int,input().split())

BMI=b/((a*0.01)**2)
print(int(BMI))

if BMI>=25:
    print("Obesity")