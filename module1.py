# function of printline
def printline(x):
    line=''
    for i in range(1,35,1):
        line=line+x
    print(line)

# function of rectangle    
def rectangle(l,b):
    return l*b

# function of circle
def circle(r):
    return(0.5*r*r)

# function of final amount
def finalA(pa,r,p):
    return(pa+(pa*r*p))

# function of biggest among three nos
def biggA3(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c   

# function of product of n nos    
def pon(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

# function of temprature conversion
def temp(c):
    return c*(9/5)+32