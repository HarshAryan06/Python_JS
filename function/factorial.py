def factorial():
    if num > 0:
        fact = 1
        for val in range(1,num+1):
                fact = val * fact
        return fact
    return "not possible"


num = int(input("enter a number of factorial : "))
print(factorial())