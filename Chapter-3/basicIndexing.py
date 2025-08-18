name = "SUBHANKAR"

sortName = name[0:3] # This will print the first three characters of the string, starting from index 0 and going up to 2 (but not including) index 3

sortName2 = name[0:-1] # This will print the string from the start up to the second to last character
sortName3 = name[-4:-2] # This will print the string from the start up to the third to last character
sortName4 = name[2:] # This will print the string from the third character to the end

print (f"The name is: {name}")
print (f"The sorted name is: {sortName}")
print (f"The sorted name with negative indexing is: {sortName2}")
print (f"The sorted name with negative indexing is: {sortName3}")
print (f"The sorted name with negative indexing is: {sortName4}")
