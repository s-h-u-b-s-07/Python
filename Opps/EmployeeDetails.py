import csv

class Employee:   #Employee class
    def __init__(self, name, department, join_year, salary): # constructor
        self.name = name               # instantiating object
        self.department = department
        self.join_year = join_year
        self.salary = salary

    def display(self):
        return self.name, self.department, self.join_year, self.salary


Headding = ['Name', 'Department', 'Year of Joinning', 'Salary']

rowsContent = [Employee('shubham', 'Software', '2020', '30000'),  # data
               Employee('Akash', 'Finance', '2021', '25000'),
               Employee('pratik', 'HR', '2022', '35000'),
               Employee('Mayur', 'Testing', '2022', '32000')]

filename = "EmployeeDetails.csv"  # file name
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)  # object

    csvwriter.writerow(Headding)  # headding  writerrow for single row printing
    for i in rowsContent:
        csvwriter.writerow(i.display())  # row content writerrows for multible row printing