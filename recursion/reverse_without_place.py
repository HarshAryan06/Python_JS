def Reverse(num,res):
    if num == 0:
        return res
    return Reverse(num // 10,res * 10 + (num % 10))

num = 234
res = 0
print(Reverse(num,res))

