import sys
for i in range(0, int(input())):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')