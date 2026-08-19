def reverse(num):
    res = 0
    while num > 0:
        dig = num % 10
        res = res * 10 + dig
        num = num // 10
    return res


num = int(input("Enter a number : "))
reverse(num)