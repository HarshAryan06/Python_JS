# wap to print a sum of a digit from 50 to 150

# for num in range(50,151):
#     dup = num
#     rem = 0
#     while num > 0:
#         digit = num % 10
#         rem = rem + digit
#         num = num // 10
#     print(f"{dup} -> {rem}")


# wap to check a number is a strong number or not 

num = 145
rem = 0
dup = num
while num > 0:
    dig = num % 10
    fact = 1
    for num1 in range(1,dig+1):
        fact = fact * num1
    rem = rem + fact
    num = num // 10
if dup == rem:
    print(f"{dup} is a strong number")
else : print(f"{dup} is not a strong number")