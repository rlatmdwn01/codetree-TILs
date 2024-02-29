s,q=input().split()
q=int(q)

for i in range(q):
    a,b,c=input().split()
    a=int(a)

    if a==1:
        b=int(b)
        c=int(c)
        s_list=list(s)
        t=s_list[b-1]
        s_list[b-1]=s_list[c-1]
        s_list[c-1]=t
        print(''.join(s_list))

    elif a==2:
        s_list=list(s)
        for i in s_list:
            if i==b:
                i=c
        print(''.join(s_list))