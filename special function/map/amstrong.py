def amstrong(num):
    if num >= 0:
        res = 0
        dup = num
        l = len(str(num))
        while num > 0:
            dig = num % 10
            res = res + dig ** l
            num = num // 10
        if dup == res:
            return f"{dup} -> amstrong number"
        return f"{dup} -> not a amstrong number"
    return f"{dup} -> not a amstrong number"


print(list(map(amstrong,range(1,1001))))