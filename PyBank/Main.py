#Dependencies
import os
import csv

#from sympy import Ne
csvfile=os.path.join("Resources","budget_data.csv")
row_count = 0
rows = []
with open (r".\Resources\budget_data.csv") as csvfile: #Open and read CSV
    budgetCSV = csv.reader(csvfile, delimiter=",")
    next(budgetCSV)
    for row in budgetCSV:
            row_count = row_count+1
            rows.append(row)


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
        change=int(profits[i+1])-int(profits[i])
        print (change)
        Profit_Changes.append(change)
total_changes = sum(Profit_Changes)
print ("total changes are " + str(total_changes))



Average_changes = total_changes / (months-1)
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

with open(r'.\Analysis\budget_data.txt', 'w') as f:
    for line in output:
        f.write(line)
        f.write('\n')
