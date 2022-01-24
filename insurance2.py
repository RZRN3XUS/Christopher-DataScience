#Christopher Dycus
#1/24/22
#Prepare dataset using CSV values
#Change female/male and smoker/nonsmoker to 0 and 1

import csv
import os
import math
os.system('cls')
file = open('insurance_data.csv')

insuranceFile = csv.reader(file)
header = next(insuranceFile)
print(header)
insuranceData = []
for row in insuranceFile:
    insuranceData.append(row)
#change female to 0
#change male to 1
for i in range(len(insuranceData)):
    if insuranceData[i][1] == "female":
        insuranceData[i][1] = 0
    else:
        insuranceData[i][1] = 1
#change smoker to 1
#change nonsmoker to 0
for i in range(len(insuranceData)):
    if insuranceData[i][1] == "yes":
        insuranceData[i][4] = 1
    else:
        insuranceData[i][4] = 0
#add cost to list
for row in insuranceData:
    cost = int((250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]) + 24000*int(row[4]) - 12500)*100)/100
    row.append(cost)
    print(row)
#create new list with region cost average
nw = []
ne = []
sw = []
se = []
for row in insuranceData:
    if row[5] == "northwest":
        nw.append(row[7])
    elif row[5] == "northeast":
        ne.append(row[7])
    elif row[5] == "southeast":
        se.append(row[7])
    elif row[5] == "southwest":
        sw.append(row[7])
print("Northwest Average Cost = " + str(round(sum(nw)/len(nw), 2)))
print("Northeast Average Cost = " + str(round(sum(ne)/len(ne), 2)))
print("Southwest Average Cost = " + str(round(sum(sw)/len(sw), 2)))
print("Southeast Average Cost = " + str(round(sum(se)/len(se), 2)))
#create list wiht only females and only males
femaleInsurance = []
for row in insuranceData:
    if row[1] == 0:
        femaleInsurance.append[row]
maleInsurance = []
for row in insuranceData:
    if row[1] == 1:
        maleInsurance.append[row]
#create a list with only smokers and non smokers
smokerInsurance = []
for row in insuranceData:
    if row[4] == 1:
        smokerInsurance.append[row]
nonSmokerInsurance = []
for row in insuranceData:
    if row[4] == 0:
        nonSmokerInsurance.append[row]
