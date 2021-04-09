import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#open csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip header
    csv_header = next(csvreader)

#get row count for total months
    row_count = sum(1 for row in csvreader)

#print output header and total months
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months : {row_count}")

#reopen csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip header
    csv_header = next(csvreader)

#Define profit variables
    sum_profit = 0
    sum_loss = 0
    totalPL = 0
    profit = 0

#for data in csv, if greater than zero than add to profit, if less than zero add to loss
#total is profits plus losses

    for row in csvreader:
        profit = float(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss + profit
    totalPL = sum_profit + sum_loss
    totalPL = round(totalPL)
    print(f"Total: ${totalPL}")
    print(sum_profit)
    #print(sum_loss)
                

#reopen file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#skip header
    csv_header = next(csvreader)

#scan rows and find min and max values in row 1 - profits/losses
    rows = list(csvreader) 
    max_revenue= max(rows, key=lambda row: int(row[1]))
    min_revenue= min(rows, key=lambda row: int(row[1]))

#print min and max, both profit/loss as well as month and year

    print(f'Greatest Increase in Profits: {max_revenue}')
    print(f'Greatest Decrease in Profits: {min_revenue}')


# Specify the file to write to
budget_output = os.path.join("..", "Analysis", "Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(budget_output, 'w') as x_file:
    x_file.write("Financial Analysis\n"),
    x_file.write("--------------------------------------\n"),
    x_file.write(f'Total Months: {row_count}\n'),
    x_file.write(f'Total: ${totalPL}\n'),
    x_file.write(f'Average Change: \n'),
    x_file.write(f'Greatest Increase in Profits: {max_revenue}\n'),
    x_file.write(f'Greatest Decrease in Profits: {min_revenue}\n'),
    