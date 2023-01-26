S = input()
S = S.upper()
max_count = 0
max_chr = ''
max_flag = False

for i in range(ord('A'), ord('Z') + 1):
    cnt = S.count(chr(i))
    if cnt == max_count and max_chr != i:
        max_flag = True
    if cnt > max_count:
        max_flag = False
        max_chr = i
        max_count = cnt

if max_flag == True:
    print('?')
else:
    print(max_chr)
