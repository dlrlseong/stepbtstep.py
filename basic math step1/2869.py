import math
A, B, V = map(int, input().split())
V = V - A
n = math.ceil(V / (A-B))
print(n+1)
