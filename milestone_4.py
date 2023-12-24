import random
word_list = ["apple", "orange", "mango", "pear", "melon"]
num_lives = 5
hangman_word = random.choice(word_list)
list_of_guesses = []
correct_letters = [str(hangman_word)]
print(hangman_word)

class Hangman:
    def __init__(self, hangman_word, word_guessed, num_letters, num_lives, word_list, list_of_guesses):
        self.hangman_word = random.choice(word_list)
        self.word_guessed = "_" * len(hangman_word)
        self.num_letters = int(hangman_word)
        self.num_lives = 5
        self.word_list = ["apple", "orange", "mango", "pear", "melon"]
        self.list_of_guesses = []
        print(num_letters)

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
    def check_guess(self, guessed, correct_letters,):
        word_guessed = "_" * len(hangman_word)
        if guessed.lower() in hangman_word:
            print("The letter is in the word")
            for i in range(len(hangman_word)):
                if hangman_word[i] in guessed:
                    word_guessed = word_guessed[:i] + hangman_word[i] + word_guessed[i+1:]
                    return word_guessed
                    print(word_guessed)

        else:
            print("Sorry, {guessing} is hard isn't it? Try again.")
    verify_guess = check_guess(guessed, correct_letters)

    print(verify_guess)