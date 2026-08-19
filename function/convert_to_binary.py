# def int2Bin(num):
#     res = 0
#     pos = 1
#     while num > 0:
#         dig = num % 2
#         res = res + dig * pos
#         num = num // 2
#         pos = pos * 10
#     return "Ob" + str(res)
    

# num = int(input("Enter a number : "))
# int2Bin(num)



def int2Bin(num):
    res = ""
    pos = 1
    while num > 0:
        dig = num % 2
        res = str(dig) + res
        num = num // 2
        pos = pos * 10
    return "Ob" + res    

num = int(input("Enter a number : "))
int2Bin(num)


# wap to reverse a number using functional programming 
# wap convert binary to integer using functional programming 