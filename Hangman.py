import random
from word import words
import string


def word_get(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = word_get(words)
    letters = set(word)  # letters in the word
    alp = set(string.ascii_uppercase)
    used = set()  # what the user has guessed
    lives = 7
    while len(letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used))
        word_list = [letter if letter in used else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alp - used:
            used.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Invalid")
        elif user_letter in used:
            print("Already used. ")
    if lives == 0:
        print("You died. Word was", word)
    else:
        print("Guessed: ", word)


if __name__ == '__main__':
    hangman()
