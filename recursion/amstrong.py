def Armstrong(val, power):
    if val == 0:
        return 0
    return (val % 10) ** power + Armstrong(val // 10, power)


num = 153
power = len(str(num))

if Armstrong(num, power) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")