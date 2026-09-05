def happy_num(num):
    if num < 10:
        if num == 1 or num == 7:
            return "happy no"
        return "not a happy number"
    num = square(num)
    return happy_num(num)

def square(num):
    if num == 0:
        return 0
    return (num % 10) ** 2 + square(num // 10)



num = 13
res = 0
print(happy_num(num))