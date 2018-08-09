import random

WORDLIST_FILENAME = "words.txt"
guessLeft=8
global Word
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
availableLetters= 'abcdefghijklmnopqrstuvwxyz'
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isGuessed = False
    for var in secretWord:
        if var in lettersGuessed:
            isGuessed = True
        else:
            isGuessed = False
            break
    return isGuessed

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Word =''
    isGuessed = isWordGuessed(secretWord, lettersGuessed)
    if isGuessed == False :
        for ch in secretWord:
            if ch in lettersGuessed:
                Word= Word + ' ' + ch
            else:
                Word= Word +' _ '
    else:
        Word = secretWord
    return Word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    global availableLetters
    
    for chr in lettersGuessed:
        #if chr in availableLetters:
        availableLetters = availableLetters.replace(str(chr),'')
    return availableLetters
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    global guessLeft,Word
    
    print('--------------------------------------------')
    print('You have ' + str(guessLeft) + ' guesses left')
    print('Available Letters = ' + str(getAvailableLetters(lettersGuessed)))
    letter =input('Please guess a letter:')
    if letter in secretWord:
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:" + str(getGuessedWord(secretWord, lettersGuessed)))
            
        else:
            lettersGuessed.append(letter)
            Word=str(getGuessedWord(secretWord, lettersGuessed))
            print('Good Guess: ' + Word)
    else:
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter:" + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed.append(letter)
            guessLeft= guessLeft-1
            print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            Word=str(getGuessedWord(secretWord, lettersGuessed))
    return Word
lettersGuessed=[]    

wordlist = loadWords()
secretWord=chooseWord(wordlist)
print('Welcome to the game, Hangman!')
#print(secretWord)
print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
   
while  guessLeft !=0 :
   
    Word1=hangman(secretWord)
    
    if Word1.find(' _ ') == -1:
        print('---------------------------------------')
        print('Congratulations: You won')
        break

if Word1 != secretWord :
    print('Sorry, you ran out of guesses. The word was ' + secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
