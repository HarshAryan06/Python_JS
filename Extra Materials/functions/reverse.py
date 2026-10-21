#waf to reverse a string
'''
def reverse():
    val = (input("Enter a string"))
    res = ""
    for i in val:
        res = i + res
    print(res)

reverse()
'''

#wap to reverse a number 
#waf to check if the number is plaindrome or not
# waf to check if the list contains integer or not 7


# waf ti checj if a number is odd or not 

'''
def isodd():
    n = int(input("Enter a number : "))
    if n % 2 != 0:
        return True
    else :
        return False

print(isodd())
'''

# waf to generate the number from 1 to 10

'''
def sequence():
    for i in range(1,11):
        return i

print(sequence())

'''

# waf to print the strong number between the given range

'''
def strong(n):
    dup = n
    strong = 0
    while dup != 0:
        rem = dup % 10
        fact = 1
        for i in range(1, rem + 1):
            fact = fact * i
        strong = strong + fact
        dup = dup // 10

    if n == strong:
        return True
    else :
        return False

l = []
st = int(input("Enter a  start number : "))
en = int(input("Enter a end number : "))

for i in range(st,en + 1):
    if strong(i):
        l.append(i)
print(l)

'''





