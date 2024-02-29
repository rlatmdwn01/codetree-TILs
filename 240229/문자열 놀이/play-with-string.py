s,q=input().split()
q=int(q)
s_list=list(s)

for i in range(q):
    a,b,c=input().split()
    a=int(a)

    if a==1:
        b=int(b)
        c=int(c)
        t=s_list[b-1]
        s_list[b-1]=s_list[c-1]
        s_list[c-1]=t
        print(''.join(s_list))

    elif a==2:
        for i in range(len(s_list)):
            if s_list[i]==b:
                s_list[i]=c
        print(''.join(s_list))