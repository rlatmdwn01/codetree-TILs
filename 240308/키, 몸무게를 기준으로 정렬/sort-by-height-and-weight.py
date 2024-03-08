class info():
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

people=[]
n=int(input())
for _ in range(n):
    name,height,weight=input().split()
    height=int(height)
    weight=int(weight)

    people.append(info(name,height,weight))

people.sort(key=lambda x: (x.height,-x.weight))

for person in people:
    print(person.name,person.height, person.weight)