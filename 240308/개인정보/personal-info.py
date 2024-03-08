class info():
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

people=[]
for _ in range(5):
    name,height,weight=input().split()
    height=int(height)
    weight=float(weight)

    people.append(info(name,height,weight))

people.sort(key=lambda x: x.name)

print('name')
for person in people:
    print(person.name,person.height, person.weight)
print()

people.sort(key=lambda x: -x.height)

print('height')
for person in people:
    print(person.name,person.height, person.weight)