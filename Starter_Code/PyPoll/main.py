import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Create txt file to export results once code is run
file_to_output = "elections_results.txt"

#Variables to be used
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""

with open(election_data) as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    
    for row in csvreader:

        # Calculate the total vote count for entire data
        total_votes += 1

        candidate = row["Candidate"]
        # After the candidates name appears for the first time in loop, add to new list of unique candidate
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        #Once unique candidate list is made the vote count will be added for that candidate
        candidate_votes[candidate] = candidate_votes[candidate] + 1


#Export results to election_results txt file
with open(file_to_output, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-----------------------------------------\n")
    txt_file.write("Total votes: %d\n" % total_votes)
    txt_file.write("-----------------------------------------\n")
    
   #comparing the winning candidate based on total number of votes amongst leading candidates, incldung percentage calculation
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes-1})\n"
        txt_file.write(voter_output)

    #Export winner result to txt file    
    winning_summary = (f"Winner: {winner}")
    txt_file.write("-----------------------------------------\n")
    txt_file.write(winning_summary)
