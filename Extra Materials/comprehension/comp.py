# comprehension 

# can be done only for the matuable data types  


# wap to check if the string start with vovels or not if it is reverse it and it to list else add as it is 

l = ["apple","mango","orange","banana","grapes"]
out = [ i[::-1] if i[0] in "AEIOUaeiou" else i  for i in l ]
print(out)

# wap to extract only vovels from the string to the list 

s = "programming language"

out = [i for i in s if i in "AEIOUaeiou"]
print(out)

# wap to check the number endwith even or not if it is even multiply by 10 else multiply by 5 and add it to the list

s = [1234,45645,436239,56432]

out = [ i*10 if i%10%2 == 0 else i * 5 for i  in s]
print(out)

# convert all the string in ["python","java","sql","excel"] to uppercase

l = ["python","java","sql","excel"]

out = [i for i in l if l.isupper(i)]
print(out)

# given number = [2,5,8,11,14,17,28] extract only the number greater than 10

num = [2,5,8,11,14,17,28]
out = [ i for i in num if i > 10]
print(out)

# given words = ["apple", "cat", "banana" , "dog", "elephant"] create a list containing the length of each word 

s = ["apple", "cat", "banana" , "dog", "elephant"]

out = []
for i in s :
    out = out + [len(i)]
print(out)

