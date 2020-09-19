import os
import csv

file_path = os.path.join("Resources", "election_data.csv")

candidate_list = {}
myTotalNum_votes = 0


with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        myTotalNum_votes +=1
        if row[2] in candidate_list:
            candidate_list[row[2]] +=1
        else:
            candidate_list[row[2]] = 1
            print(row[2])

print(f"Total Number of Votes: {myTotalNum_votes}")

Election_winner = ""
current_top_votes = 0

for candidate in candidate_list:
    if candidate_list[candidate] > current_top_votes:
        Election_winner = candidate
        current_top_votes = candidate_list[candidate]

print(f"Election Winner: {Election_winner}")
print(current_top_votes)


            



