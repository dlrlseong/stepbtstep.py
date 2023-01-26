n = int(input())
tmp = 0
for i in range(1, 100001):
    tmp += i
    if tmp >= n:
        break
if i % 2 == 1:
    print(f'{tmp-n+1}/{i-(tmp-n)}')
else:
    print(f'{i-(tmp-n)}/{1+(tmp-n)}')