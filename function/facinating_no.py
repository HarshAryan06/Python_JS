def facinating(val):
    ans = str(val * 1) + str(val * 2) + str(val * 3)
    for num in range(1,10):
            if str(num) not in ans:
                return "not a facinating number"
    return "facinating number"


num = 192
print(facinating(num))