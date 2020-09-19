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
            



Election_winner = ""
current_top_votes = 0

print("Election Results")
print("-----------------------")
print(f"Total Number of Votes: {myTotalNum_votes}")
print("-----------------------")

for candidate in candidate_list:
    if candidate_list[candidate] > current_top_votes:
            Election_winner = candidate
            current_top_votes = candidate_list[candidate]


output_path = os.path.join("Analysis", "election_analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Candidate", "Percentage Vote Won", "Number of Votes", "Total Number of Votes", "Winner"])
    for myCandidate in candidate_list:
        percent_vote = 100*candidate_list[myCandidate]/myTotalNum_votes
        formatted_percent_vote = "{:.3f}".format(percent_vote)
        print(f"{myCandidate}: {formatted_percent_vote}% ({candidate_list[myCandidate]})")
        csvwriter.writerow([myCandidate, formatted_percent_vote, candidate_list[myCandidate], myTotalNum_votes, Election_winner])

        

print("-----------------------")
print(f"Election Winner: {Election_winner}")
print("-----------------------")


            



