

# num = 4
# for row in range(1, num + 1):
#     for col in range(1,row + 1):
#         print("*",end =" ")
#     print()

# * 
# * * 
# * * * 
# * * * * 

# num = 4
# star = 1
# for row in range(1, num + 1):
#     for col in range(1,star + 1):
#         print("*",end =" ")
#     print()
#     star = star + 1

# * 
# * * 
# *   * 
# * * * * 
# num = 4
# for row in range(1,num + 1):
#     for col in range(1,row + 1):
#         if col == 1 or row == num or col == row:
#             print("*",end=" ")
#         else: print(" ",end= " ")
#     print()

# * * * * 
# * * * 
# * * 
# * 
# num = 4
# star = num
# for row in range(1,num + 1):
#     for col in range(1,star + 1):
#         print("*",end= " ")
#     print()
#     star = star - 1


# * * * * 
# *   * 
# * * 
# * 
# num = 4
# star = num
# for row in range(1,num + 1):
#     for col in range(1,star + 1):
#         if row == 1 or col == 1 or col == star:
#             print("*",end= " ")
#         else : print(" ",end=" ")
#     print()
#     star = star - 1


#       * 
#     * * 
#   * * * 
# * * * * 
# num = 4
# space = num - 1
# star = 1
# for row in range(1,num + 1):
#     for col in range(1,space + 1):
#         print(" ", end=" ")
#     for col2 in range(1,star + 1):
#         print("*",end = " ")
#     print()
#     space -= 1
#     star += 1

#       * 
#     * * 
#   *   * 
# * * * * 

# num = 4
# space = num - 1
# star = 1
# for row in range(1,num + 1):
#     for col in range(1,space + 1):
#         print(" ", end=" ")
#     for col2 in range(1,star + 1):
#         if col2 == 1 or row == num or col2 == star:
#             print("*",end = " ")
#         else: print(" ", end=" ")
#     print()
#     space -= 1
#     star += 1


# * * * *
#   * * *
#     * *
#       *


# num = 5
# space = 0
# star = num - 1
# for row in range(1,num + 1):
#     for col in range(1,space + 1):
#         print(" ", end=" ")
#     for col2 in range(1,star + 1):
#                 print("*",end = " ")
#     print()
#     space += 1
#     star -= 1

# * * * *
#   *   *
#     * *
#       * 

# num = 5
# space = 0
# star = num - 1
# for row in range(1,num + 1):
#     for col in range(1,space + 1):
#         print(" ", end=" ")

#     for col2 in range(1,star + 1):
#         if row == 1 or col2 == star or col2 == 1:
#             print("*",end = " ")
#         else: print(" ",end=" ")
#     print()
#     space += 1
#     star -= 1

#       * 
#     * * * 
#   * * * * * 
# * * * * * * *  

# num = 4
# space = num - 1
# star = 1

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         print("*",end=" ")
#     print()
#     space = space - 1
#     star = star + 2

#       * 
#     *   * 
#   *       * 
# * * * * * * * 

num = 4
space = num - 1
star = 1

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         if row == num or col2 == 1 or col2 == star:

#             print("*",end=" ")
#         else : print(" ",end=" ")
#     print()
#     space = space - 1
#     star = star + 2

# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

# num = 4
# space = 0
# star = num * 2 - 1

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             print("*",end=" ")
#     print()
#     space = space + 1
#     star = star - 2



# * * * * * * * 
#   *       * 
#     *   * 
#       * 

# num = 4
# space = 0
# star = num * 2 - 1

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             if row == 1 or col2 == 1 or col2 == star:
#                 print("*",end=" ")
#             else: print(" ", end=" ")
#     print()
#     space = space + 1
#     star = star - 2



# * * * * * * * * * 
# *       *       * 
# *       *       * 
# *       *       * 
# * * * * * * * * * 
# *       *       * 
# *       *       * 
# *       *       * 
# * * * * * * * * * 
# num = 9
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         if row == 1 or col == 1 or row == num or col == num or row == num // 2 + 1 or col == num // 2 + 1:
#          print("*",end=" ")
#         else : print(" ",end=" ")
#     print()

# * * * * * * * * * * 
# * *       *     * * 
# *   *     *   *   * 
# *     *   * *     * 
# *       * *       * 
# * * * * * * * * * * 
# *     *   * *     * 
# *   *     *   *   * 
# * *       *     * * 
# * * * * * * * * * *

# num = 10
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         if row == 1 or col == 1 or row == num or col == num or row == num // 2 + 1 or col == num // 2 + 1 or row == col or row + col == num + 1:
#          print("*",end=" ")
#         else : print(" ",end=" ")
#     print()

# * * * * * 
# *       * 
# *   *   * 
# *       * 
# * * * * * 

# num = 5
# for row in range(1,num + 1):
#     for col in range(1,num + 1):
#         if row == 1 or col == 1 or row == num or col == num or (row == num //2 +1 and col == num // 2 + 1):
#          print("*",end=" ")
#         else : print(" ",end=" ")
#     print()

#         * 
#       * * * 
#     * * * * *  
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# num = 7
# space = num // 2 
# star = 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             print("*",end=" ")
#     print()
#     if row < num // 2 + 1: 
#         space = space - 1
#         star = star + 2
#     else: 
#          space = space  + 1
#          star = star - 2


#       * 
#     *   * 
#   *       * 
# *           * 
#   *       * 
#     *   * 
#       * 

# num = 7
# space = num // 2 
# star = 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         if col2 == 1 or col2 == star:
#             print("*",end=" ")
#         else: print(" ",end=" ")
#     print()
#     if row < num // 2 + 1: 
#         space = space - 1
#         star = star + 2
#     else: 
#          space = space  + 1
#          star = star - 2


#       * 
#     *   * 
#   *       * 
# * * * * * * * 
#   *       * 
#     *   * 
#       * 

# num = 7
# space = num // 2 
# star = 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         if col2 == 1 or col2 == star or row == num // 2 + 1:
#             print("*",end=" ")
#         else: print(" ",end=" ")
#     print()
#     if row < num // 2 + 1: 
#         space = space - 1
#         star = star + 2
#     else: 
#          space = space  + 1
#          star = star - 2


#         * 
#       * * * 
#     *   *   * 
#   *     *     * 
# * * * * * * * * * 
#   *     *     * 
#     *   *   * 
#       * * * 
#         * 

# num = 9
# space = num // 2 
# star = 1
# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#         if col2 == 1 or col2 == star or row == num // 2 + 1  or col2 == star // 2 + 1:          # space + col2 == num // 2 + 1
#             print("*",end=" ")
#         else: print(" ",end=" ")
#     print()
#     if row < num // 2 + 1: 
#         space = space - 1
#         star = star + 2
#     else: 
#          space = space  + 1
#          star = star - 2


# * * * * * 
#   * * * 
#     * 
#   * * * 
# * * * * * 

# num = 5 
# space = 0
# star = num

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             print("*",end=" ")
#     print()
#     if row < num // 2 + 1: 
#         space = space + 1
#         star = star - 2
#     else: 
#          space = space  - 1
#          star = star + 2


# * * * * * * * 
#   *       * 
#     *   * 
#       * 
#     *   * 
#   *       * 
# * * * * * * *

# num = 7
# space = 0
# star = num

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             if row == 1 or row == num or col2 == star or col2 == 1:
#                 print("*",end=" ")
#             else : print(" ",end=" ")
#     print()

#     if row < num // 2 + 1: 
#         space = space + 1
#         star = star - 2
#     else: 
#          space = space  - 1
#          star = star + 2


# *           * 
#   *       * 
#     *   * 
#       * 
#     *   * 
#   *       * 
# *           * 

# num = 7
# space = 0
# star = num

# for row in range(1,num + 1):
#     for col1 in range(1,space + 1):
#         print(" ",end=" ")
#     for col2 in range(1,star + 1):
#             if col2 == star or col2 == 1:
#                 print("*",end=" ")
#             else : print(" ",end=" ")
#     print()

#     if row < num // 2 + 1: 
#         space = space + 1
#         star = star - 2
#     else: 
#          space = space  - 1
#          star = star + 2


