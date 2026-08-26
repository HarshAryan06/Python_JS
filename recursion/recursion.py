def factorial(val): 
    if val < 0:
        return "not possible"
    elif val == 0:
        return 1
    return val * factorial(val - 1)


num = -1
print(factorial(num))