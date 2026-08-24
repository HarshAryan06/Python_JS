def fact(val1):                                        
        fact = 1
        for num in range(1,val1 + 1):
            fact = fact * num
        return fact

def sum_fact(val2):
    res = 0
    while val2 > 0:
        dig = val2 % 10
        res = res + fact(dig)
        val2 = val2 // 10
    return res

def strong(val3):
    if sum_fact(val3) == num:
        return "strong number"
    return "not a strong number"
    

    
num = 40585
print(strong(num))





