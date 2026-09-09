#  Comprehensions / Expression 

# list 
# tuple
# set 
# dict

#list comprehensions : syantax  [val for loop]
# [val for val in range(1,5)]
# [val * 2 for val in range(1,5)]

# s = 'abcd'
# print(list(s))
# [ch for ch  in s]

# s = "abcd"              # o/p -> ["a" , "bb" , "ccc" , "dddd"]
# print([s[ind] * (ind + 1) for ind in range(len(s))])

# l1 = [20,30,40]             #op -> [23 ,34,45]
# l2 = [3,4,5]

# print([l1[ind] + l2[ind] for ind in range(len(l1))])


# list(range(1,11))
# l = []
# for val in range(1,11):
#     if val % 2 == 0:
#         l.append(val)

# print(l)

# # syntax = [ val for loop if condition]

# val = [2,4,6,8,10]
# print([val for val in range(1,11) if val % 2 == 0])

# Q write a program to print the factors of a number 

# num = 8
# print(value for value in range(1,num + 1) if num % value == 0)

# num = 8
# print([val for val in range(1,num + 1) if num % val == 0])
# num = 8
# print("prime" if len([val for val in range(1,num + 1) if num % val == 0]) == 2 else "np")

# num = 11
# print("prime" if num > 1 and len([val for val in range(2,int(num ** 0.5) + 1) if num % val == 0]) == 0 else "np")



# Q s = "abcd"

# op = ["a","ab", "abc", " abcd", "b", "bc" , "bcd", "c", "cd", "d"]
# s = "abcd"
# l = []
# for ind in range(len(s)):
#     for ind2 in range(ind + 1,len(s) + 1):
#         l.append((s[ind : ind2]))
        
# # print(l)

# s = "abcd"
# print([s[ind : ind2] for ind in range(len(s)) for ind2 in range(ind + 1,len(s) + 1)])


# Q. write a program to print vowels from a string
s = "abcdefghij"

print([ch for ch in s if ch in "aeiouAEIOU"])

# Q . write a program to print char which are not digit

s = "a4bg@c d8#U"

print([ch for ch in s if ch in "1234567890"])

#Q write a program to print th character from a string

s = "a4bg@c d8#U"

print([ch for ch in s if "a" <= ch <= "z" or "A" <= ch <= "Z"])     # using asci

print([ch for ch in s if ch.isalpha()])             #using ialpha


s = "12456789"

for num in s:
    if num > str(5):
        print(num)

print([num for num in s if num > str(5) ])


s = ["hello", "happy birth" , "google", "apple"]

print([ch for ch in s if len(ch) > 10 ])


s = [-1 , -10 , -9 , 10]
for num in s:
    if num < 0:
        num = -num
    print(num)

