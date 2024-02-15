a,b=input().split()
c,d=input().split()
e,f=input().split()

b=int(b)
d=int(d)
f=int(f)



if a=='Y':
    if b>=37:
        a='A'
    else:
        a='C'
elif a=='N':
    if b>=37:
        a='B'
    else:
        a='D'

if c=='Y':
    if d>=37:
        c='A'
    else:
        c='C'
elif c=='N':
    if d>=37:
        c='B'
    else:
        c='D'

if e=='Y':
    if f>=37:
        e='A'
    else:
        e='C'
elif e=='N':
    if f>=37:
        e='B'
    else:
        e='D'

if (a=='A' and c=='A' and e=='A') or (a=='A' and c=='A') or (a=='A' and e=='A') or (c=='A' and e=='A'):
    print('E')
else:
    print('N')