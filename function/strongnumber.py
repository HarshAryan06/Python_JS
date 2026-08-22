def strong_no(val):
    dup = val
    res = 0
    while val > 0:
        dig = val % 10
        fact = 1
        for num in range(1,dig + 1):
            fact = fact * num
        res = res + fact
        val = val // 10
    if dup == res:
        return "strong number"
    return " not a strong number "

num = 145
print(strong_no(num))


#-------------with two functions --------------------------

# def fact(val1):                                        
#         fact = 1
#         for num in range(1,val1 + 1):
#             fact = fact * num
#         return fact

# def strong(val2):
#     dup = val2
#     res = 0
#     while val2 > 0:
#         dig = val2 % 10
#         res = res + fact(dig)
#         val2 = val2 // 10

#     if dup == res:
#         return "strong number"
#     return "not a strong number"
    

    
# num = 145
# print(strong(num))