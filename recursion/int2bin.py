def int2bin(val,place):
    if val == 0:
        return 0
    return (val % 2) * place + int2bin(val // 2,place * 10)

num = 7
place = 1
print(int2bin(num,place))


