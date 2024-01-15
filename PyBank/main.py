import os
import csv

# Path to collect budget data from the Resources folder

budget_csv = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')

# path to output the results to a text file
output_file = os.path.join('python-challenge','PyBank','analysis','PyBank_Output.txt')

# lists to collect and calculate data
months = []
profits_losses = []
profit_change = []

# Read the csv file
with open(budget_csv, 'r') as budgetfile:

    # Split the data on commas
    csvreader = csv.reader(budgetfile, delimiter = ',')

    # Read the header from the 1st roe
    header = next(csvreader)

    # for each row in the csv after header populate months and profits_losses
    for row in csvreader:

        months.append(row[0])
        
        profits_losses.append(int(row[1]))


    # for each row in profits_losses, calculate profit_change
    for i in range(1, len(profits_losses)):
        
        profit_change.append(
            int(profits_losses[i]) - int(profits_losses[i-1])
        )
    
    # Total Months
    total_months = len(months)

    # Total Profit and Losess
    total = sum(profits_losses)

    # Average Change
    average = round((sum(profit_change)) / (len(profit_change)),2)

    # Greatest Increase in Profits
    greatest_increase = max(profit_change)
    greatest_increase_index = profit_change.index(greatest_increase)
    greatest_increase_month = months[greatest_increase_index+1]

    # Greatest Decrease in Profits
    greatest_decrease = min(profit_change)
    greatest_decrease_index = profit_change.index(greatest_decrease)
    greatest_decrease_month = months[greatest_decrease_index+1]

    # output the results to the terminal                                  
    print("Financial Analysis")

    print("----------------------------")

    print(f'Total Months: {total_months}')
    
    print(f'Total: ${total}')
    
    print(f'Average Change: ${average}')

    print(f'Greatest Increase in Profits: {str(greatest_increase_month)} (${greatest_increase})')

    print(f'Greatest Decrease in Profits: {str(greatest_decrease_month)} (${greatest_decrease})')

    # open the output file and write the financial analysis results
    with open(output_file, "w", newline='') as textfile:

        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------\n")

        textfile.write(f'Total Months: {total_months}\n')
        
        textfile.write(f'Total: ${total}\n')
        
        textfile.write(f'Average Change: ${average}\n')

        textfile.write(f'Greatest Increase in Profits: {str(greatest_increase_month)} (${greatest_increase})\n')

        textfile.write(f'Greatest Decrease in Profits: {str(greatest_decrease_month)} (${greatest_decrease})\n')