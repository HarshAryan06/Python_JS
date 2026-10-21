# a = 5
# b = a
# print(a)
# print(b)

# def func1():
#     print("hi")
#     def func2():
#         print("hello")
#     return func2

# print(func1)
# dup = func1
# print(dup())

def outer(arg):                         
    print(f'arg = {arg}')
    def Inner():
        print(f"inner = {Inner}")
    return Inner

@outer
def func1():
    print("Hello")

print(f'Func1 = {func1}')
func1()

