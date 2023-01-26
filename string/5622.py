def ABC_to_123(c):
    if c < ord('D'):
        return 2
    elif c < ord('G'):
        return 3
    elif c < ord('J'):
        return 4
    elif c < ord('M'):
        return 5
    elif c < ord('P'):
        return 6
    elif c < ord('T'):
        return 7
    elif c < ord('W'):
        return 8
    else:
        return 9


A = input()
answer = 0

for n in A:
    answer += (ABC_to_123(ord(n)) + 1)

print(answer)

# d = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# print(sum(d.index(b)+3 for a in input() for b in d if b.find(a)>=0))