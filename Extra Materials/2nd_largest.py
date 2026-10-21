l = [1,50,60,45,100]

largest = 0
smallsmallest = 0

for i in l:
    if i > largest:
        smallest = largest
        largest = i
    elif i > smallest and i != largest:
        smallest = i
print(smallest)