# nested for loop :  writing a for loop  inside another for loop is called asnested for loop
#                    it is possible to write n no. of for loop inside a single for loop

# syntax : for var1 in collections:
#               for var2 in collection:

# eg. : 

'''
for i in range(1,7):
    for j in range(1,3):
        print(i,j)

'''

# wap to count the no. of vovels of each word in a given string 

'''
st = "python is very easy"
#o/p {"python" : 1,"is" : 1, "very" : 1, "easy" : 2}

d = {}
for i in st.split():
    count = 0
    for j in i:
        if j in "aeiouAEIOU":
            count = count + 1
    d[i] = count
print(d)
'''

'''
st = "aaaaabbbbbcccdd"
#o/p = "a5b4c3d2"

out = ""
for i in st:
    count = 0
    if i not in out:
        for j in st:
            if i == j:
                count = count + 1
        out = out + i + str(count)
print(out)
'''

'''
st = "python is very easy"
#o/p = [('python',6),('is',2),('very', 4),('easy' , 4)]

out = []

for i in st.split():
    length = 0
    for j in i:
        length = length + 1
    out = out +[(i,length)]
    # out.append((i,length))
print(out)
'''

'''
st = "python is very easy"    
# o/p = ['python', "is", "very","easy"]

out = []
word = ""
for i in st:
    if not i  == " ":
        word = word + i
    else : 
        out = out + [word]
        word = ""
out = out + [word]
print(out)
'''

'''

st = "java is dabba language"
# o/p = {'java' : ["java",2,'avaj'] , "is" :["is" , 1, 'si'] , "dabba" : ["dabba" , 2,"abbad"].......}
out = {}

for word in st.split():
    max_count = 1
    for i in range(len(word)):
        count = 0
        for j in range(len(word)):
            if word[i] == word[j]:
                count += 1
        if count > max_count:
            max_count = count
    out[word] = [word, max_count, word[::-1]]
print(out)
'''

'''
st = "kabab is love"
# o/p = {"kabab" :["babak", 2 ,kbb],}
out = {}

for word in st.split():
    max_count = 0
    rev = ''
    for i in word:
        max_count+=1
        rev = i+rev 
    out[word] = [rev ,max_count,word[::2]]
print(out)
'''


'''
st = "kabab is love"
out = {}

for i in st.split():
    vovel_count = 0
    rev = ""
    even = ""

    for index,value in enumerate(i):
        if value in "AEIOUaeiou":
            vovel_count = vovel_count + 1
        rev = value + rev

        if index % 2 == 0:
            even = even + value
    out[i] = [rev,vovel_count,even]
print(out) 


st = "kabab is love"
out = {}

for i in st.split():
    vovel_count = 0
    rev = ""
    even = ""

    for index,value in enumerate(i):
        if value not  in "AEIOUaeiou":
            vovel_count = vovel_count + 1
        rev = value + rev

        if index % 2 == 0:
            even = even + value
    out[i] = [rev,vovel_count,even]
print(out) 

'''

'''
num = [10,200,35,40,60]
# o/p = [335,235,400,395,375]
out = []
sum = 0
for i in num:
    sum = sum + int(i)
    for j in int(i):
        out = out + sum
        print(out)


'''





l = [100, 200, 50, 400, 300]
target = 300

out = []

for i in range(len(l)):
    if l[i] == target:
        out = out + [[l[i]]]

    for j in range(i + 1, len(l)):
        if l[i] + l[j] == target:
            out = out + [[l[i], l[j]]]

print(out)
    


