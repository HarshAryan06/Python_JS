def Add_nums():
    res = 0
    for val in range(1,num + 1):
        res = res + val
    return res

num = int(input("Enter a number of n natural : "))
print(Add_nums())