# # # # # num = int(input("Enter a number : "))

# # # # # if num == 0:
# # # # #     print('No is positive')

# # # # # else: print("no is not positive")


# # # # num = int(input("Enter a number : "))

# # # # if num % 2 == 0:
# # # #     print('number is even')

# # # # else: print('no is not even')

# # # num = int(input("Enter a number : "))

# # # if num >= 18:
# # #     print('person can vote')
# # # else: print("person cant vote")

# # 
# # num2 = int(input("Enter a number : "))

# # if num1 > num2:
# #     print('num1 is highest')
# # else:
# #     print('num2 is highest')

# num = int(input("Enter a number : "))

# if num % 10 == 0:
#     print("no is divisible by 10")
# else:
#     print("no is not divisible by 10")



# a,b,c,d,e = 56,88,96,52,66
# if a > b:
#     if a > c:
#         if a > d:
#             if a > e:
#                 print("a is highest")

#             else: print("e is highest")
        
#         else:
#             if d > e:
#                 print("d is highest")
            
#             else: print("e is highest")

#     else :
#         if c > d:
#             if c > e:
#                 print("c is hihest")

#             else: print("e is highest")

#         else: 
#             if d > e:
#                 print("d is highest")
            
#             else: print("e is highest")

# else:
#     if b > c:
#         if b > d:
#             if b > e:
#                 print('b is highest')

#             else:
#                 print("e is highest")

#         else :
#             if d > e:
#                 print("d is highest")
#             else : print("e is highest")

#     else:
#         if c > d:
#             if c > e:
#                 print("c is highest")  

#             else: print("e is highest") 

#         else:
#             if d > e:
#                 print("d is highest") 
#             else: 
#                 print("e is highest")




# a,b,c,d,e = 56,88,96,52,66

# if a == b == c == d == e:
#     print("all are same")

# else :
#     if a > b and a > c and a > d and a > e:
#         print("a is highest") 
    
#     elif b > c and b > e and b > d:
#         print("b is highest")
    
#     elif c > d and c > e:
#         print("c is highest")
    
#     elif d > e: 
#         print("d is highest")

#     else : 
#         print("e is highest")




# for i in range(10,1,-1):
#     print(i)


# num = int(input("Enter a table no : "))

# for i in range(1,11):
#     print(f'{num} X {i} = {num * i}')


# num = int(input("Enter a table no : "))

# for i in range(num,0,-1):
#     print(i)

# num = int(input("Enter a number : "))
# sum = 0

# for i in range(1,11):
#     sum = sum + i

# print(sum)

# num = int(input("Enter a number : "))

# sum = 0
# for i in range(num,0,-1):
#     sum = sum + i
# print("Sum of a number : " , sum)

# num = int(input("Enter a number : "))

# sum = 0

# for i in range(1,num):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)

# num = int(input("Enter a number : "))

# sum = 0

# for ele in range(1, num + 1):
#     if ele % 2 != 0:
#         sum = sum + ele
    
# print(sum)

# num = input("Enter a string for reverse : ")

# ans = ''

# for ch in num:
#     ans = ans + ch
# print(ans)


# num = int(input("Enter a number : "))

# rev = 0

# while num > 0:
#     digt = num % 10
#     rev = rev * 10 + digt
#     num = num // 10
# print(rev)

arr = [10,2,3,45,6]

great = arr[0]

for ele in arr:
    if ele > great:
        great = ele
print(great)


