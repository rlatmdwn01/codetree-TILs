class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

# n명의 사람 객체 생성
n = int(input())
people = []
for _ in range(n):
    name, address, city = input().split()
    people.append(Person(name, address, city))

# 사전순으로 이름이 가장 느린 사람 찾기
slowest_person = max(people, key=lambda x: x.name)

# 결과 출력
print("name", slowest_person.name)
print("addr", slowest_person.address)
print("city", slowest_person.city)