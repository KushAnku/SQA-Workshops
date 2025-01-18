# WorkShop_2 
# Ankush Singh 


def performAdd(p, q):
    return p + q 

def performSub(a, b):
    return a - b 

def performMul(x, y):
    return x * y

def performDiv(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
