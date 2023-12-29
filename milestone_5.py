import random

class Hangman:

    def __init__(self,  word_list, num_lives):
        self.hangman_word = random.choice(word_list)
        self.word_guessed = "_" * len(self.hangman_word)
        self.num_letters = len(self.hangman_word)
        self.word_list = ["apple"]
        #self.word_list = ["apple", "orange", "mango", "pear", "melon"]
        self.list_of_guesses = []
        self.num_lives = num_lives
        print(self.hangman_word)

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) > 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                continue
            else:
                self.list_of_guesses.append(guess.lower())
                print(f"Guessed letters {self.list_of_guesses} ")
                break
        self.check_guess(guess)
     #self.num_letters, self.num_lives
    guessed = ask_for_input
       
    def check_guess(self, guessed): #num_letters, num_lives
        # word_guessed = self.word_guessed
        if guessed.lower() in self.hangman_word:
            print("The letter is in the word")
            for i in range(len(self.hangman_word)):
                    if self.hangman_word[i] in guessed:
                        self.word_guessed = self.word_guessed[:i] + self.hangman_word[i] + self.word_guessed[i+1:]
                        self.num_letters = self.num_letters - 1
            print(self.word_guessed, end=' ')
            print(f"There is {self.num_letters} to go")
               
        else:
                        self.num_lives = self.num_lives - 1
                        print(f"You have {self.num_lives} lives left.")
                        print(self.num_lives)
                       # return num_lives

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print("You Lost")
            break
        elif game.num_lives >= 0 and game.num_letters >= 1:
            game.ask_for_input()
            continue
        else:
            print("congratulations, you won the game!")
            break  

if __name__ == '__main__':
    play_game(word_list=["apple"])
    print("Game is finished")