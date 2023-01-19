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

# n=[0 for i in range(42)]
# for _ in range(10):
#   a=int(input())
#   n[a%42]=1
# ans=0
# for i in n:
#   if i==1:
#     ans+=1
# print(ans)