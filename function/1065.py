def is_Hansu (n):
    if n < 10:
        return True
    
    A = set()
    while n>=10:
        a = n % 10
        b = (n//10) % 10
        n = n //10
        A.add(a - b)
    
    if len(A) == 1:
        return True
    else:
        return False

X = int(input())
cnt = 0
for i in range(1, X+1):
    if is_Hansu(i) == True:
        cnt += 1
        
print(cnt)