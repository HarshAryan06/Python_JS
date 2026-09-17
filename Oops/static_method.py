class Sample:
    a = 30
    b = 50

    @staticmethod
    def M1():
        print("hello")

obj1 = Sample()
obj2 = Sample()

obj1.M1()
Sample.M1()