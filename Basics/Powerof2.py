def powerOfTwo(power):

    i = 1
    result = 1
    while i <= power:
        result = result * 2
        i = i + 1
        print(result)

input = int(input("Power for 2 : "))
powerOfTwo(input)