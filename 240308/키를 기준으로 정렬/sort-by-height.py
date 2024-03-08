class info:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

person=[]
n=int(input())

for _ in range(n):
    name,height,weight=input().split()
    height=int(height)
    weight=int(weight)
    person.append(info(name,height,weight))

person.sort(key=lambda x: x.height)

for member in person:
    print(member.name,member.height,member.weight)