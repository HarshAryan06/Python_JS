num = 5
space = num // 2
star = 1
for ev in range(1,num + 1):
    for col1 in range(1,space + 1):
        print(" ",end=" ")
    data = 1
    for col2 in range(1,star + 1):
        print(data,end= " ")
        if col2 < star // 2 + 1:
            data = data + 1
        else :
            data = data - 1
    print()
    if ev <  num // 2 + 1:
        space = space - 1
        star = star + 2
    else:
        space = space  + 1
        star = star - 2