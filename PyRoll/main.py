#import dependencies
import os
import csv

#set data source file path
file_path = os.path.join("Resources", "election_data.csv")

candidate_list = {}
myTotalNum_votes = 0

#read in data
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #every new row is a new person's vote so add it to the total number of votes cast
        myTotalNum_votes +=1

        #check to see if the candidate voted for has already been voted for
        #if they have then add one to their vote total
        if row[2] in candidate_list:
            candidate_list[row[2]] +=1
        else:
            #candidate is new so initialize their vote total to one
            candidate_list[row[2]] = 1
            



Election_winner = ""
current_top_votes = 0

#results print out
print("Election Results")
print("-----------------------")
print(f"Total Number of Votes: {myTotalNum_votes}")
print("-----------------------")

#calculate the winner of the election by determining the candidate with the most votes
for candidate in candidate_list:
    if candidate_list[candidate] > current_top_votes:
            Election_winner = candidate
            current_top_votes = candidate_list[candidate]

#Prepare to write analysis to election_analysis.csv in the Analysis folder
output_path = os.path.join("Analysis", "election_analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Candidate", "Percentage Vote Won", "Number of Votes", "Total Number of Votes", "Winner"])
    for myCandidate in candidate_list:
        #calculate the percentage of the total vote the candidate won
        percent_vote = 100*candidate_list[myCandidate]/myTotalNum_votes
        formatted_percent_vote = "{:.3f}".format(percent_vote)
        #print candidate results to terminal
        print(f"{myCandidate}: {formatted_percent_vote}% ({candidate_list[myCandidate]})")
        #write candidate results to csv file
        csvwriter.writerow([myCandidate, formatted_percent_vote, candidate_list[myCandidate], myTotalNum_votes, Election_winner])

        

print("-----------------------")
print(f"Election Winner: {Election_winner}")
print("-----------------------")


            



