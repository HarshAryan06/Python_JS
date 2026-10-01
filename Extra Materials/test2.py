# val = (10,20,30,40,50,60)
# ans = ()

# for tuple in val:
#     ans = (tuple,) + ans
# print(ans)

#-------------------------------------------

# plaindrome 

# ch = "racecars"
# ans = ""

# for val in ch:
#     ans = val + ans

# if ch == ans:
#     print("palindrome")
# else : print("not a plaindrome ")

#------------------------------------------------

# ch = {"a" : 1, "b" : "hello" , "c": 33}
# ans = {}
# for val in ch:
#     ans = {val : ch[val]} | ans
# print(ans)

#-------------------------------------------
 # reversing the set :

# ch = {10,20,30,40,50}
# ans = set()
# for val in ch:
#     ans = {val} | ans
# print(ans)

#---------------------------------------------

# wap to count the word and its length pair

'''st =  " python is very tough"

# o/p = {'python' : 6 , 'is' : 2 , 'very' : 4, 'easy' : 4}

out = {}
for i in st.split():
    # var[key] = new_value

    out[i] = len(i)
print(out)
'''


st =  "python is very tough"

# o/p = {'p' : 1, 'y' : 1 ............}

# out = {}
# for i in st:

#     if i not in out:
#         out[i] = st.count(i)
# print(out)


out = {}
for i in st:
    if not i == " ":
    
        if i not in out:
            
            out[i] = 1
        else :
            out[i] += 1
print(out)



#wap to remove the vovels from the string

st = "apple"
# o/p = "pple"

out = {}
for val in st:
    if val not  in "aeiouAEIOU":
        out[i] = out[i] + val
print(out)




# wap to count the vovels character 

st = "python is easy"
# o/p = {"o" : 1, "a": 1......}

out = {}
for i in st:
    if i in "aeiouAEIOU":
        if i not in out:
            out[i] = 1
        else : out[i] = out[i] + 1
    print(out)

# wa pto find the longest substring

st = "python is a programming languge"
# o/p = "programming"
out = ""
length = 0
for val in st.split():
    if len(i) > length:
        length = len(i)
        out = i
print(out)


# wap to print the plaindrome string in a given list

l = ['mom','sapna','dream','dad','tamil']
o/p = ['mom', 'dad','']
        