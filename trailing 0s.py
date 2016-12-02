### A factorial number is an number that is being denoted by N! this means what ever n is the equation
## is going to times n by itself then in decending order times itself
##this means 5! = 5 x 4 x 3 x 2 x 1 = 120.

def trailing_zeros_of_factorial(): 
    n = int(input("Please enter the number you would like to find the trailing 0s in"))
     
    
    assert n >= 0, n ## assert makes sure you dont have to do an if statement, it will automaticly return false if it does not meet that condition
    zeros = 0 ## 0 is the number i am starting out with (0)
    while n:
        n //= 5     ## counts how many 5s go in a number
        zeros += n ## this is the count

    return zeros


print(trailing_zeros_of_factorial())
