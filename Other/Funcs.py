from math import sqrt

def discriminant(a,b,c):
    
    D = b ** 2 - 4 * a * c
    
    if D > 0:
        
        x1 = (-b + sqrt(D)) / 2
        x2 = (-b - sqrt(D)) / 2
        
        return (x1, x2)
    
    if D == 0:
        
        return (-b / 2 * a)
    
    if D < 0:
        
        return ()
    
    

def sum(a,b):
    return a + b

def mult(a,b):
    return a * b

def calc_lists(a,b,opfunc):
    result = []
    
    for numa, numb in zip(a,b):
        result.append(opfunc(numa, numb))
    
    return result



def add(x):
    
    def add_fn(y):
        return x + y
    
    return add_fn



def create_counter(init=0):
    
    count = init
    
    def increment():
        nonlocal count
        count += 1
        return count
        
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    return increment, decrement

inc, dec = create_counter(42)
print(inc())