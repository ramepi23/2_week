def solve_quadratic(a,b,c):
    d = (b**2) - (4*a*c)

    if d == 0:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        return(int(x1)) 
    elif d>0:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
        return(int(x1),int(x2))

