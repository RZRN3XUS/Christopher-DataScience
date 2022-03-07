import pandas as pd
import os
os.system('cls')
#Create Pandas DataFrame
data = {'name': ['Jim', 'Peter'], 'age':['30', '20']}
df = pd.DataFrame(data)
print(df)

listBig = [['Peter', 20], ['Sherry', 12], ['Chris', 40]]
df1 = pd.DataFrame(listBig, columns = ['name', 'age'])

print(df1)

#ins = pd.read_csv('insurance_data.csv')

#df3 = ins[(ins['age']>20) & (ins['smoker'] == 'yes') & (ins['sex'] == 'female')]

df = pd.DataFrame([
    ['Amy', 'Assignent 1', 75],
    ['Amy', 'Assignment 2', 35],
    ['Amy', 'Assignent 3', 80],
    ['Amy', 'Assignment 4', 55],
    ['Bob', 'Assignment 1', 99],
    ['Bob', 'Assignment 2', 35],
    ['Bob', 'Assignment 3', 50],
    ['Bob', 'Assignment 4', 70]
], columns = ['Name', 'Assignment', 'Grade'])

print(df.groupby('Name').Grade.mean())
print(df.groupby('Name').Grade.std())
print(df.groupby('Name').Grade.median())
print(df.groupby('Name').Grade.count())