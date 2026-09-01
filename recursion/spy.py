# def sum_digit(num):
#     if num == 0:
#         return 0
#     return (num % 10) + sum_digit(num // 10)


# def product_digit(num):
#     if num == 0:
#         return 1
#     return (num % 10) * product_digit(num // 10)


# num = 1124

# if sum_digit(num) == product_digit(num):
#     print("Spy Number")
# else:
#     print("Not a Spy Number")



#------------------------using one function ---------------------------------------------------

def spy(num,add,prod):
    if num == 0:
        if add == prod:
            return "spy"
        return "not a spy"
    return spy(num // 10,add + (num % 10),prod * (num % 10))
num = 123
add= 0
prod = 1
print(spy(num,add,prod))
