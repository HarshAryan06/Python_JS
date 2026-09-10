class student:
    loacation = "Banglore"
    course = "Python"

harsh = student()
aryan = student()
roy =  student()

print(harsh.loacation)      #object referneces 
print(student.loacation)    # class refernces

print("-------------------------------")
harsh.course = "SQL"            
student.loacation = "Goa"
print(harsh.course)      # object reference
print(aryan.loacation)