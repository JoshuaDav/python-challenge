import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = 0
mostvotes = 0
winner = ""
candidates = []
votesperlist = {}

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
    votes += 1
    individual = row[2]
    if individual not in candidates
        candidates.append(individual)
        votesperlist[individual] = 0

    votesperlist[individual] += 1

