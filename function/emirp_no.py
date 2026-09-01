def prime(val1):
    if val1 > 1:
        for num in range(2,int(val1 ** 0.5) + 1):
            if val1 % num == 0:
                return False
        return True
    return False

def Revers(val2):
    res = 0
    while val2 > 0:
        dig = val2 % 10
        res = res * 10 + dig
        val2 = val2 // 10
    return res

def emirpno(val3):
    rev = Revers(val3)
    if prime(val3) and rev != val3 and prime(rev):
        return "emirpno"
    return "Not a emirpno"

num = 17
print(emirpno(num))

