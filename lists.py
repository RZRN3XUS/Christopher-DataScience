#Christopher Dycus
#1/23/2022
#List Practice
import os
os.system('cls')

list1 = [15, 100, 154, 20, 253, 530, 203]
for i in range(0, len(list1)):
    if (list1[i] == 20):
        list1[i] = 200
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
newlist = []
for i in range(0, len(list1)):
    if (list1[i] != 20):
        newlist.append(list1[i])
print(newlist)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
newlist = []
for i in range(0, len(list1)):
    if (list1[i] != ""):
        newlist.append(list1[i])
print(newlist)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h", "i", "j"])
print(list1)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(0, len(list1)):
    print(str(list1[i]) + ' ' + str(list2[3-i]))

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
for i in range(0, len(list1)):
    print(str(list1[i]) + str(list2[i]), end = ' ')
print()

list1 = [1, 2, 3, 4, 5, 6, 7]
for i in range(0, len(list1)):
    print(list1[i] ** 2, end = ' ')
print()

phrase = "The best class in Greenhill is Data Science"
tempstring = ""
words = []
for i in range(0, len(phrase)):
    if (phrase[i] != " "):
        tempstring += phrase[i]
    else:
        words.append(tempstring)
        tempstring = ""
words.append(tempstring)
print(words)
