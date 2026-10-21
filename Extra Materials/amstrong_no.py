# n = 153
# l = len(str(n))
# res = 0

# for i in str(n):
#     power = int(i) ** l
#     res = res + power
# # print(res)

# if res == n:
#     print("amstrong_no")
# else :
#     print("not a amstrong number")

'''
l = ['hello', 227, 3.4, 'last', 189, 34]
out = []

for i in l:
    if type(i) == int:
        rev = int(str(i)[::-1])
        out.append(rev)
print(out)

'''

num = 145
res = 0

for i in str(num):
    fact = 1

    for j in range(1,int(i) + 1):
        fact = fact * j

    res = res + fact
print(res)