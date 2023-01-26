n = int(input())
for i in range(n):
    H, W, N = map(int, input().split())
    h = N % H
    if h == 0:
        h = H
        w = N//H
    else:
        w = N // H + 1
    if w < 10:
        print(f'{h}0{w}')
    else:
        print(f'{h}{w}')

# n = int(input())
# for i in range(n):
#     h,w,m = map(int,input().split())
#     print(((m-1)%h+1)*100+(m-1)//h+1)