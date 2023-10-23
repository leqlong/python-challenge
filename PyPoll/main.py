import os 
import csv
filepath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Initialize variables to store the results
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read data from the CSV file
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        candidate = row['Candidate']
        
        # Count the total number of votes
        total_votes += 1

        # If the candidate is not in the dictionary, add them
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)

# Find the winner based on popular vote
for candidate, (votes, percentage) in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print the results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate, (votes, percentage) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Save the results to a text file
filepath = os.path.join('PyPoll', 'analysis', 'PypollResults.txt')
with open(filepath, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------------------\n")
    for candidate, (votes, percentage) in candidates.items():
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")