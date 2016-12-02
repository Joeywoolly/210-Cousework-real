def BinarySearch(Myitem, Mylist):     ## Function name and arguments
	    first = 0   ## the start of the list
	    last = len(Mylist)-1 ## the end of the list
	    #print(last)
	    found = False  
	
	    while first <= last and not found: ## ignore the the found assignment
	        mid = (first + last)//2 ##splits the list in two
	      
	        if Mylist[mid] == Myitem:##if the value is in the middle of the list
	            found = True ## display True
	            
	        else:
	            if Mylist[mid] < Myitem: ##if it is not, it searches down the list
	                first = mid +1
	            else:
	                last = mid-1
	
	    return found
	
#Sorted =  ## sorted list of numbers


print(BinarySearch( 4,[1,2,3,4,5,6,7,8,9])) ## using the Binary search function to search for number 2

##The output should be TRUE

