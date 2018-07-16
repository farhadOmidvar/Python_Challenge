# PyPoll
# Import Dependencies
import os
import csv

# Open CSV file to read and a text file to write
csv_path = os.path.join('Resources','election_data.csv')
with open(csv_path, 'r') as csv_file,\
	open('Eletion_Results.txt', 'w') as text_file:
	
	# Read CSV file
	election_data = csv.reader(csv_file, delimiter=",")
	
	# Skip header
	election_data_header = next(election_data)

	# Creat empty dictionaries to store datas and set initial counter
	candidates_votes = dict()
	candidates_percentage = dict()
	votes_counter = 0
	
	# Loop through each row of election data  and 
	for row in election_data:
		# count number votes for each candidate and store them in a dictionary
		if row[2] not in candidates_votes:
			candidates_votes[row[2]] = 1
		else:
			candidates_votes[row[2]] +=1
		# count the total number of votes cast
		votes_counter += 1

	# Find number of votes for winner candidate
	winner = max(candidates_votes.values())

	# A complete list of candidates who received votes
	candidates_list = list(candidates_votes.keys())

	# Converting "candidates:number of votes" dictionary to a list of tuples
	list_candidates_votes = list(candidates_votes.items())

	# Loop through each candidates(key), votes(value) in list of tuples
	for candidates, votes in list_candidates_votes:
		# calculate the percentage of votes each candidate won and store it a dictionary
		votes_percentage = "{0:.3f}".format((votes/votes_counter)*100)
		candidates_percentage[candidates] = votes_percentage
		# Find the winner of the election based on popular vote
		if votes == winner:
			popular_candidates = candidates

	# Creating election results
	election_results = f"""
	Election Results
	----------------------
	Total Votes = {votes_counter}
	----------------------
	{candidates_list[0]}: {candidates_percentage[candidates_list[0]]}% ({candidates_votes[candidates_list[0]]})
	{candidates_list[1]}: {candidates_percentage[candidates_list[1]]}% ({candidates_votes[candidates_list[1]]})
	{candidates_list[2]}: {candidates_percentage[candidates_list[2]]}% ({candidates_votes[candidates_list[2]]})
	{candidates_list[3]}: {candidates_percentage[candidates_list[3]]}% ({candidates_votes[candidates_list[3]]})
	----------------------
	Winner: {popular_candidates}
	----------------------
	"""
	# Write the election results as a text file
	text_file.write(election_results)

	# Print the election results to the terminal
	print(election_results)

	

	

