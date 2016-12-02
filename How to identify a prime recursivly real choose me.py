LookngforPrime= 7
LookngforPrime*=1
prime = True    ##way to test if it is prime is to divide every number less than n
                ##into n and if none divide then answer Yes. If any divide then answer No
for divisor in range(2,LookngforPrime):
    if LookngforPrime/divisor==int(LookngforPrime/divisor):   ## divides the start number by the divisor
        prime=False
if prime==False:
    print (LookngforPrime," is not prime")
else:
    print (LookngforPrime, "is prime")
