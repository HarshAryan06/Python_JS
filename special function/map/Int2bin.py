def int2Bin(num):
    res = 0
    pos = 1
    while num > 0:
        dig = num % 2
        res = res + dig * pos
        num = num // 2
        pos = pos * 10
    return res    

print(list(map(int2Bin,range(1,10))))
