# def prime(num,val):
#     if val > num:
#         return 0
#     if num % val == 0:
#         return 1 + prime(num,val+1)
#     return prime(num , val + 1)

# def Reverse(num ,res = 0):
#     if num == 0:
#         return 0
#     res = 0
#     dig = num % 10
#     res = res * 10 + dig
#     return Reverse(res,num // 10)


# num = 101
# val = 1
# if prime(num,val) == 2 and Reverse(num,res=0) == num:
#     print("pLyprime")
# else : print("not a palyprime")


def prime(num,val):
    if val > num:
        return 0
    if num % val == 0:
        return 1 + prime(num,val+1)
    return prime(num,val + 1)
    
def Reverse(val,place):
    if val == 0:
        return 0
    return (val % 10) * place + Reverse(val // 10,place // 10)

num = 11
val = 1
place = 10 ** (len(str(num)) - 1)
if (Reverse(num,place)) == num and prime(num,val) == 2:
    print("palyprime")
else : print("not a palyprime")



