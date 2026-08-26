def sqare(num):
        res = 0
        while num > 0:
            dig = num % 10
            res = res + dig ** 2
            num = num // 10
        return res
    
def happy_num(num):
    while num > 9:
        num = sqare(num)
    if num == 1 or num == 7:
         return "happy no"
    return "not a happy number"
    

num = 192
print(happy_num(num))