c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
y = len(s)
for i in c:
    if s.find(i) != -1:
        y -= (len(i) - 1) * s.count(i)
        s = s.replace(i,'.'*len(i))
print(y)