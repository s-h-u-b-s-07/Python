def harmonic_number(number):
    initial = 2
    harmonic = '1'
    result = 1
    while initial <= number:
        harmonic = harmonic + '+1/' + str(initial)
        result = result + 1 / initial
        initial = initial+1
    print(harmonic+"=" + str(result))

input_number = int(input("Enter Nth number of Harmonic series : "))
harmonic_number(input_number)