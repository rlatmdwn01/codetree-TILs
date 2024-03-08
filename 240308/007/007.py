class member:
    def __init__(self,secret,place,time):
        self.secret=secret
        self.place=place
        self.time=time

n,m,k=input().split()
member1=member(n,m,k)

print("secret code :",member1.secret)
print("meeting point :",member1.place)
print("time :",member1.time)