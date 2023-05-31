import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

#Create txt file to export results once code is run
text_file = "budget_results.txt"

#Variables to be used 
total_number_of_months = 0
total_profits = 0
previous_profits = 0
profits_change = 0
profits_change_list = []
average_profits = 0
greatest_decrease = ["", 99999999]
greatest_increase = ["", 0]



with open(budget_data) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:

        #Count the total number of months
        total_number_of_months += 1

        #Calculate the total Profits/Losses by addidng each row in the time period
        total_profits = total_profits + int(row["Profit/Losses"])

        #Calculate the change in Profits from month to month over the time period
        #If statement is made to caclculate the average profits without including the first month "change", it is set to 0
        if len(profits_change_list) == 0:
            previous_profits = float(row["Profit/Losses"])
            profits_change_list = profits_change_list + [profits_change]
        else:
            profits_change = float(row["Profit/Losses"])-previous_profits
            previous_profits = float(row["Profit/Losses"])
            profits_change_list = profits_change_list + [profits_change]
       
        #The greatest increase in profits and include date and amount, loop through entire time period
        if profits_change>greatest_increase[1]:
            greatest_increase[1]= profits_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in profits and include date and amount, loop through entire time period
        if profits_change<greatest_decrease[1]:
            greatest_decrease[1]= profits_change
            greatest_decrease[0] = row['Date']
    
    #calculate the average profits for the entire time period
    average_profits= sum(profits_change_list)/(len(profits_change_list)-1)

#Anylyze results and export to budget_results to text file 
with open(text_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------------\n")
    file.write("Total Months: %d\n" % total_number_of_months)
    file.write("Total: $%d\n" %total_profits)
    file.write("Average Change $%.2f\n" % average_profits)
    file.write("Greatest Increase in Profits: %s ($%d)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%d)\n" % (greatest_decrease[0], greatest_decrease[1]))