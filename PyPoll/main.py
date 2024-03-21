#Dependencies 
import os
import csv


# Define the path of file to load (csv) and file to upload (txt)
CURRENT_DIR= os.path.dirname(__file__)

file_to_load = os.path.join(CURRENT_DIR, "Resources", "election_data.csv")
file_to_output = os.path.join(CURRENT_DIR,"analysis","election_analysis.txt")

#Create dictionary for candidate name, and vote count
candidates = []
count_votes = []
percent_votes = []
winner_list = []
election_csv = {}


#Define variable
total_votes = 0

#Read csv file and convert it into a list of dictionaries
with open(file_to_load, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #Skip the header line
    next(csvread, )

    #create dictionary from csv file using candidate name as keys
    #count votes for each candidate
    #total votes counted by number of rows for each loop (skip the header)
    
    for row in csvread:
        #Add to the total vote count
        total_votes = total_votes + 1
        if row[2] in election_csv.keys():
            election_csv[row[2]] = election_csv[row[2]] + 1
        else:
            election_csv[row[2]] = 1


#Add keys and values of the dictionary into the lists

for key, value in election_csv.items():
    candidates.append(key)
    count_votes.append(value)

#calculate vote percentage

for n in count_votes:
    percent_votes.append(round(n/total_votes * 100, 3))

#zip candidates, vote percentage, vote counts into tuples
Combine_data = list(zip(candidates, percent_votes, count_votes))

#create a list of winners and extract the name of winner
max_votes = max(count_votes)
for candidate_name in Combine_data:
    if candidate_name[2] == max_votes:
        winner_list.append(candidate_name[0])

#Write results to text file
with open(file_to_output, 'w') as txt_file:
     
    txt_file.writelines("Election Results \n------------------------- \nTotal Votes: " + str(total_votes) +
      "\n-------------------------\n")
    
    for item in Combine_data:
     txt_file.writelines(str(item[0]) + ": " + str(item[1]) +"%  (" + str(item[2]) + ")\n")  

#Define winner
    winner = ", ".join(winner_list)    
    txt_file.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#Read the result and print it on terminal
with open(file_to_output, 'r') as read_file:
    print(read_file.read())
