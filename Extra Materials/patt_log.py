# st = "abc**ab*ac*"
# o/p = "aaa"

st = "abc**ab*ac*"
out = ""

for i in st:
    if i == "*":
        out = out[:-1]              
    else :
        out = out + i
print(out)