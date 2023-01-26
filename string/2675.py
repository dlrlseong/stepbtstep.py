n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    answer = str()
    for i in b:
        for j in range(int(a)):
            answer += i

    print(answer)
