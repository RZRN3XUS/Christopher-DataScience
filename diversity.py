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
diversityList = []
for row in diversityFile:
    diversityList.append(row)

for row in diversityList:
    if row[2] not in states and row[2] != 'NA':
        states.append(row[2])

#Make a list of all the minority groups per state and add a total number of students
for state in range(len(states)):
    minorities = []
    totalM = 0
    for row in diversityList:
        if states[state] == row[2]:
            if row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'White' and row[3] != 'Unknown' and row[3] != 'Non-Resident Foreign' and row[3] not in minorities:
                minorities.append(row[3])
            if row[3] == 'Total Minority':
                totalM += int(row[4])
    print(str(states[state]) + ' contains a total minority population attending university of', str(totalM) + ' including groups: ', end = '')
    print(minorities)

#Make a list of the number of schools studied per state
for state in range(len(states)):
    schools = []
    for row in diversityList:
        if row[2] == states[state] and row[0] not in schools:
            schools.append(row[0])
    print(str(states[state]) + ' contains ' + str(len(schools)) + ' schools')

#What is the greatest ethnic group per state
for state in range(len(states)):
    groups = []
    groupcounts = []
    for row in diversityList:
        if row[2] == states[state] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] not in groups:
            groups.append(row[3])
            groupcounts.append(0)
    for i in range(len(groups)):
        for row in diversityList:
            if row[2] == states[state] and row[3] == groups[i]:
                groupcounts[i] += int(row[4])
    print(states[state] + '\'s largest ethinicity population enrolled in university is ' + str(groups[groupcounts.index(max(groupcounts))]) + ' at ' + str(max(groupcounts)))

#Add a column for a percentage of race per university
universities = []
for row in diversityList:
    if row[0] not in universities:
        universities.append(row[0])

for school in range(len(universities)):
    population = 0
    for row in diversityList:
        if row[0] == universities[school]:
            population += int(row[4])
    for row in diversityList:
        if row[0] == universities[school] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'Unknown':
            print(universities[school] + ' is ' + str(round(int(row[4])/population, 2) * 100) + '% ' + row[3])
