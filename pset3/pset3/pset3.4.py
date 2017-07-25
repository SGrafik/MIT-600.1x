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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secretWord))

    lettersGuessed = []
    guesses = 8
    availableLetters = getAvailableLetters(lettersGuessed)

    while True:
        print("-" * 11)
        print("You have %d guesses left." % guesses)
        print("Available letters: %s" % availableLetters)

        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord, lettersGuessed))

        elif guess in secretWord:
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            print("Good guess: %s" % getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)
            guesses -= 1
            print("Oops! That letter is not in my word: %s" % getGuessedWord(secretWord, lettersGuessed))


        if isWordGuessed(secretWord, lettersGuessed):
            print("-" * 11)
            return print("Congratulations, you won!")

        elif guesses == 0:
            print("-" * 11)
            return print("Sorry, you ran out of guess. The word was %s." % secretWord)
