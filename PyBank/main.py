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
month_to_month = []

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
    average_change_profit = (total_profit / month_count)

    # In order to find the greatest increase and decrease in profit, I need to calculate the changes from month to month? Store those values?
    current_month_profit = int(row[1])
    previous_month_profit = int(row[1]) - current_month_profit
    month_to_month = current_month_profit - previous_month_profit
    
    # The greatest increase in profits over the entire period, using max function, 
    greatest_increase = max(month_to_month)

    # The greatest decrease in losses over the entire period, using min function, 
    greatest_decrease = min(month_to_month)

    # Find the date for the greatest increase
    greatest_increase_date = [month_to_month.index(greatest_increase)]

    #Find the date for the greatest decrease
    greatest_decrease_date = [month_to_month.index(greatest_decrease)]

# Create the print statement
print("Financial Analysis")
print("---------------------------------------------")
print("Total Months: " + str(month_count))
print("Total Profit: " + str(total_profit))
print("Average Change: " + "$" + str(average_change_profit)
print("Greatest Increase in Profits: " + str(greatest_increase_date) + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + str(greatest_decrease))

# Open the text file

with open('analysis.txt, 'w') as text:
    text.write("---------------------------------------\n")
    text.write("Financial Analysis" + "\n")
    text.write("Total Months: " + str(month_count) + "\n")
    text.write("Total Profit: " + "$" + str(total_profit) +"\n")
    text.write("Average Change: " + "$" + str(average_change_profit) + "\n")
    text.write("Greatest Increase In Profit: " + str(greatest_increase_date) + "$" + str(greatest_increase) + "\n")
    text.write("Greatest Decrease In Profit: " + str(greatest_decrease_date) + "$" + str(greatest_decrease) + "\n")
