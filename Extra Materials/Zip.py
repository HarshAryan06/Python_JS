# s = "ABCD"
# l = [10,20,30,42]

# print(dict(zip(s,l)))

'''
s = "ABCD"
l = [65,66,67,68]

d = {}
for i in zip(s,l):
    d[i[0]] = i[-1]
print(d)
'''

'''
cities = ["banglore","bhubaneswar","chennai","pune","kochi"]
pop = [1500000,6000000,5000000,680000,620000]

d = {}

for i in zip(cities,pop):
    if pop[-1] < 15000555:
        d[i[0]] = i[-1]
print(d)
'''

'''
emp = ['Harsh',"Rahul","vishnu","hanmant",]
salary = [25000,2000,15000,20000]

d = {}

for i in zip(emp,salary):
    d[i[0]] = i[-1] + i[-1] * 10//100 
print(d)
'''

# wap to print the product name and its price and find the highest and lowest price along with their product names 
prod = ['iphone','laptop','fridge','shoes','watch']
price = [170000,10000,55000,2000,1500]

d = {}
largest = 0
smallest = price[3]
highest_prod = {}
lowest_prod = {}

for pro,cost in zip(prod,price):
    d[pro] = cost
    if cost > largest:
        highest_prod = cost
    if cost < smallest:
        lowest_prod = cost
print(d)
print(pro,highest_prod)
print(pro,lowest_prod)

