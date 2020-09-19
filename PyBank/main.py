import os
import csv
file_path = os.path.join("Resources", "budget_data.csv")
total_net = 0
myLength = 0 
myMin = [' ', 0]
myMax = [' ', 0]



with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        myLength +=1
        myProfit = int(row[1])
        total_net += myProfit
        if myProfit < myMin[1]:
            myMin[0] = row[0]
            myMin[1] = myProfit

        if myProfit > myMax[1]:
            myMax[0] = row[0]
            myMax[1] = myProfit


myAvg = total_net/myLength
print (myLength)
print(myAvg)
print(myMin)
print(myMax)   
print(total_net)