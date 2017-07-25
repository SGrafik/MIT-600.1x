def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in lettersGuessed ).lower()
