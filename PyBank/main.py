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


myAvgProfit = total_net/myLength
myAvg = "{:.2f}".format(myAvgProfit)
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {myLength}")
print(f"Total: {total_net}")
print(f"Average Change: {myAvg}")
print(f"Greatest Increase in Profits: {myMax}")
print(f"Greatest Decrease in Profits: {myMin}")

output_path = os.path.join("Analysis", "budget_analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Months', 
        'Net Profits', 
        'Average Change', 
        'Greatest Increase Date', 
        'Greatest Increase Amount',
        'Greatest Decrease Date',
        'Greatest Decrease Amount'
    ])
    csvwriter.writerow([myLength,
        total_net,
        myAvg,
        myMax[0],
        myMax[1],
        myMin[0],
        myMin[1]
    ])