import random

class Hangman:
    ''' 
    An implementation of the classic Hangman game.

    Arguments:
        word_list (list): a list of strings
        num_lives (int): the number of lives
        word (string): a word chosen randomly from word_list
        word_guessed (list): a list of chars
        num_letters (int): unique number of letters in word
        list_of_guesses (list): a list of characters
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['-'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        ''' 
        A function that checks if a guessed letter is in word.

        Arguments:
            guess (char): a character
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in word.')
            print(f'You have {self.num_lives} lives left.')
            print(self.word_guessed)


    def ask_for_input(self):
        ''' 
        Function that asks the player to guess a character.
        '''
        while True:
            guess = input("Guess a letter: ")
            if (len(guess) != 1) or (not guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    ''' 
    Function that initiates a new game.

    Arguments:
        word_list (list): a list of strings
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


word_list = ["apple", "banana", "grapes", "orange", "lemon"]
play_game(word_list)





        


       
