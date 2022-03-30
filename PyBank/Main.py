import os
import csv

from sympy import Ne

# CSVpath = os.path.join(".","resources","PyBank", "budget_data.csv" )
# print(CSVpath)
#print("resources\PyBank\budget_data.csv")
#with open (r"C:\Users\dans1\Desktop\GT Data Analysis\Python HW\Python_Challenge\resources\PyBank\budget_data.csv") as csvfile:
row_count = 0
rows = []
with open (r".\resources\PyBank\budget_data.csv") as csvfile:
    budgetCSV = csv.reader(csvfile, delimiter=",")
    next(budgetCSV)
    for row in budgetCSV:
            row_count = row_count+1
            rows.append(row)

#print(f"rows = {rows}")
# print(row_count)
# print(rows[0][1])
# Net_Total = int(rows[86][1]) - int(rows[1][1])
# print(Net_Total)
months_list = []
for r in rows:
    months_list.append(str(r[0]))
#print(months_list)
profits = []
for r in rows:
    profits.append(int(r[1]))
total_profits = sum(profits)
#print("total profits are " + str(total_profits))

months=len(profits)
#print(f"There are {months} months of data")

months_profits = list(zip(months_list, profits))
#print(months_profits)

Profit_Changes=[]
for i in range(len(profits)):
    k=len(profits)
    #print("k is" +str(k))
    if i < k-1:
        change=int(profits[i])-int(profits[i-1])
        #print (change)
        Profit_Changes.append(change)
total_changes = sum(Profit_Changes)
#print ("total changes are " + str(total_changes))


# current=profits[0]
# for r in profits:
#     new=profits[1]
#     change=int(new)-int(current)
#     Profit_Changes.append(change)
#     current = new
#print(f"Profit_Changes = {Profit_Changes}")
#print(f"change is {change}")
Average_changes = total_changes / months
Average_changes =round(Average_changes, 2)
#print(f"The average change is {Average_changes}")

greatest = int(profits[0])
Least = int(profits[0])


for i in range(len(profits)):
    k=len(profits)
    if i < k-1:
        if greatest < int(profits[i]):
            greatest = int(profits[i])
            #print(greatest)

for i in months_profits:
    if i[1] == greatest:
        Great_Month = i
        great_string = f"${Great_Month[1]}"
        Great_Month = [Great_Month[0], great_string]
        #print(f"The greatest month was {Great_Month}")

for i in range(len(profits)):
    k=len(profits)
    if i < k-1:
        if Least > int(profits[i]):
            Least = int(profits[i])
            #print(Least)
for i in months_profits:
    if i[1] == Least:
        Least_Month = i
        least_string = f"${Least_Month[1]}"
        Least_Month = [Least_Month[0], least_string]
        #print(f"The worst month was {Least_Month}")

            
output = ["Financial Analysis",
"-----------------------",
f"Total Months: {months}",
f"Total: ${total_profits}",
f"Average Change: ${Average_changes}",
f"Greatest Increase in Profits: {Great_Month}",
f"Greatest Decrease in Profits: {Least_Month}"]

for L in output:
    print(L)

with open('budget_data.txt', 'w') as f:
    for line in output:
        f.write(line)
        f.write('\n')
