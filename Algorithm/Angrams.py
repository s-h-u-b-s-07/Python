def checking(string1, string2): # function for checking strings

    if(sorted(string1) == sorted(string2)): #Equality check for string
        print("These strings are anagrams.")
    else:
        print("These strings are not anagrams.")        
         
string1 ="ear"
string2 ="are"
checking(string1, string2) # calling function