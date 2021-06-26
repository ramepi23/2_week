def big_fibonacci(n):
    a,b = 1,1 
    if n == 1:
        return 1 
    
    while len(str(b))<n:
        a,b = b,a+b
        
    return b 