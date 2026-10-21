num = 145
res = 0

for i in str(num):
    fact = 1
    for j in range(1,int(i) + 1):
        fact = fact * j
    res = res + fact
print(res)