import os, random, requests, json
from datetime import datetime
os.system('cls')
word=""
guess=""
def selectWord(length):
    global word
    webster = requests.get("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")
    dictionary = webster.json()
    fruits = list(dictionary.keys())
    check = True
    while(check):
        word = random.choice(fruits)
        if len(word) == length:
            check = False

def selDiff():
    global difficulty
    check=True
    os.system('cls')
    while check:
        try:
            difficulty=input('Select length of word to guess - 5, 7, or 9\n')
            if difficulty == '5' or difficulty == '7' or difficulty == '9':
                check = False
            else:
                print('Invalid Difficulty')
                print(difficulty)
        except ValueError:
            print('Invalid Difficulty')
            print(difficulty)

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
           
username = input('Name?')
gameOn=True
highestScore = 0
gameEnd = False
score = 11
while gameOn:
    selDiff()
    selectWord(int(difficulty))
    tries=0
    match = True
    gameEnd  = False
    letterGuessed=""
    while match:
        guessFunction()
        letterGuessed += guess  #letterGuessed=letterGuessed + guess
        if guess not in word:
            tries +=1
        countLetter=0
        for letter in word:
            if letter in letterGuessed:
                print(letter, end=" ")
                countLetter +=1
            else:
                print("_", end=" ")
        if tries > 10:
            print("\n Sorry run out chances ")
            print('The word was ' + word)
            gameEnd = True
        if countLetter == len(word):
            print("\nyou guessed! ")
            gameEnd = True
        if gameEnd:
            check = True
            if tries < score:
                score = tries
            print('Previous Score: ' + str(tries))
            print('Highest Score: ' + str(score))
            while check:
                playAgain = input('play again? (y/n)')
                if playAgain == 'y' or playAgain == 'n':
                    if playAgain == 'n':
                        gameOn = False
                    check = False
                    match = False
                else:
                    print('invalid input')
jsondump = {'Username: ': [username], 'Date: ': [datetime.today().strftime('%Y-%m-%d')], 'Highest Score: ': [score]}
with open('game.json', 'w') as f:
    json.dump(jsondump, f)