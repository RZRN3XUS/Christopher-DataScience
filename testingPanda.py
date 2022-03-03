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

ins = pd.read_csv('insurance_data.csv')

df3 = ins[(ins['age']>20) & (ins['smoker'] == 'yes') & (ins['sex'] == 'female')]
print(df3)
