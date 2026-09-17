class Sample:
    a = 5
    b = 10
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def m1(self):
        print(self.v1,self.v2)              # object method
        self.v1 = 1000


obj1 = Sample(500,600)
obj2 = Sample(700,800)

obj1.m1()                               # callinf by object 
obj2.m1()
print("-----------------------")
Sample.m1(obj1)                             # calling by class_reference
print(obj1.v1)