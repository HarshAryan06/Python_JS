# inp =
# count = 0

# for num in range(2,inp//2 +1):           #  best approach
#     if inp % num == 0:
#         print("not a prime no")
#         break
# else : print("prime no")

# inp = int(input("enter a number : "))
# if inp > 1:
#     for num in range(2,inp//2 +1):                          # better approach
#         if inp % num == 0:
#             print(f"{inp} not a prime no ")
#             break
#     else : print(f"{inp} prime no")


# else: print(f"{inp} not a prime no ")



# inp = int(input("enter a number : "))
# if inp > 1:
#     for num in range(2,int(inp ** 0.5) + 1):                          # optimal approach
#         if inp % num == 0:
#             print(f"{inp} not a prime no ")
#             break
#     else : print(f"{inp} prime no")


# else: print(f"{inp} not a prime no ")

#------------------------ palyprime ------------------------------------
# inp = int(input("enter a number : "))
# rev = 0
# dup = inp
# if inp > 1:
#     for num in range(2,int(inp ** 0.5) + 1):
#         if inp % num == 0:
#             print(f"{inp} not a palyprime")
#             break
#     else :
#         while inp > 0:
#             dig = inp % 10
#             rev = rev * 10 + dig
#             inp = inp // 10
#         if dup == rev:
#             print("no is palyprime")

#         else: print(f"{inp} not a palyprime ")
# else : print("not a palyprime ")





inp = int(input("enter a number : "))
rev = 0
dup = inp
if inp > 1:
    for num in range(2,int(inp ** 0.5) + 1):
        if inp % num == 0:
            print(f"{inp} not a EMIRP no")
            break
    else :
        while inp > 0:
            dig = inp % 10
            rev = rev * 10 + dig
            inp = inp // 10
        if dup != rev:
            for num in range(2,int(rev ** 0.5) + 1):
                if rev % num == 0:
                    print(f"{inp} not a EMIRP no")
                    break
            else : print("is a palyprime")

        else : print("not palindrome no  ")
else : print("not a prime no ")

       


