# def tento1(val):
#     if val == 0:
#         return 
#     print(val)
#     val1 = val - 1
#     tento1(val1)


# num = 10
# (tento1(num))


def tento1(val):
    if val == 0:
        return 
    print(val)
    tento1(val - 1)


num = 10
(tento1(num))