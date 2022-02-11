def bubblesort(Num):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(Num)-1, 0, -1):
    for i in range(n):
      if Num[i] > Num[i + 1]:
        # swapping data if the element is less than next element in the array
        Num[i], Num[i + 1] = Num[i + 1], Num[i]
Num = [10,9,8,7,6,5,4,3,2,1,0]
  
print("Unsorted list is,") 
print(Num)
bubblesort(Num)
print("Sorted Array is, ")
print(Num)