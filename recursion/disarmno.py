def Disarm(val, place):
    if val == 0:
        return 0
    return (val % 10) ** place + Disarm(val // 10, place - 1)


num = 135
place = len(str(num))

print(Disarm(num, place))