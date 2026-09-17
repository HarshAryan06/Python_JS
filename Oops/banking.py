class SBI_BANK:
    branch_loc = "Marathali"
    IFSC_Code = "SBIN000420"
    ROI       = 0.7

    def __init__(self,name,addhar,Acc_no,Bal):
        

    def deposite(self):
        ac = int(input("Enter your account number : "))
            if self.Account == ac:
               amount =  int(input("Enter an ammount"))
               if 500 <= amount <= 20000 and amount % 100 == 0:             
                   self.Bal = self.Bal + amount
                   print("amount credited !!")
        
               else : print("invalid amount")
            else : print("your account no doesnt exist !!!!")



