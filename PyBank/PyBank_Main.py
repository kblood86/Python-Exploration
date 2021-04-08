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
    print(sum_loss)

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    rows = list(csvreader) 
    max_revenue_row = max(rows, key=lambda row: int(row[1]))
    in_revenue_row = min(rows, key=lambda row: int(row[1]))

    print(f'Greatest Increase in profit: {max_revenue_row}')
    print(f'Greatest Decrease in profit: {in_revenue_row}')