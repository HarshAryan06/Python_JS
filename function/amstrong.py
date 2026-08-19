def check_amstrong(val):
    res = 0
    dup = val
    power = (len(str(val)))
    while val > 0:
        dig = val % 10
        res = res + dig ** power
        val = val // 10
    if dup == res:
        return "amstrong number"
    return "not a amstrong number"

num = int(input("enter a number : "))
print(check_amstrong(num))
