#         5 
#       5 4 
#     5 4 3 
#   5 4 3 2 
# 5 4 3 2 1

# num = 5
# space = num - 1
# for ev in range(num,0,-1):
#     for col1 in range(1,space + 1):
#         print(" ",end = " ")
#     for col2 in range(num,ev - 1,-1):
#         print(col2,end=" ")
#     print()
#     space = space - 1


#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7

# num = 4
# space = num - 1
# for row in range(2,num * 2 + 1, 2):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,row):
#         print(col2,end=" ")
#     print()
#     space = space - 1


#-----------------or -------------
# num = 4
# star = 1
# space = num - 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")

#     for col2 in range(1,star + 1):
#         print(col2,end=" ")
#     print()
#     space = space - 1
#     star = star + 2

#-----------------or -----------------------

# num = 4
# star = 1
# space = num - 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     data = 1
#     for col2 in range(1,star + 1):
#         print(data,end=" ")
#         data = data + 1
#     print()
#     space = space - 1
#     star = star + 2



# 1 2 3 4 5 6 7 
#   1 2 3 4 5 
#     1 2 3 
#       1 

# num = 4
# space = 0
# for ev in range(num * 2 , 1 , -2):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,ev):
#         print(col2,end=" ")
#     print()
#     space = space + 1

#-----------------------------or-------------------

# num = 4
# space = 0
# star = num * 2 - 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         print(col2,end=" ")
#     print()
#     space = space +1 
#     star = star - 2
#-----------------------------or-------------------

# num = 4
# space = 0
# star = num * 2 - 1
# for row in range(1,num + 1):
#     data = 1
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         print(data,end=" ")
#         data = data + 1
#     print()
#     space = space + 1 
#     star = star - 2


#     1 
#   1 2 3 
# 1 2 3 4 5 
#   1 2 3 
#     1 

# num = 5
# space = num // 2
# star = 1
# for ev in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         print(col2,end= " ")
#     print()
#     if ev <  num // 2 + 1:
#         space = space - 1
#         star = star + 2
#     else:
#         space = space  + 1
#         star = star - 2



num = 5
space = num // 2
star = 1
for ev in range(1,num + 1):
    for col1 in range(1,space + 1):
        print(" ",end=" ")
    data = 1
    for col2 in range(1,star + 1):
        print(data,end= " ")
        if col2 < star // 2 + 1:
            data = data + 1
        else :
            data = data - 1
    print()
    if ev <  num // 2 + 1:
        space = space - 1
        star = star + 2
    else:
        space = space  + 1
        star = star - 2