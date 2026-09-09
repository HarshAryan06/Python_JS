s1 = "abcd"
s2 = "mnop"
s3 = "1234"
mapobj = map(lambda a,b,c : a + b + c ,s1,s2,s3)
print(tuple(mapobj))