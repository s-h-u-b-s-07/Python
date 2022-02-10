import math

# the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3
# please enter values accordingly.

v = float(input('Wind speed in miles/hours: '))
t = float(input('Wind Temperature in Farenhite: '))

#formula for WindChill
w = 35.74 + 0.6215*t + 0.4275*t*v**0.16 - 35.75*v**0.16
print('The WindChill is',int(round(w,0)))