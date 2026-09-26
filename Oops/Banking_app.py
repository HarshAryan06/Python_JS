class SBI_BANK:
    branch_loc = "Marathali"
    IFSC_Code = "SBIN000420"
    ROI       = 0.7

    def __init__(self,name,Addhar,Acc_no,Bal,pin):
        self.name = name
        self.Addhar = Addhar
        self.Acc_no = Acc_no
        self.Bal = Bal
        self.pin = pin

    @classmethod
    def Change_loc(cls):
        cls.branch_loc = "Jamshedpur"

    @staticmethod
    def Get_Password():
        pwd = int(input("Enter a 4 - digit pin : "))
        return pwd

    def Check_Bal(self):
        count = 3
        while count > 0:
            print(f"Attempt left {count}")
            if self.Get_Password() == self.pin:
                print(f"Available bal is {self.Bal}")
                break
            else : 
                print("Incorrect password !!")
                count = count - 1
        else :    
            print("no attemp left ")
            print("try after 24hr")


    def With_Draw(self):
        amount = int(input("Enter the amount : "))
        if 100 <= amount <= 20000 and amount % 100 == 0:
            if self.Bal >=  amount:
                self.Bal = self.Bal + 

       
    def deposite(self):
        ac = int(input("Enter your account number : "))
        if self.Account == ac:
               amount =  int(input("Enter an ammount"))
               if 500 <= amount <= 20000 and amount % 100 == 0:             
                   self.Bal = self.Bal + amount
                   print("amount credited !!")
        
               else : print("invalid amount")
        else : print("your account no doesnt exist !!!!")



