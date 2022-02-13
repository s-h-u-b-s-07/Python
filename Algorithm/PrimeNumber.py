for Num in range(1, 1000):  #looping for the range 1 to 1000
    counter = 0
    for i in range(2, (Num//2 + 1)):   #iterating in rage 2 to next numbr
        if(Num % i == 0):              # remainder = 0 then dont print nuber go to next number
            counter = counter + 1
            break

    if (counter == 0 and Num != 1):     
        print(" %d" %Num, end = '  ')       