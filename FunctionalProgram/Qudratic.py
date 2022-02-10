import cmath  #complex math

a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter vaule of c :'))

Delta = (b*b) - (4*a*c) #calculate delta

FirstRoot = (-b + cmath.sqrt(Delta))/(2*a) #1st root of x
secondRoot = (-b - cmath.sqrt(Delta))/(2*a) #2nd root of x

print(FirstRoot)
print(secondRoot)