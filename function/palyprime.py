def prime(val1):
    if val1 > 1:
        for num in range(2,int(val1 ** 0.5) + 1):
            if val1 % num == 0:
                return False
        return  True
    return  False

def rever(val2):
    res = 0
    while val2 > 0:
        dig = val2 % 10
        res = res * 10 + dig
        val2 = val2 // 10
    return res

def palyprime(val3):
    if prime(val3) and rever(val3) == val3:
        return "palyprime"
    return "Not a palyprime"

num = 101
print(palyprime(num))

