# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# Import modules
import os
import csv

# Set path for csv 
pypollcsv = os.path.join('Resources', 'election_data.csv')

# Variable counters
total_votes = 0
total_correy= 0
total_khan = 0
total_li = 0
total_otooley = 0

# Open csv and skip header
with open(pypollcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

# Read each row
for row in csv_reader:  
    # Total number of votes, just found out about the += function, what a time saver!!!
    total_votes += 1

    # Total votes per candidate
    if (row[2] == "Correy"):
        total_correy += 1
    elif (row[2] == "Khan"):
        total_khan += 1
    elif (row[2] == "Li"):
        total_li += 1
    elif (row[2] == "O'Tooley"):
        total_otooley += 1

    # Percentage votes per candidate
    correy_percent_vote = total_correy / total_votes
    khan_percent_vote = total_khan / total_votes
    li_percent_vote = total_li / total_votes
    otooley_percent_vote = total_otooley / total_votes

    # Format into percentage
    correy_percentage = "{:.0%}".format(correy_percent_vote)
    khan_percentage = "{:.0%}".format(khan_percent_vote)    
    li_percentage = "{:.0%}".format(li_percent_vote)
    otooley_percentage = "{:.0%}".format(otooley_percent_vote)

    # Winner based on popular vote
    if total_correy > total_khan and total_li and total_otooley:
        winner = "Correy"
    elif total_khan > total_correy and total_li and total_otooley:
        winner = "Khan"
    elif total_li > total_correy and total_khan and total_otooley:
        winner = "Li"
    elif total_otooley > total_correy and total_khan and total_li:
        winner = "O'Tooley"

# Print Statement in integrated terminal
print("Election Results")  
print("--------------------------------------")
print("Total Votes: " + str(total_votes)) 
print("--------------------------------------")
print("Correy: " + correy_percentage + str(total_correy))
print("Khan: " + khan_percentage + str(total_khan))
print("Li: " + li_percentage + str(total_li))
print("O'Tooley: " + otooley_percentage + str(total_otooley))
print("--------------------------------------")
print("Winner: " + winner)

# Open text file to write analysis
with open('analysis.txt, 'w') as text:
    text.write("Election Results" + "\n")
    text.write("---------------------------------------\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    text.write("Correy: " + correy_percentage + str(total_correy) +"\n")
    text.write("Khan: " + khan_percentage + str(total_khan) + "\n")
    text.write("Li: " + li_percentage + str(total_li) + "\n")
    text.write("O'Tooley: " + otooley_percentage + str(total_otooley) + "\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + winner + "\n")
