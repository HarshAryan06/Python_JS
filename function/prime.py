def prime():
    if num > 1:
        for val in range(2,int(num ** 0.5) + 1):  
                if num % val == 0:
                    return "not a prime"
        return "prime number"
    return "not a prime number"

num = int(input("enter a number : "))
print(prime())                                                          