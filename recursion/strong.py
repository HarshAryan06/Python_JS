def fact(num):                                        
        if num == 0:
             return 1
        return num * fact(num - 1)
        

def strong(num):
    if num == 0:
         return 0
    return fact(num % 10) + strong(num // 10)


num = 145
if strong(num) == num:
      print("strong no")
else : print("not a strong number")
    

    