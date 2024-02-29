first_str=input()
second_str=input()

third_str=first_str+second_str
fourth_str=second_str+first_str

if third_str==fourth_str:
    print('true')
else:
    print('false')