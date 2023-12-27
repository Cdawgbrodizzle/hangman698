import random
word_list = ["apple", "orange", "mango", "pear", "melon"]

hangman_word = random.choice(word_list)
list_of_guesses = []
correct_letters = [str(hangman_word)]
print(hangman_word)

class Hangman:
    def __init__(self, num_lives, word_list, num_letters):
        self.hangman_word = random.choice(word_list)
        self.word_guessed = "_" * len(hangman_word)
        self.num_letters = len(hangman_word)
        self.word_list = ["apple", "orange", "mango", "pear", "melon"]
        self.list_of_guesses = []

        def ask_for_input(self):
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
                self.verify_guess()
                return guess
        guessed = ask_for_input(self)
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

        def play_game(word_list):
            num_lives = 5
            while True:
                if num_lives == 0:
                    print("You Lost")
                    break
                elif num_lives >= 0 and num_letters >= 0:
                    ask_for_input()
                    continue
                else: 
                    print("congratulations, you won the game!")

        play_game(word_list=["apple", "orange", "mango", "pear", "melon"])
            
game = Hangman(num_lives=5, word_list=["apple", "orange", "mango", "pear", "melon"], num_letters = len(hangman_word))

print(game)