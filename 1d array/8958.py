N = int(input())

for i in range(N):
    score = 0
    answer  = input().split('X')
    for Os in answer:
        if len(Os) != 0:
            tmp = 0
            for j in range(len(Os)):
                tmp += 1
                score += tmp
    print(score)
