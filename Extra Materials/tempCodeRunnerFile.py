ch = {"a" : 1, "b" : "hello" , "c": 33}
ans = {}
for val in ch:
    ans = {val : ch[val]} | ans
print(ans)