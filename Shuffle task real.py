old_word=['This is Awsome']  
	  
	# the new words  
new_word=['Awsome this is']  
	  
def Shufflemywords(statement):  
	  # iterate over the list of old words  
    for word in old_word:  
	    # get the index of the current word  
        index = old_word.index(word)  
	  
	    # use this index to replace the two words
    statement = statement.replace(old_word[index], new_word[index])  
	  
    return statement  
	  
mystring="This is Awsome"  
mystring = Shufflemywords(mystring)  
print (old_word)  
print ("Turns into")  
print (mystring)  
