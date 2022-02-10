row = int(input("Rows:"))
col = int(input("Columns:"))

matrix = []
print("Enter the entries row wise:")

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
print("Printing Array in the Matrix Form : ")
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()