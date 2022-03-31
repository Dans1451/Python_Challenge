import os
import csv
from tokenize import Name

row_count = 0
rows=[]
Ballot_ID = []
county = []
Candidate = []
CanNames=[]


with open (r".\Resources\election_data.csv") as csvfile:
    electionCSV = csv.reader(csvfile, delimiter=",")
    next(electionCSV)
    for row in electionCSV:
            rows.append(row)
for r in rows:
    Ballot_ID.append(int(r[0]))
    county.append(r[1])
    Candidate.append(r[2])
total_votes=len(Ballot_ID)
print(total_votes)

for l in range(len(Candidate)):
    if Candidate[l] not in CanNames:
        #print(Candidate[l])
        CanNames.append(Candidate[l])
Can_Total=[]
#total=0
Cname=Candidate[0]
#print(CanNames)
Vote_Name = list(zip(Ballot_ID, Candidate))
#print(Vote_Name[0])
#for i in range(0,len(Vote_Name)):
def CanVotes(Name_Of_C):
    total = 0
    for row in Vote_Name:
        if row[1] == Cname:
            total = total+1
            #print(total)
    return total
for Cname in CanNames:
    total = CanVotes(Cname)
    #print(total)
    Can_Total.append(Cname)
    Can_Total.append(total)
#print(Can_Total)

Can1 = [CanNames[0], f"{round(int(Can_Total[1])/int(total_votes),2)*100}%", f"({Can_Total[1]})"]
#print(Can1)
Can2 = [CanNames[1], f"{round(int(Can_Total[3])/int(total_votes),2)*100}%", f"({Can_Total[3]})"]
#print(Can2)
Can3 = [CanNames[2], f"{round(int(Can_Total[5])/int(total_votes),2)*100}%", f"({Can_Total[5]})"]
#print(Can3)

if Can_Total[3] > Can_Total[1]and Can_Total[3]>Can_Total[5]:
    winner = Can_Total[2]
elif Can_Total[5]>Can_Total[3]and Can_Total[5] and Can_Total[1]:
    winner = Can_Total[4]
else:
    winner = Can_Total[0]
#print(winner)

output= ["Election Results","-------------", f"Total Votes: {total_votes}","----------",str(Can1),str(Can2),str(Can3),"------------",f"Winner: {winner}"]
#print(output)
for line in output:
    print(line)

with open(r'.\Analysis\poll_data.txt', 'w') as f:
    for line in output:
        f.write(line)
        f.write('\n')
#         print(row[i-1])
#         if row[i+1] == row[i]:
#             total = int(total) + int(row[i-1])
#         else:
#             #total = int(total) + int(row[i-1])
#             Can_Total.append(total)
#             toal=0
# print(Can_Total)