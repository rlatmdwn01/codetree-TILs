class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

# 입력 처리
N = int(input())
students = []
for i in range(N):
    height, weight = map(int, input().split())
    students.append(Student(height, weight, i + 1))

# 규칙에 따라 정렬
students.sort(key=lambda x: (-x.height, -x.weight, x.number))

# 결과 출력
for student in students:
    print(student.height, student.weight, student.number)