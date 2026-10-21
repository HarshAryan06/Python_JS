# while is a loop statement which is use to execute some set of instruction repeatedly or again and again untill the given conditions

# in while loop intiazilaztion of looping variable and updations of looping variable is mandatory 
# if we dont initialize the looping variable then controller will throw an error(name error)
# if we dont update the looping variable then it will act as infinite loop.

# syntax 
            # initialization
             #  while <condition>:
                      #  statement


'''
#factorial of a number 
num = 5
fact = 1
res = 1

while res <= num:
    fact = fact * res
    res = res + 1
print(fact)
'''

'''
s = "hello"
res = 0
while res<len(s):
    print(s[res])
    res = res + 1
print(res)
'''

# wap to print python 5 times 
'''
num = 1
while num <= 5:
    print("python")
    num = num + 1
'''

# wap to print n natural number 

'''
num = 1
while num <= 5:
    print(num)
    num = num + 1
'''

# wap to print all the char in string 

'''
st = "hello"
res = 0

while res <len(st):
    print(st[res])
    res = res + 1
'''

# wap to print the table
'''
num = 5
res = 1

while res<=10:
    print(res*num)
    res = res + 1
'''    

# wap to to print the all the vivels present in a string 

'''
st = "heklloworld"
v = ""
i = 0

while i < len(st):
    if st[i] in "AEIOUaeiou":
        v = v + st[i]
    i = i + 1

print(v)
'''
# wap to 

'''
num = 123
res = 0
dup = num

while num > 0:
    dig = num % 10
    res = res * 10  + dig
    num = num // 10
if dup == res:
    print("palindrome")
else :
    print("not a palindrome ")
'''

# wap to find the sum of individual digits of a number 

'''
num = 123
res = 0
dup = num

while num > 0:
    dig = num % 10
    res = res + dig
    num = num // 10
print(res)
'''

# wap to check a number is perfect no or not 
'''
num = 28
i = 1
dup = num
fact = 0
while i<=num:
    if dup % i == 0:
        fact = fact + i
    i = i + 1
print(fact)

'''
# wap to login to phonepay by entinering correct otp
'''
import random
otp = random.randint(0000,9999)
user_otp = int(input("enter a otp"))
chances = 3
i = 1

while i <= chances:
    if otp == user_otp:
        print("login success")
        break
    else :
        print()

'''
# amstrong number 
'''
num = 153
res = 0
dup = num
power = len(str(num))

while num > 0:
    dig = num % 10
    res = res + dig ** power
    num = num // 10
if dup == res:
    print("amstrong number")
else :
    print("not a amstrong number")

'''

'''
val1 = "1001110"
val2 = "0011010"

count = 0
i = 0

while i < len(val1):
    if val1[i] == val2[i]:
        count = count + 1
    i = i + 1
print(count)
'''


# amstrong range
'''
num = int(input("enter a number : "))
i = 2
while i<num:
    if num % i == 0:
        print("not a prime number")
        break
    i = i + 1
    else:
        print("prime no")
'''

# hcf of a number 
'''
a = 16
b = 28

if a < b:
    i = a
else : 
    i = b

while i != 0:
    if a % i == 0 and b % i == 0:
        print(i)
        break
    i = i - 1

'''

num = 10010
res = 0
power = 0
while num > 0:
    dig = num % 10
    res = res + dig * (2 ** power)
    power = power + 1
    num = num // 10
print(res)

# decimal to bin 
#------------Approach 1 --------------
num = 12
res = 0
power = 1

while num > 0:
    dig = num % 2
    res = res + dig * power 
    power = power * 10
    num = num // 2
print(res)

#------------Approach 2 --------------
num = 13
bin = ""
while num > 0:
    res = num % 2
    bin = str(res) + bin
    num = num // 2
print(bin)


# guess the number

import random
guess_num = random.randint(0,20)

while num 