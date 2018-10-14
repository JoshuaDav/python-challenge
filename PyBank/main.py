import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

months = 0
profitloss = 0
maxchange = ["", 0]
minchange = ["", 1000000000000]
monthchange = []
changelist = []


with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    first_row = next(reader)
    months = months + 1
    profitloss = profitloss + int(first_row[1])
    prevchange = int(first_row[1])

    for row in reader:
        months = months + 1
        profitloss = profitloss + int(row[1])
        net_change = int(row[1]) - prevchange
        prevchange = int(row[1])
        changelist = changelist + [net_change]
        monthchange = monthchange + [row[0]]

        if net_change > maxchange[1]:
            maxchange[0] = row[0]
            maxchange[1] = net_change

        if net_change < minchange[1]:
            minchange[0] = row[0]
            minchange[1] = net_change

average = sum(changelist) / len(changelist)

print("Financial Review")
print(f"Total Months: {months}")
print(f"Total: {profitloss}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {maxchange}")
print(f"Greatest Decrease in Profits: {minchange}")


new_file = open("PyBank.txt","w")
new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write(f"Total Months: {months} \n")
new_file.write(f"Total: {profitloss} \n")
new_file.write(f"Average Change: {average} \n")
new_file.write(f"Greatest Increase in Profits: {maxchange} \n")
new_file.write(f"Greatest Decrease in Profits: {minchange} \n")