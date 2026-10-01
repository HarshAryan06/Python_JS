'''
num = int(input("Enter a number : "))
flag = False

for i in range(2,num):
    if num % i == 0:
        flag = False
        break 
    else : 
        flag = True

if flag == True:
    print("Prime no")
else : 
    print("not a prime no")

'''

num = int(input("Enter a number : "))
flag = False

for i in range(2,num):
    if num % i == 0:
        print(" not a prime no")
        break 

else :
    print("prime no ")

