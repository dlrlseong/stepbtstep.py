student = []
for i in range(1, 31):
    student.append(i)

for i in range(0, 28):
    submit = int(input())
    student.remove(submit)

for i in student:
    print(i, end=' ')