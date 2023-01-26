cnt = 0
a = int(input())
for _ in range(0, a):
    s = input()
    cnt += 1
    for i in range(0, len(s)-1):
        if s[i+1:].find(s[i]) == -1:
            continue
        else:
            if s[i+1] != s[i]:
                cnt -= 1
                break
        
print(cnt)