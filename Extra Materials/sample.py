# s = "abcdabcdabcd"
# print(s.find(""))

# m = "+91-785 456 756"
# o/p = 785456756


# print(m.replace("+91-","").replace(" ",""))
# print(m)
# m = 20000
# if (m % 100 == 0):
#     print(m)


# s = "abCdAb"
# if len(s) % 2 == 0:
#     if "A" <= s[len(s) // 2 - 1] <= "Z":
#         print(s[len(s) // 2 - 1])
#     else : print("noa a valid")
# else : print("not possible")


# s = "abs"
# print(s[::-1])

# l = [1,2,1,3,1]

# dup = {}
# for num in l:
#     if num not in dup:
#         dup[num]=1
#     else:
#         dup[num]+=1
# print(dup.keys())



class Demo:
    a = 10
    _b = 20
    __c = 30

    def get_value(self):
        return self.__c
# print(dir(Demo))
ob = Demo()
# print(ob._Demo__c)
print(ob.get_value())

