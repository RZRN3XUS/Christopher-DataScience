#Christopher Dycus
#1/20/2022
import os
os.system('cls')
#Learning about lists, tuples, dictionaries

fruits = ['apples', 'oranges', 1, 7, 'banana']
print(len(fruits))
for elem in fruits:
    print(type(elem))
mylist = list((3,5,6))
print(mylist)

fruits.append('kiwi')
fruits.insert(3, 'grapes')

fruits.append(mylist)
print(fruits)