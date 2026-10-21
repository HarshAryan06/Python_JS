# calculator  program

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def sub(a,b):
    return a - b

def div(a,b):
    return a / b


def main():
    while True:
        print("\n-------- Welcome to my Calculator -----\n")
        n1 = int(input("Enter a number 1 : "))
        n2 = int(input("Enter a number 2 : "))
        print("1.Addition\n2.Substraction\n3.multiplication\n4.Division\n5.quit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            print(add(n1,n2))
        if choice == 2:
            print(sub(n1,n2))
        if choice == 3:
            print(mul(n1,n2))
        if choice == 4:
            print(div(n1,n2))
        if choice == 5:
            break
    
main()


