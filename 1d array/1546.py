N = int(input())
score = list(map(int, input().split()))
max_score = max(score)

for i in range(N):
    score[i] = score[i] / max_score * 100

print(sum(score) / N)

# n = int(input())
# arr = list(map(int,input().split()))
# print((sum(arr)/max(arr)*100)/n)