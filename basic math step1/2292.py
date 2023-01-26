n = int(input())
for i in range(1, 1000000):
    tmp = 1
    an = 1 + 3*i*(i-1)
    if n <= an:
        print(i)
        break