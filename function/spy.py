def spy(val):
    res = 0
    mul = 1
    while val > 0:
        dig = val % 10
        res = res + dig
        mul = mul * dig
        val = val // 10

    if mul == res:
        return "spy no"
    return "not a spy no"

num = 123
print(spy(num))