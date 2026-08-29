def bin2int(val,place):
    if val == 0:
        return 0
    return (val % 10) * (2 ** place) + bin2int(val // 10 ,place + 1) 

num = 111
place = 0
print(bin2int(num,place))


