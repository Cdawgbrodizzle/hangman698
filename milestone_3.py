import random
word_list = ["apple", "orange", "mango", "pear", "melon"]
hangman_word = random.choice(word_list)
print(hangman_word)

def guesser():
        while True:
            guess = input("Guess a letter: ")
            if len(guess) > 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            else:
                break
        return guess
guessed = guesser()
def verify_guess(guessed):
    if guessed.lower() in hangman_word:
        print("The letter is in the word")
        return guessed
    else:
        print("Sorry, {guessing} is hard isn't it? Try again.")
    return verify_guess
vg = verify_guess(guessed)

print(vg)