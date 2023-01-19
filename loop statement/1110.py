n = int(input())
answer = n
cnt = 0

while True:
    if n < 10:
        cnt += 1
        n = n*10 + n
        if n == answer:
            break
    else:
        cnt += 1
        n = (n % 10)*10+((n//10)+(n % 10)) % 10
        if n == answer:
            break
        
print(cnt)
