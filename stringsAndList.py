#Christopher Dycus
#1/13/22
#Strings and Lists
import os, sys, random
os.system('cls')
num1=8
num2=4.5
char='t'
flag=False
StringVar1 = 'Hello'
StringVar2 = "Goodbye"
#concatanation adding 2 strings
print(StringVar1 + " " + StringVar2)
print(StringVar1 + " " + str(num1) + StringVar2)

print(type(num2))
print(StringVar1[3:0])
print(StringVar1)
print("Hello \t Peter \n I am here\\or not \"Goodbye\" ")

for letter in StringVar1:
    print(letter, end = ' ')
print()
for i in range(8):
    print(i, end = " ")
for i in range(10, 20):
    print(i, end = "\n")

#getting user input
marioSize = input('What size would you like the tower? ')
print()
while (true):
    for row in range(int(marioSize)):
        for space in range(int(marioSize) - row - 1, 0, -1):
            print(" ", end="")
        for i in range(row + 1):
            print("#", end ="")
        print("  ", end = "")
        for i in range(row + 1):
            print("#", end ="")
        print("\n", end ="")