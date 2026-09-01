def prime(num,val):
    if val > num:
        return 0
    if num % val == 0:
        return 1 + prime(num,val+1)
    return prime(num,val + 1)
    

num = 7
val = 1
if (prime(num,val)) == 2:
    print("prime no")
else : print("not a prime no")