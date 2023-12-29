# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This README is to describe the properties of the code and the process by which the Hangman game was developed.

## Table of Contents:

1. Outline
2. Installation
3. Usage Instructions
4. File Structure

## Outline
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. It does this through the use of a class that contains the main functionality of the game, which is then passed through a function outside of the class, which contains the win/lose parameters of the game.

The aim of this project was to demonstrate my capability in the use of object oriented programming and a wider set of essential python tools to create usable code. In the process of this project, I was able to refine a number of concepts that I have made use in smaller tasks. It taught me the value of these concepts when they work in concert and have given me insight into how I might bring this skills together in future projects.

## Installation

This project is built to run with minimal inputs from the user and should be able to run through Visual Studio, or any other tool package that can run python. Download the code from its repository and open the python file milestone_5.py on doing so, simply run the program and it should play until completion.

## Usage Instructions

As said above, there is little installation to be done. Upon opening the milestone_5.py file you press play in visual studio, or run the program from the terminal and you will be presented with the blanks of the word you are being asked to find and will be asked to input a letter.

If you enter a letter it will tell you whether or not the letter is in the word. If it is in the word, the blank corresponding to the position of the letter will be filled in and you will be asked to enter another letter, this will continue until you have filled in all letters, at which point, a message wil appear saying that you have won the game.

If you enter an incorrect letter, then you will lose a life, if you lose all your lives, the game will end with the message "You lose." at which point the game will end and you can start again if you choose. There is a counter that will inform you of how many remaining chances you have.

If you enter a key that is not an alphabetic letter, you will be asked to submit an alphabetic letter and will do so until you comply with this.

If you enter a letter that has already been guessed, you will be informed of this and be asked to guess a new letter.

## File Structure

This project was created incrementally and the various stages of development are reflected in the milestone folders. All but milestone_5.py are incomplete versions of the game that reflect the process of development.

As said above, milestone_5.py is the complete version and the only file that should be played. For those curious the other folders represent the various design stages.

milestone_4.py representeds the core functionality of the game, where the class has been designed to take in inputs and verify the guesses, but will not play a complete game, which would require the seperate function that appears in milestone_5.py

milestone_3.py demonstrates the earlier core functionality of the class being made. At this time there was not a class, but the two functions that would make up the body of the class. It is missing some of the wider functions, as it was not yet developed to play a full game and only pass through a letter and check it against the secret word.

milestone_2.py was the earliest function from which the game was built out from. At this time it was just the proto code for the ask_for_input function of later designs, it did not make use of an isalpha. check but rather scrolled the range of the alphabet which was later changed due to the simplicity and wider range of an isalpha. check.

The earliest file has not been included as this was simply a word list file that was rolled into milestone_2.py and never added as a standalone demonstration.

dump_code.py was a file that was used for any expermentation throughout the project which does not describe any particular stage and was used to pilot certain code without causing too much deviation from the original, or hold code while other parts where being modified.

There is also a template file that explains some of the principles of how to build a hangman project.

