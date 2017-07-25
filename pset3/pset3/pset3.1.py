def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letter_count = 0

    for i in secretWord:
        if i in lettersGuessed:
            letter_count += 1

    if letter_count == len(secretWord):
        return True
    else:
        return False
