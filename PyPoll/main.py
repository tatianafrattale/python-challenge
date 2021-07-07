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
pypollcsv = os.path.join("Resources", "election_data.csv")

# Variable counters
total_votes = 0
total_khan = 0
total_correy = 0
total_li = 0
total_otooley = 0

# Open csv
with open(pypollcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
