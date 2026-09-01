def facinating(num,res,val):
    if val > 9:
        return "facinating no"
    if str(val) not in res:
        return "not a facinating no"
    return facinating(num,res,val+1)
    

num = 192
res = str(num * 1) + str(num * 2) + str(num * 3)
# 192384576
val = 1
print(facinating(num,res,val))