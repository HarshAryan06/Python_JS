# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# num = 5

# l = list(map(lambda a : "* " * a ,range(1,num + 1)))
# print("\n".join(l))


# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# num = 5

# l = list(map(lambda a : "* " * a ,range(num,0,-1)))
# print("\n".join(l))


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# num = 5

# l = list(map(lambda  sp , st: "  " * sp + "* " * st  , range(num - 1 ,-1 ,-1), range(1,num + 1)))
# print("\n".join(l))

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# num = 5

# l = list(map(lambda  sp , st: "  " * sp + "* " * st  , range(0,num + 1), range(num , 0 ,-1)))
# print("\n".join(l))

#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 


# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

# num = 5

# l = list(map(lambda sp , st : "  " * sp + "* " * st , range(0,num + 1),range(num * 2 -1,0,-2)))
# print("\n".join(l))



# l = [(15,5),(14,6)]
# p = l.copy().sort()
# print(l)
# print(p)
l = [(15,5),(14,6),[10,200]]
# l.sort()
# print(l)
a = l.copy()
l[0] = 100
l[-1][0] = 1000
print(l) 
print(a)
# a = l.copy()
# a.sort()
# print(l)
# print(a)


