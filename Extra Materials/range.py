# it is consider as a collection datatypes but is doesnt have any data structure to display  the output to overcome this problem 

# we have to use typecasting or for loop (it is used to generate sequence of number based on the argumnets)

# syntax : range(start, end , step)

'''
print(range(1,6))

print(tuple(range(1,6)))

print(set(range(1,6)))

# print(dict(range(1,6)))

print(list(range(1,6)))

print(list(range(-1,-6,-1)))
'''

# wap to generate a 5 natural number 
'''
for i in range(1,6):
    print(i)
'''

# wap to gnerate 5 whole number
'''
for i in range(5):
    print(i)
'''
# wap to genrate  5 natural number in reverse 

'''
for i in range(5,0,-1):
    print(i)
'''
# wap to generate only odd number from 1 to 50

'''
for i in range(1,51,2):
    print(i)
'''
# wap to gnerate to get sum of all the odd number from 1 to 50

'''
odd = 0
for i in range(1,51,2):
    if i % 2 != 0:
        odd = odd + i
print(odd)
'''

# wap to find the factorial of anumber 

'''
fact = 1
for i in range(1,6):
    fact = fact * i
print(fact)

'''

# wap to find the the sum og n natural number 
'''

val = int(input("enter number "))
sum = 0
for i in range(1,val):
    sum = sum + i
print(sum)

'''

# wap to generate the lowercase alphabedts from a to z

'''
for i in range(ord("a"),ord("z") + 1):
    print(chr(i),end=" ")

'''

# wap to extract index numner along with its character 

'''
s = "python"

for i in range(len(s)):
    print(f"{i} --> {s[i]}")

'''

# wap to reverse a string without using 3rd variable

'''
s = "python"
for i in range(len(s) - 1,-1,-1):
    print(s[i],end=" ")
'''




# o/p = {"a" : 97, "b" : 98, "c" : 99 , "d" : 100}

'''
st = 'abcd'
l = [97,98,99,100]
out = {}
for i in range(len(st)):
    out[st[i]] = l[i]
print(out)
'''

'''
 * * * * *
 * * * *
 * * *
 * *
 *
for i in range(5,0,-1):
    print(" *" * i)
'''

'''
for i in range(1,6):
    print(" *" * i)
for i in range(5,-1,-1):
        print(" *" * i)

'''

# wap to print the position of  vovels present in a given string 

''''
s = "abcde"
for i in range(len(s)):
    if s[i]  in "AEIOUaeiou":
        print(i)
'''

# wap to find the divisor of a particular number and add it in to a list

# i/p = 10
# o/p = [1,2,,5,10]

'''
num = 10
out = []

for i in range(1,num + 1):
    if num %  i == 0:
        out = out + [i]
print(out)
'''

# wap to find the perfect number 
'''
num = 28
out = 0

for i in range(1,num//2 +1):
    if num % i == 0:
        out = out + i
if num == out:
    print("perfect number")
else : print("not a perfect number")

'''


num = 10
place = 1
res = 0
while num > 0:
    dig = num % 2
    res = res + dig * place
    num = num // 2
    place = place * 10
print(res)

num 
