num = int(input("Enter a number : "))
while num > 9:
    res = 0
    while num > 0:
        dig = num % 10
        res = res + dig ** 2
        num = num // 10
    num = res
if num == 1 or num == 7:
    print(f"is a happy number")
else : print(f"is not a happy number")
