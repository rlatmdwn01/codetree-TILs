def day_correct(M,D):
    if 1<=M<=7:
        if M%2==1:
            if 1<=D<=31:
                return True
            else:
                return False
        elif M%2==0 and M!=2:
            if 1<=D<=30:
                return True
            else:
                return False
    elif 8<=M<=12:
        if M%2==0:
            if a<=D<=31:
                return True
            else:
                return False
        elif M%2==1:
            if 1<=D<=31:
                return True
            else:
                return False
    elif M==2:
        if 1<=D<=28:
            return True
        else:
            return False

a,b=tuple(map(int,input().split()))
if day_correct(a,b):
    print('Yes')
else:
    print('No')