import csv

Headding = ['Name', 'Department', 'Year of Joinning', 'Salary']
  
rowsContent = [ ['shubham', 'Software', '2020', '30000'], #data
                ['Akash', 'Finance', '2021', '25000'],
                ['pratik', 'HR', '2022', '35000'],
                ['Mayur', 'Testing', '2022', '32000']]
  
filename = "EmployeeDetails.csv" #file name
with open(filename, 'w') as csvfile:

    csvwriter = csv.writer(csvfile)  #object

    csvwriter.writerow(Headding)  #headding
    
    csvwriter.writerows(rowsContent)  #row content