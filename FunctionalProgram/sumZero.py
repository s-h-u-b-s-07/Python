def triplets(num):
    for i in num:
        for j in num:
            for k in num:
                if (i + j + k) == 0:
                    print(f"{i} + {j} + {k} = 0")

if __name__ == '__main__':
    num = list()
    n = int(input("Enter the total number you want to enter: "))
    for i in range(n):
        a = int(input("Number of elements in the array: "))
        num.append(a)
    
    triplets(num)