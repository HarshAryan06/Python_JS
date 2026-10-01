# wap to find the most repeated char from the given string 
'''
st = "aaabbbcc"
max_count = 0
char = None

for i in st:
    if st.count(i) > max_count:
        max_count = st.count(i)
        char = i

print(f"most repeated char --> {char}")
'''

# wap to exatrat all the key value pairs from the dict only if the key are of string datatype and values are integer
 
'''
d = {10:'hello','a':[10,20,30],'b':20,'c':{10,20},'d':40}

out = {}
for i in d:
    if type(i) == str and type(d[i]) == int:
        out[i] = d[i]
print(out) 
'''


# wap to extract key value pairs from the dict only if both keys and values are exactly same
'''
d = {'a':'a','b':'bob',10:10,20:200}

out = {}
for i in d:
    if (i) == (d[i]):
        out[i] = d[i]
print(out)

'''

# wap to get the following output
# s = 'power star'
# out = {'power': 5, 'star': 4}
'''
s = "power star"

out = {}
for i in s.split():
    out[i] = len(i)
print(out)

'''

# wap to get the following output
# s = 'power star'
# out = {'power': rewop, 'star': rats}

'''
s = "power star"
out = {}

for i in s.split():
    out[i] = s[::-1]
print(out)
'''


# wap to extract all the non default values from the list
'''
s = [0,10,None,0.0,"python"]
out = []
for i in s:
    if bool(i) == True:
        out = out + [i]
print(out)
'''
# wap to replace the space by * present in a string

'''
s = "hello goodmorning"
space = ""
for i in s:
    if i == " ":
        space = space + "*"
    else: space = space + i
print(space)
'''

# wap to get the follwing output 
# s = 'always keep smiling

'''
s = 'always keep smilling'
out = " "
for i in s.split():
    out = out + i[::-1] + " " 
print(out)
'''



# wap to get the follwing output
# s  = "push maandi kushi padi"

#out = {"push" : "ph" , "maandi" : "a" , "kushi" : 'a' , "padi" : "pi"}

'''
s  = "push maadi kushi padi"
out = {}
for i in s.split():
    if len(i) % 2 == 0:
        out[i] = i[0] + i[-1]
    else :
        out[i] = i[len(i) // 2]
print(out)

'''

# s = "jio.com fb.com osp.in edu.in file.in"
# out = {'com':["jio","fb"] , "in" : ["osp", "edu"] , "py" : ["file"]}
'''
s = "jio.com fb.com osp.in edu.in file.in"
out = {}

for i in s.split():
    if 

'''

# st = "aaaaabbbbcccdd"
# o/p = "a5b4c3d2"

'''
st = "aaaaabbbbcccdd"
out = ""

for i in st:
    if i not in out:
        out = out + i + str(st.count(i))
print(out) 
'''

# st = "76124953"
# out = "71539624"

'''
st = "76124953"

out = ""
even = ""
odd = ""

for i in st:
    if int(i) % 2 == 0:
        even = even + str(i)
    else : 
        odd = odd + str(i)
print(odd + even)

'''