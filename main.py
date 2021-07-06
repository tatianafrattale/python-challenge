# Challenge 1- PyBank

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Import os and csv
import os
import csv
 
# Set path for csv
pybankcsv = os.path.join("Resources", "pybank_budget_data.csv")

# Create variables and lists
total_months = []
net_profit_loss = []

# Variable counts
month_count = 0
total_profit = 0


# Open csv
with open(pybankcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

for row in csv_reader:
    # Count months
    month_count = month_count + 1

    # Add to total to months list
    total_months.append(row[0])

    # Net total amount of Profit and losses over entire period
    total_profit = total_profit + int(row[1])

    # Add total profit to net profit loss list
    net_profit_loss.append(row[1])


    # Calculate average of changes in profit and losses over entire period. I need to take the total profit/loss and divide it by the amount of months
    average_change_profit = total_profit / month_count



    # The greatest increase in profits over the entire period

    # The greatest decrease in losses over the entire period
