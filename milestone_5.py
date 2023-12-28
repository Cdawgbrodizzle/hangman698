import random
word_list = ["apple", "orange", "mango", "pear", "melon"]

hangman_word = random.choice(word_list)
correct_letters = [str(hangman_word)]
print(hangman_word)
list_of_guesses = []

class Hangman:

    def __init__(self, num_lives, word_list, num_letters):
        self.hangman_word = random.choice(word_list)
        self.word_guessed = "_" * len(hangman_word)
        self.num_letters = len(hangman_word)
        self.word_list = ["apple", "orange", "mango", "pear", "melon"]
        self.list_of_guesses = []

        def ask_for_input():
                while True:
                    guess = input("Guess a letter: ").lower()
                    if len(guess) > 1 or not guess.isalpha():
                        print("Invalid letter. Please, enter a single alphabetical character.")
                        continue
                    elif guess in list_of_guesses:
                        print("You already tried that letter!")
                        continue
                    else:
                        break
                return guess
        guessed = ask_for_input()
        
        def check_guess(guessed, num_letters, num_lives):
            word_guessed = "_" * len(hangman_word)
            if guessed.lower() in hangman_word:
                print("The letter is in the word")
                for i in range(len(hangman_word)):
                    if hangman_word[i] in guessed:
                        word_guessed = word_guessed[:i] + hangman_word[i] + word_guessed[i+1:]
                        num_letters = num_letters - 1
                        return word_guessed, num_letters
            else:
                num_lives = num_lives - 1
                print("Sorry, {guessing} is hard isn't it? Try again.")
                print("You have {num_lives} lives left.")
                return num_lives
        verify_guess = check_guess(guessed, num_letters, num_lives)
        print(verify_guess)


#Hangman(num_lives=5, word_list=["apple", "orange", "mango", "pear", "melon"], num_letters = len(hangman_word))

def play_game(word_list, num_letters):
    num_lives = 5
    game = Hangman(word_list=["apple", "orange", "mango", "pear", "melon"], num_lives = 5, num_letters = len(hangman_word))
    while True:
        if num_lives == 0:
            print("You Lost")
            break
        elif num_lives >= 0 and game.num_letters >= 0:
            game.guessed()
            break
        else: 
            print("congratulations, you won the game!")
            break  
#play_game(word_list, num_letters = len(hangman_word))
if __name__ == '__main__':
    play_game(word_list=["apple", "orange", "mango", "pear", "melon"], num_letters=len(hangman_word))