A = int(input())
B = int(input())
print(A*(B % 10))
print(A*((B // 10) % 10))
print(A*(B // 100))
print(A*B)

# a = int(input())
# b = input()
# for i in b[::-1]:
#     print(a*int(i))
# print(a*int(b))