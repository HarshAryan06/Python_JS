def sample(val):
    if val == 5:
        return 
    print(val)
    val1 = val + 1
    sample(val1)
    
num = 1
sample(num)