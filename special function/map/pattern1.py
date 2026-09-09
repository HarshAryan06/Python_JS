# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# num = 5

# l = list(map(lambda a : "* " * a ,range(1,num + 1)))
# print("\n".join(l))


num = 5

l = list(map(lambda a : "* " * a ,range(num,0,-1)))
print("\n".join(l))