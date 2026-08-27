def add_dig(val):
    if val == 0:
        return 0
    return (val % 10) + add_dig(val // 10)

num = 345
print(add_dig(num))