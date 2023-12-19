import random

word_list = ["Apple", "Orange", "Mango", "Pear", "Melon"]
r_list = random.choice(word_list)
ch = input()
if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print("The Given Character ", ch, "is an Alphabet") 
else:
    print("Oops! that is not a valid input.")