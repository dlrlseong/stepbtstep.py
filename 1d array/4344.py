N = int(input())

for _ in range(N):
    TestCase = list(map(int, input().split()))
    TestCase.remove(TestCase[0])
    Average = sum(TestCase) / len(TestCase)
    numberOfStudents = len(TestCase)
    TestCase.sort()
    print(TestCase)