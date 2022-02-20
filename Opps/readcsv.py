import csv

from EmployeeDetails import Employee

with open('EmployeeDetails.csv') as file:
    reader = csv.reader(file) # .reading the file
    for rowsContent in reader:
        print(rowsContent)