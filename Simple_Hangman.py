# -*- coding: utf-8 -*-

# Hangman

import random
import nltk
import os
from nltk.corpus import words

nltk.download('words')

clear = lambda: os.system("clear")

word_list = words.words()

hangman_logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

hangman_ascii = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
    _|___
'''

# Handle ascii art as a list
hangman_ascii_list = [c for c in hangman_ascii]

# Create a copy for the game while in progress
hangman_game = hangman_ascii_list.copy()

# Start without all the body members

# remove head
hangman_game[42] = " "
hangman_game[43] = " "
hangman_game[44] = " "

# remove body
hangman_game[59] = " "
hangman_game[75] = " "

# remove hands
hangman_game[58] = " "
hangman_game[60] = " "

# remove feet
hangman_game[89] = " "
hangman_game[91] = " "

def add_head(hangman):
    hangman[42] = hangman_ascii_list[42]
    hangman[43] = hangman_ascii_list[43]
    hangman[44] = hangman_ascii_list[44]
    return hangman

def add_body(hangman):
    hangman[59] = hangman_ascii_list[59]
    hangman[75] = hangman_ascii_list[75]
    return hangman

def add_left_hand(hangman):
    hangman[58] = hangman_ascii_list[58]
    return hangman

def add_right_hand(hangman):
    hangman[60] = hangman_ascii_list[60]
    return hangman

def add_left_foot(hangman):
    hangman[89] = hangman_ascii_list[89]
    return hangman

def add_right_foot(hangman):
    hangman[91] = hangman_ascii_list[91]
    return hangman

chosen_word = (random.choice(word_list)).lower()

original_word = chosen_word

# In case of hardcoding a word
# chosen_word = "vencedor"

chosen_word = [c for c in chosen_word]

blanked_word = ("_ " * len(chosen_word)).split()

lives = 6

# keep track of guessed letters
guessed = []

print(hangman_logo)
print("\n## Welcome to Hangman! ##\n")

while True:
    
    clear
    print("\n" + ' '.join(blanked_word) + "\n")
    print(''.join(hangman_game))
    guess = input("Guess a letter: ").lower()
    
    # Validate input
    
    if len([c for c in guess]) > 1:
        print("\nThe input must be a single letter!\n")
        continue
    elif guess.isnumeric():
        print("\nThe input must be a letter, not a number!\n")
        continue
    elif guess in guessed:
        print("\nYou already tried this letter! Try another!\n")
        continue
    
    # Remember this guessed letter
    guessed.append(guess)
        
    letter_hits = chosen_word.count(guess)
    
    if (letter_hits != 0):
        
        for x in range(1,letter_hits + 1):
            blanked_word[chosen_word.index(guess)] = guess
            chosen_word[chosen_word.index(guess)] = '*'
            
        print(f"\nCongrats! You've made {letter_hits} hits!")
        
    else:
        lives -= 1
        
        print("\nNo hits! You've lost 1 life!")
        
        if (lives == 5):
            hangman_game = add_head(hangman_game)
        elif (lives == 4):
            hangman_game = add_body(hangman_game)
        elif (lives == 3):
            hangman_game = add_left_hand(hangman_game)
        elif (lives == 2):
            hangman_game = add_right_hand(hangman_game)
        elif (lives == 1):
            hangman_game = add_left_foot(hangman_game)
        elif (lives == 0):
            hangman_game = add_right_foot(hangman_game)
            print("\n" + ' '.join(blanked_word) + "\n")
            print(''.join(hangman_game))
            print("\nYou Lost! Game Over.\n")
            print("The secret word was: " + ''.join(original_word) + ".")
            break;
            
    if (blanked_word.count("_") == 0):
        print("\nCongrats! You won! Game Over.")
        break; 