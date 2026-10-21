a = 0
b = 1

num = int(input("enter a number : "))

for i in range(num):
    print(a,end=" ")
    a, b   =  b , a + b

