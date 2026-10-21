def Outer(arg):
    def inner(v1,v2):
        if v2 == 0:
            v1,v2 = v2,v1 
        if v1 == 0 and v2 == 0:
            return "not possible"
        return arg(v1,v2)
    return inner

@Outer
def Div(num1,num2):
    return num1 / num2

print(Div(5,10))
print(Div(0,2))
print(Div(0,0))
print(Div(3,0))


"""codition was if denomerator is zero swap the denomerator with numerator 
and if numerator and denomerator is 0  not possible"""