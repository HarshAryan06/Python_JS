def sum_digit(num):
    if num == 0:
        return 0
    return (num % 10) + sum_digit(num // 10)


def product_digit(num):
    if num == 0:
        return 1
    return (num % 10) * product_digit(num // 10)


num = 1124

if sum_digit(num) == product_digit(num):
    print("Spy Number")
else:
    print("Not a Spy Number")