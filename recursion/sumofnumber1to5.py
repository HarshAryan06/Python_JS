def add_num(val):
    if val == 6:
        return 0
    return val + add_num(val + 1)
    

num = 1
print(add_num(num))
