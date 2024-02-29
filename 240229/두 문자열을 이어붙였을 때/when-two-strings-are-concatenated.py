first_str=input()
second_str=input()

third_str=first_str+second_str
fourth_str=second_str+first_str

n=len(third_str)
m=len(fourth_str)

if n==m:
    print('true')
else:
    print('false')