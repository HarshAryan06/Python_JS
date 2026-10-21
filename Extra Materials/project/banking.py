import time
customer = {}

def admin():
    user = input("Enter a username : ")
    pwd  = input("Enter a password : ")
    print("\n")
    

    if user == "admin" and pwd == "admin":
        time.sleep(3)
        print("login successfully")
        return True
    else :
        time.sleep(3)
        print("login failed")
        return False

#-------------------------------- login area --------------------------------------

def account_openeing():
    account_number = 100
    while True:
        print("\n--------  𝑩𝒂𝒏𝒌𝒊𝒏𝒈 𝑺𝒚𝒔𝒕𝒆𝒎  ---------\n")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Balance Enquiry")
        print("5. Transaction History")
        print("6. View Customer Details")
        print("7. Update Customer Details")
        print("8. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            account_number = create_account(account_number)
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            Balance_Enquiry()
        elif choice == 5:
            Transaction_history()
        elif choice == 6:
            customer_details()
        elif choice == 7:
            update_details()
        elif choice == 8:
            print("Thank you visit again")
            break


def create_account(account_number):
    
    name = input("Enter ur name : ")

    if len(name) >= 32:
        print("invalid username !!")
        return account_number

    phone = (input("Enter ur phone number : "))
    if len(phone) != 10 or not phone.isdigit():
        print("invalid phone")
        return account_number

    aadhaar_no = (input("Enter ur aaddhar no : "))
    if len(aadhaar_no) != 12 or not aadhaar_no.isdigit():
        print("invalid aadhaar !!")
        return account_number

    dob = input("enter ur a date of birth ''d/m/y'' ")
    if dob == "":
        print("invalid dob !!")
        return account_number

    pan = input("Enter ur pan_no : ")
    if len(pan) != 10:
        print("invalid pan_no !!")
        return account_number

    email = input("Enter ur email address : ")
    if "@" not in email or "." not in email:
        print("invalid email address")
        return account_number

    nomine = input("Enter ur nomine name : ")
    if nomine == "":
        print("nomine required !! ")
        return account_number    


    customer[account_number] = {
        "name" : name,
        "phone" : phone,
        "aaddhar" : aadhaar_no,
        "dob" : dob,
        "pan" : pan,
        "email" : email,
        "nomine" : nomine,
        "balance" : 0,
        "transaction" : []
    }

    print("Account created !!!")
    print(f"account number :{account_number}")

    account_number = account_number + 1
    return account_number


def deposit_money():
    account_number = int(input("Enter your account number : "))

    if account_number in customer:
        amount = int(input("Enter a deposite amount : "))

        if amount > 0:
            customer[account_number]["balance"] = customer[account_number]["balance"] + amount

            customer[account_number]["transaction"].append("Deposited : " + str(amount))

            print("Money deposited successfully !")
            print(f"current balance : {customer[account_number]["balance"]}")

        else : print("amount must be greater than --> 0 ")

    else : print("account not found !!! ")


def withdraw_money():
    account_number = int(input("Enter account number : "))

    if account_number in customer:
        amount = int(input("enter withdraw amount : "))

        if amount < 0:
            print("amount must be greater than 100")

        elif amount > customer[account_number]["balance"]:
            print("insufficent balance in ur account")
        else :
            customer[account_number]["balance"] = customer[account_number]["balance"] - amount
            customer[account_number]["transaction"].append("Withdraw : " + str(amount)) 

            print("withdraw successfull !!!")
            print(f"current balance : {customer[account_number]["balance"]}")

    else : print("account number not found")


def Balance_Enquiry():
    account_number = int(input("Enter a account number : "))

    if account_number in customer:
           print(f"account balance : {customer[account_number]["name"]} : {customer[account_number]["balance"]} ")

    else : print("account not found !!!")

def Transaction_history():
        account_number = int(input("Enter a account number : "))
           
        if account_number in customer:
            print("Transaction history")

            transaction = customer[account_number]["transaction"]

            if len(transaction) == 0:
                print("no transaction there !!")

            else :
                for i in transaction:
                    print(i)

        else :
            print("no account found !!!")


def customer_details():
    account_number = int(input("Enter a account number : "))
               
    if account_number in customer:
        print("---customer details--")
        print(f"A/C : {account_number}")
        print(f"name : {customer[account_number]["name"]}")
        print(f"phone : {customer[account_number]["phone"]}")
        print(f"aaddhar : {customer[account_number]["aaddhar"]}")
        print(f"dob : {customer[account_number]["dob"]}")
        print(f"pan : {customer[account_number]["pan"]}")
        print(f"email : {customer[account_number]["email"]}")
        print(f"nomine : {customer[account_number]["nomine"]}")
        print(f"balance : {customer[account_number]["balance"]}")

    else :
        print("Account not found !!")

def update_details():
    account_number = int(input("Enter a account number : "))

    if account_number in customer:
        print("update customer details ")

        print("1. update phone")
        print("2. update email")

        choice = int(input("Enter a choice : "))

        if choice == 1:
            phone = input("Enter ur new phone number : ")
            if len(phone) == 10 and phone.isdigit():
                customer[account_number]["phone"] = phone
                print("phone no updated  ")

            else : print("invalid phone number ")

        elif choice == 2:
            email = input("Enter new email : ")
            if "@" not in email or "." not in email:
                    print("invalid email address") 

    else :
        print("Account not found")

def main():
    if admin():
        account_openeing()
main()

