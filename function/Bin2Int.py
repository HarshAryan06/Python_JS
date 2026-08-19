
def Bin2Int(num):
    res = 0
    power = 0
    while num > 0:
        dig = num % 10
        res = res + dig * (2 ** power)
        power = power + 1
        num = num // 10
    print(res)

num = int(input("Enter a number : "))
Bin2Int(num)