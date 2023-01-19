a = []
b = []
for i in range(10):
    a.append(int(input()))

for i in range(0, 10):
    n = a[i] % 42
    if b.__contains__(n):
        continue
    else:
        b.append(n)

print(len(b))
