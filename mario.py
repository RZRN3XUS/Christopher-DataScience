#Mario
check = False
#Get size
while (not check):
    #Get size
    marioSize = input("What size would you like? ")
    if int(marioSize) <= 25 and int(marioSize) >= 1:
        for row in range(int(marioSize)):
            for space in range(int(marioSize) - row - 1, 0, -1):
                print(" ", end="")
            for i in range(row + 1):
                print("#", end ="")
            print("  ", end = "")
            for i in range(row + 1):
                print("#", end ="")
            print("\n", end ="")
    elif int(marioSize) == -1:
        check = True
    else:
        print("Invalid size")
print("bruh")