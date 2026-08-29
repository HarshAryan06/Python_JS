# val = int(input("enter a number : "))
# rev = 0
# dup = val
# while val > 0:                            # check reverse , palindrome no 
#     dig = val % 10
#     rev = rev * 10 + dig
#     val = val // 10
# if dup == val:
#     print("Palindrome no")
# else : print("not a palindrome")

# num = -456
# dub = num
# num = abs(num)
# rev = 0
# place = 10 ** (len(str(num)) - 1)
# while num > 0:
#     dig = num % 10
#     rev = rev + dig * place
#     place = place // 10
#     num = num // 10
# if dub < 0:
#     print(rev * -1)
# else: print(rev)



# val = int(input("Enter a number : "))
# place = 1
# rev = 0
# while val > 0:
#     dig = val % 2                   # place = place  - 1 
#     rev = rev + dig * place 
#     val = val // 2
#     place = place * 10
# print(rev)

# val = int(input("Entera number : "))
# power = 0
# rev = 0
# while val > 0:
#     dig = val % 10
#     rev = rev + dig * (2 ** power)
#     power = power + 1
#     val = val // 10
# print(rev)


# val = int(input("Enter a number : "))
# power = 0
# rev = 0
# while val > 0:
#     dig = val % 10
#     rev = rev + dig * (2 ** power)
#     power = power + 1
#     val = val // 10
# print(rev)


# num = 1
# while num < 5:
#     print(num)
#     num = num + 1
# else : print("else block")

# val = 192
# ans = str(val * 1) + str(val * 2) + str(val * 3)
# print(ans)

# for num in range(1,10):
#     if str(num) not in ans:
#         print("not a facinating number")
#         break
# else: print("facinating number")


# num = input("Enter anumber : ")
# res = ''

# for val in num:
#     if val != '0':
#         res = res + val
# print(res)

val = int(input("Enter a number : "))

res = 0
place = 1

while val > 0:
    dig = val % 10

    if dig != 0:
        res = res + dig * place
        place = place * 10
    val = val // 10
print(res)
