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

num = 17
val = 1
place = 10 ** (len(str(num)) - 1)
res = Reverse(num ,place)
if res != num and prime(res,val) == 2 and prime(num,val) == 2:
    print("emirp no")
else : print("not a emirpno")