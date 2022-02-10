Year = 2025

if( Year % 400 == 0) and ( Year % 100 == 0):
    print("{} Leap Year" .format(Year))
elif( Year % 4 == 0) and ( Year % 100 != 0):
    print("{} Leap Year" .format(Year))
else:
    print("{} Not Leap Year" .format(Year))