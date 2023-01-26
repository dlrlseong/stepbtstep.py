N = int(input())

for _ in range(N):
    TestCase = list(map(int, input().split()))
    TestCase.remove(TestCase[0])
    Average = sum(TestCase) / len(TestCase)
    numberOfStudents = len(TestCase)
    cnt = 0
    for test in TestCase:
        if test > Average:
            cnt += 1
    answer = cnt/numberOfStudents*100
    # print("%.3f%%" % (cnt/numberOfStudents*100))
    print(f"{answer:.3f}%")
