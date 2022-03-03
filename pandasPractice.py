import pandas as pd
df2 = pd.DataFrame([
    [1, 'San Diego', 100],
    [2, 'Los Angeles', 120],
    [3, 'San Francisco', 90],
    [4, 'Sacramento', 115]
],
    columns = ['Store ID', 'Location', 'Store #'])

print(df2)

df3 = pd.DataFrame([
    [1, 'T-Shirt', 'blue'],
    [2, 'T-Shirt', 'green'],
    [3, 'Skirt', 'red'],
    [4, 'Skirt', 'black']
],
    columns = ['Product ID', 'Product Name', 'Color'])

print(df3)

