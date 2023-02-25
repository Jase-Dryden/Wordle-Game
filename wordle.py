import random
# Constant variables
RED = "\u001b[31m"
YELLOW = "\u001b[33m"
GREEN = "\u001b[32m"
WHITE = "\u001b[97m"


def Main():
    word = SelectWord()
    run = True
    turn = 0
    while run:
        guess = PlayerGuess()
        if guess == word:
            run = False
        CompareWords(word, guess)
        for i in  guess:
            print(i, end="")
        print()
        if turn == 5:
            run = False
            print(f"{WHITE} The answer was {''.join(word)}")    
        turn += 1   

def SelectWord():
    """
    Selects a word form WordList.CSV and returns it
    as a list of character.
    """
    with open("WordList.csv", "r") as file:
        lines = file.readlines()
        word =  list(lines[random.randint(0,5757)])
        word.remove("\n")
        return word
    
def PlayerGuess():
    """
    Asks a the player for a five letter word. It
    retures that word as a list of characters.
    """
    guess = input(f"{WHITE} Guess a 5 Letter word?\n")
    return list(guess)

def CompareWords(word: list, guess: list):
    """
    Takes the player's guess interates through it and
    compares to the lettes in the word. If the letter
    is in the word but in the wong location it will turn 
    that letter Yellow. If the letter is in the word and 
    in the right location the letter will be green.
    If the letter is not in the word, the letter will be red
    """
    for i in range(len(guess)):
        if guess[i] in word:
            if guess[i] == word[i]:
                guess[i] = f"{GREEN} {guess[i]}"
            else:
                guess[i] = f"{YELLOW} {guess[i]}"
        else:
            guess[i] = f"{RED} {guess[i]}"

Main()