def printsorted(arr):   
    # Sorting using sorted function providing key as len
    print(*sorted(arr, key=len))

arr = ["Nashik", "I", "from", "am"] 
# Passing list to printsorted function
printsorted(arr)