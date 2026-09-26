# val = "Harsh"
# pwd = 123456
# if val == "Harsh":
#     if pwd == 123456:
#         print("login success")
#     else : print ("incorrect password ")
# else : print("not a valid user name !!!")  


# l = [10, 20,"hello",25,26]

# # if len(l) // 2 == 0:
# #     print(l[len(l) // 2])

# # else : print("error")

# # length = len(l)//2

# # if length%2 == 0:
# #     print(l[length])
# # else:
# #     print("error")

# # length = len(l)//2

# # if length%2==0:
# #     print(l[length])
# # else:
# #     print("error")


# # if len(l) % 2 != 0:
# #     print(l[len(l) // 2])


# s = "hello world happy"

# val = s.split()
# res = ""

# for word in val:
#     rev = ""

#     for ch in word:
#         rev = ch + rev

#     res = res + rev + " "

# print(res)


class sample:
    def __init__(self):
        self.__a = 30
    def gettar(self):
        return self.__a 
    def settar(self):
        self.__a = 40

obj = sample()
print(obj.gettar())
obj.settar()
print(obj.gettar())

    # staring, function ,  method