from Stack import StackADT

def reverseStr(str, capacity = 100):
    s = StackADT(capacity)
    
    for c in str[::-1]:
        s.push(c)

    return s.array

    

