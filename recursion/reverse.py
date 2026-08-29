def Reverse(val,place):
    if val == 0:
        return 0
    return (val % 10) * place + Reverse(val // 10,place // 10)

num = 345
place = 10 ** (len(str(num)) - 1)
print(Reverse(num,place))



