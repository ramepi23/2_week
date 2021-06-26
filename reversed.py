def my_reverse(X):
    reversed_list = []
    length = len(X) - 1 
    
    while length > -1 : 
        reversed_list.append(X[length])
        length -= 1 
    
    return reversed_list 