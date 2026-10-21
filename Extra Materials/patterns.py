'''
*         
*         
*         
*         
* * * * *

num = 5
for i in range(1,num+1):
    for j in range(1,num + 1):
        if j == 1 or i == 5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''
'''
* * * * * 
        * 
        * 
        * 
        * 

num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i == 1 or j == 5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''


'''
* * * * *  
*       *  
*       *  
*       *  
* * * * *
num = 5
for i in range(1,num + 1):
    for j in range(1,num +1):
        if i == 1 or  j == num or i == num or j == 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''


'''
  *
    *
      *
        *
      *
    *
  *
*
    
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i == j:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i + j == num:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''


'''
*               *   
  *           *     
    *       *       
      *   *         
        *  
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i == j:
            print("*",end=" ")
        else :
           print(" ",end=" ")
    for j in range(1,num+ 1):
        if i + j == num:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''

'''
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * * 
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i + j == num + 1 or i == j or j == 1 or i == 1 or j == 5 or i == 5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''

'''
* 
* * 
* * * 
* * * * 
* * * * * 

num = 5
for i in range(1,num + 1):
    for j in range(1,i + 1):
        print("*",end=" ")
    print()

'''

'''
* * * * * 
* * * *   
* * *     
* *       
* 
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i + j == num+1 or i + j < num+1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
'''

'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i + j == num+1 or i + j >= num+1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''


'''
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i >= j:
            print("*",end=" ")
    for j in range(1,num + 1):
                if i + j <= num:
                    print("*",end=" ")
                else :
                    print(" ",end=" ")   

        
    print()
'''

'''''
* * * * * 
  * * * * 
    * * * 
      * * 
        *
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i<= j:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

'''

'''''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
num = 5
for i in range(1,num + 1):
    for j in range(1,num + 1):
        if i>= j:
            print("*",end=" ")
    print()
for i in range(1,num):
    for j in range(1,num):
            if i<= j:
                print("*",end=" ")
    print()
    

'''

# num = 5
# for i in range(1,num + 1):
#     for j in range(1,num + 1):
#         if (j==1 and i!=1) or (i==1 and j!= 1) or () :
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()


head = [1,1,2,3,3]
out = []

for i in head:
    if i not in out:
        out = out + [i]
print(out)