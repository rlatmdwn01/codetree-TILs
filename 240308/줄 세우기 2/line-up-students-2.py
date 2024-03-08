class Student:
    def __init__(self, height, weight, index):
        self.height = height
        self.weight = weight
        self.index = index

# 입력 처리
N = int(input())
students = []
for i in range(N):
    h, w = map(int, input().split())
    students.append(Student(h, w, i + 1))

# 키를 기준으로 정렬하되, 키가 같으면 몸무게를 기준으로 정렬
sorted_students = sorted(students, key=lambda x: (x.height, -x.weight))

# 출력
for student in sorted_students:
    print(student.height, student.weight, student.index)