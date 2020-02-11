import os
import csv

with open("election_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    khan = 0
    correy = 0
    li = 0
    otooley = 0

    votes_list = list(csvfile)
    votes = len(votes_list)
    print("Votes Cast:", votes - 1)
    

    for row in csvreader:
        if "Khan" == row[2]:
            khan = khan + 1
        elif "Correy" == row[2]:
            correy = correy + 1
        elif "Li" == row[2]:
            li = li + 1
        elif "O'Tooley" == row[2]:
            otooley = otooley + 1   
    
    print(khan)
    print(correy)
    print(li)
    print(otooley)


    khan_percent = ((khan/votes)*100)
    correy_percent= ((correy/votes)*100)
    li_percent = ((li/votes)*100)
    otooley_percent = ((otooley/votes)*100)

    print("Khan:" + str(khan) + " " + str(khan_percent).format(khan_percent)+"%")
    print("Correy:" + str(correy) + " " + str(correy_percent).format(correy_percent)+"%")
    print("Li:" + str(li) + " " + str(li_percent).format(li_percent)+"%")
    print("O'Tooley:" + str(otooley) + " " + str(otooley_percent).format(otooley_percent)+"%")

    if khan > correy & li & otooley:
        print("Winner: Khan")
    if correy > khan & li & otooley:
        print("Winner: Correy")
    if li > correy & khan & otooley:
        print("Winner: Li")
    if otooley > correy & li & otooley:
        print("Winner: O'Tooley")




