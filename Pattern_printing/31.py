# 1 1 1 1 
# 1 1 1 1 
# 1 1 1 1 
# 1 1 1 1 

# num = 4
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         print(1,end = " ")
#     print()

# 1 1 1 1 
# 2 2 2 2 
# 3 3 3 3 
# 4 4 4 4 

# num = 4
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         print(row,end = " ")
#     print()

# 4 4 4 4 
# 3 3 3 3 
# 2 2 2 2 
# 1 1 1 1

# num = 4
# for row in range(num,0,-1):
#     for col in range(1,num + 1):
#         print(row,end = " ")
#     print()

# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4

# num = 4
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         print(col, end = " ")
#     print()

# 4 4 4 4 
# 3 3 3 3 
# 2 2 2 2 
# 1 1 1 1 

# num = 4
# for row in range(1,num + 1):
#     for col in range(num,0,-1):
#         print(col, end = " ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

# num = 5
# for row in range(1,num + 1):
#     for col in range(1, row + 1):
#         print(col,end = " ")
#     print()

            #------ or --------
# num = 5
# for ev in range(2,7):
#     for col in range(1,ev):
#         print(col,end=" ")
#     print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1 

# num = 5
# for ev in range(num + 1,1,-1):
#     for col in range(1,ev):
#         print(col,end=" ")
#     print()

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1 

# num = 5
# for st in range(1,num + 1):
#     for col in range(st,0,-1):
#         print(col,end=" ")
#     print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 

# num = 5
# for ev in range(num,0,-1):
#     for col in range(ev,0,-1):
#         print(col,end=" ")
#     print()

# 5 
# 4 5 
# 3 4 5 
# 2 3 4 5 
# 1 2 3 4 5 

# num = 5
# for st in range(num,0,-1):
#     for col in range(st,num + 1):
#         print(col,end=" ")
#     print()

#         5 
#       4 5 
#     3 4 5 
#   2 3 4 5 
# 1 2 3 4 5 

# num = 5
# space = num - 1
# for st in range(num,0,-1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col in range(st,num + 1):
#         print(col,end=" ")
#     print()
#     space = space - 1


#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1 

# num = 5
# space = num - 1
# for st in range(1,num + 1):
#     for col1 in range(1,space + 1):
#                 print(" ",end=" ")
#     for col in range(st,0,-1):
#         print(col,end=" ")
#     print()
#     space = space - 1

# 5 4 3 2 1 
#   5 4 3 2 
#     5 4 3 
#       5 4 
#         5 

# num = 5
# space = 0
# for ev in range(0,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col in range(num ,ev,-1):
#         print(col,end=" ")
#     print()
#     space = space + 1


# arr = [3,6,8,14,23,45,78]

# target = 78

# start = 0
# last = len(arr) - 1

# while start <= last:
#     mid = (start + last) // 2

#     if arr[mid] == target:
#         print("elemet found",mid)
#         break

#     elif arr[mid] > target:
#         last = mid - 1
#     else:
#         start = mid + 1
        

# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]

# target = 60

# m = len(matrix)
# n = len(matrix[0])

# start = 0
# last = m * n - 1



# while start <= last:
#     mid = (start + last) // 2
#     row = mid // n
#     col = mid % n
#     matrix_element = matrix[row][col]
#     if matrix_element == target:
#         print("element found at ", mid)
#         break

#     elif matrix_element > target:
#         last = mid - 1
#     else:
#         start = mid  + 1
        


# num = 5
# for row in range(1,num + 1):
#     for col in range(0,num + 1):
#         print(col,end=" ")
#     print()

# num = 5
# for row in range(1,num + 1):
#     for col in range(num,row - 1,-1):
#         print(col,end=" ")
#     print()

# num = 5 
# for sv in range(1,num + 1):
#     for col in range()



num = 5
space  = num - 1
for st in range(2,(num + 1) + 1):

    for col2 in range(1,space + 1):
        print(" ",end= " ")
    for col3 in range(1,st):
        print(col3,end = " ")
    print()
    space = space - 1
  






