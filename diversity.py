#Christopher Dycus
#1/26/2022
#Editing diversity school CSV

import os
import csv
from tokenize import group
os.system('cls')

file = open('diversity_school.csv')

diversityFile = csv.reader(file)

header = next(diversityFile)
states = []

for row in diversityFile:
    if row[2] not in states and row[2] != 'NA':
        states.append(row[2])

groups = []
for state in range(len(states)):
    for row in diversityFile:
         if row[2] == state[states]:
             groups.append(row[3])  
    print(str(states[state]) + ' contains the following minority groups:' + str(groups))