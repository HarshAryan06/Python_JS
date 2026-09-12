class SBI_BANK:
    loactions = "bengaluru"
    Branch     = "marathali"
    def __init__(self,name,age):
        self.n = name
        self.a = age

cust1 = SBI_BANK("Harsh",20)
cust2 = SBI_BANK("Aryan",18)

print(cust1.n,cust1.a)

# object name inside the class
# word self outside of the class