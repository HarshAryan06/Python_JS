def Outer(arg):
    def inner(v1,v2):
        if v1 < 0:
            v1 = v1 *(-1)
        if v2 < 0:
            v2 = v2 * (-1)
        return arg(v1,v2)


    return inner

@Outer
def funct1(num1,num2):
    return num1 + num2

print(funct1(5,6))
print(funct1(3,-6))
print(funct1(-4,5))
print(funct1(-3,-4))