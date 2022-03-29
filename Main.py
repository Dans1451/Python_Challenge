import os
import csv

CSVpath = os.path.join("resources","PyBank", "budget_data.csv" )

with open (CSVpath) as csvfile:
    
    budgetCSV =  csv.reader(csvfile, delimiter=",")
print(budgetCSV)