import os 
import csv
filepath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Initialize variables to store the results
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
dates = []

# Read data from the CSV file
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        date = row['Date']
        profit = int(row['Profit/Losses'])
        
        # Calculate the total number of months and net total profit/loss
        total_months += 1
        net_total += profit

        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            profit_change = profit - previous_profit
            profit_changes.append(profit_change)
            dates.append(date)
        
        previous_profit = profit

# Calculate the average change in profit/loss
average_change = round(sum(profit_changes) / (total_months - 1), 2)

# Find the greatest increase and decrease in profits
max_increase = max(profit_changes)
max_decrease = min(profit_changes)

# Find the corresponding dates for the greatest increase and decrease
max_increase_date = dates[profit_changes.index(max_increase)]
max_decrease_date = dates[profit_changes.index(max_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Save the results to a text file
filepath = os.path.join('PyBank', 'analysis', 'PybankResults.txt')
with open(filepath, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")