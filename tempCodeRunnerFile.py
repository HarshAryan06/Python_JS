
for num1 in range(100,1000):
    ans = str(num1 * 1) + str(num1 * 2) + str(num1 * 3)
    for num in range(1,10):
        if str(num) not in ans:
            # print(f"{num1} -> not a facinating number")
            break
    else: print(f"{num1} -> facinating number")
