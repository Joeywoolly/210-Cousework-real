def PerfectSquare(Number): ## number is what we are looking for
  x = 0    ## x is the calculation, set x to 0
  if Number >= 0:
        while x*x < Number:
            x = x+1 ## this is the increase of the calculation, 1 x 1 /  1 x 2
            a = x*x  ##
            print(a)
        if a != Number: ## if a is not eqal to the number 5*5
          return False
        else: 
           return True
  else:
        return False
print (PerfectSquare (25))
