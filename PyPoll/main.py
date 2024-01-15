import os
import csv

# Path to collect election data from the Resources folder

election_csv = os.path.join('python-challenge','PyPoll','Resources','election_data.csv')

# path to output the results to a text file
output_file = os.path.join('python-challenge','PyPoll','analysis','PyPoll_Output.txt')

# variables to collect election data

voters = []
candidates = []
candidate_name = ""
candidate_votes = {}
candidates_summary = {}
winner_count = 0
winner = ""

# Read the csv file

with open(election_csv, 'r') as electionfile:

    # Split the data on commas
    csvreader = csv.reader(electionfile, delimiter = ',')

    # Read the header from the 1st row in the csv
    header = next(csvreader)

    # Read all rows the csv
    for row in csvreader:

        voters.append(int(row[0]))

        candidate_name = row[2]

        if(candidate_name not in candidates):
            candidates.append(row[2])
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            

    # Total Votes
    total_votes = len(voters)

    # Candidate 
    for candidate_name in candidate_votes:
        
        percent_votes = round((candidate_votes[candidate_name] / total_votes) * 100, 3)

        candidates_summary[candidate_name] = (candidate_name+ ": " + str(percent_votes) +"% (" + str(candidate_votes[candidate_name]) +")")

        if(winner_count <= candidate_votes[candidate_name]):
            winner_count = candidate_votes[candidate_name]
            winner = candidate_name

    # output the results to the terminal        
    print('Election Results')

    print('-------------------------')

    print(f'Total Votes: {total_votes}')

    print('-------------------------')

    for name in candidates_summary:
        print (candidates_summary[name]) 

    print('-------------------------')

    print(f'Winner: {winner}')

    print('-------------------------')

# open the output file and write the election analysis results
    with open(output_file, "w", newline='') as textfile:

        textfile.write("Election Results\n")
        textfile.write("----------------------------\n")

        textfile.write(f'Total Votes: {total_votes}\n')
        textfile.write("----------------------------\n")

        
        for name in candidates_summary:
            textfile.write(f"{candidates_summary[name]}\n") 
        
        textfile.write("----------------------------\n")

        
        textfile.write(f'Winner: ${winner}\n')
        textfile.write("----------------------------\n")
