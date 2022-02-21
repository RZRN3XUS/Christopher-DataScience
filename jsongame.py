import os, random, requests, json
os.system('cls')
word=""
guess=""
def selectWord(length):
    global word
    webster = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")
    dictionary = webster.json()
    fruits = list(dictionary.keys())
    word = random.choice(fruits)
    while(len(word) != length):
        word = random.choice(fruits)

def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")
           
gameOn=True
tries=0
letterGuessed=""
print('Select difficulty - 5, 7, 9')
selectWord()
while gameOn:
   
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries > 10:
        print("\n Sorry run out chances ")
        #playGame() ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed! ")