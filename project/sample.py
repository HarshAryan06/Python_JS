from time import sleep
import random

dummy_dm = {"admin" : "pwd"}

print("The Indian Dhaba")
print("-----------------------")
print("1. Login\n2. signup\n")

choice = int(input("Enter a choice : "))
if choice == 1:
    username = input("Enter a username : ")
    if username in dummy_dm:
        password = input("Enter ur password : ")
        if password in dummy_dm:
            print("loading.........")
            print("login successfully")
        else : print("wrong passwrod")
    else : print("invalid username")



#------------------------------------------------------------


elif  choice == 2:
    first_name  = input("Enter a firstname : ")
    last_name   = input("Enter a lastname : ")
    email       = input("Enter an mail_id : ")
    mobile_no   = input("Enter a mobile_no : ")
    print("account creating...........")
    sleep(3)
    



# username = "admin"
# password = "pwd"



# print("Enter your choice : ")

# if choice == 1:
#     username = print("Enter a username : ")
# else : print("invalid choice !!!")

