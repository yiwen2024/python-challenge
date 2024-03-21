#Dependencies 
import os
import csv

#Define the path of csv file and text file
CURRENT_DIR = os.path.dirname(__file__)

file_to_load = os.path.join(CURRENT_DIR, "Resources", "budget_data.csv")
file_to_output = os.path.join(CURRENT_DIR, "analysis","budget_analysis.txt")

#Declare variables
total_month = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]
total_revenue = 0
revenue_change = 0
previous_revenue = 0
total_change = 0

#Read csv file and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader =csv.DictReader(revenue_data, delimiter=",")

#Set i to exclude the revenue of first month in the calculation of month of change
    i = 1
#Track the revenue change
    for row in reader:

        total_month = total_month + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        if i > 1:
            revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        i = i + 1

        total_change = total_change + revenue_change

#Calculate the greatest increase and decrease
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

#Calculate the average revenue change
avg_change = total_change / (total_month-1)

#Output results
output = (f"\nFinancial Analyst\n"
f"-------------------------------\n"
f"Total Months: {total_month}\n"
f"Total Revenue: ${total_revenue}\n"
f"Average Change: ${avg_change}\n"
f"Greates Increase in Revenue: {greatest_increase[0]}, (${greatest_increase[1]})\n"
f"Greates Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Print results on terminal
print(output)

#Write results in text file in the folder of analysis
with open (file_to_output, "w") as txt_file:
    txt_file.write(output)
