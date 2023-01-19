total = int(input())
sum = 0
for i in range(0, int(input())):
    A, B = map(int, input().split())
    sum += A * B

print('Yes') if sum == total else print ('No')