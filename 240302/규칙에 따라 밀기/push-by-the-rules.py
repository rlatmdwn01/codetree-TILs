A=input()
A_list=list(A)
str_size=len(A)
q_str=input()
q_list=list(q_str)

for i in q_list:
    if i=='L':
        front=A_list[0]
        for i in range(1,str_size):
            A_list[i-1]=A_list[i]
        A_list[str_size-1]=front
    elif i=='R':
        back=A_list[str_size-1]
        for i in range(str_size-1,0,-1):
            A_list[i]=A_list[i-1]
        A_list[0]=back

print("".join(A_list))