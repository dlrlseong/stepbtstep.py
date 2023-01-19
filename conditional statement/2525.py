H, M = map(int, input().split())
TIME = H * 60 + M
TIME = TIME + int(input())
print((TIME//60) % 24, TIME % 60)
