import random
import collections
import string

right = 0
att = 8


def game_start():
    print("Welcome to Hangman")
    global words
    global user_guess
    global rnd_word
    words = ("python", "java", "javascript", "php")
    rnd_word = random.randint(0, int(len(words)))


game_start()
main_word = list(words[rnd_word])


def main_menu():
    play = input("Type 'play' to start. Type 'exit' to quit: ")
    if play == 'exit':
        print("You quit the game")
        raise SystemExit(1)
    if play != 'play':
        print("try again!")
        main_menu()

def user_word():
    main_menu()
    global guessed_word_list
    global user_guess
    guessed_word_list = list(words[rnd_word])
    i = -1
    for j in guessed_word_list:
        i += 1
        guessed_word_list[i] = "-"
    print("".join(map(str, guessed_word_list)))


user_word()


def main_function():
    user_guess = input("Guess a letter: ")
    if int(len(user_guess)) > 1:
        user_guess = input("Please, enter 1 letter, using english lowercase letters: ")
    okay = False
    for k in string.ascii_lowercase:
        if k == user_guess:
            okay = True
    if not okay:
        user_guess = input("lowercase letters: ")

    for k in guessed_word_list:
        if (k == user_guess):
            print("You've already guessed this letter!")
            main_function()
            return

    def comparing():
        i = -1
        global ugadal
        ugadal = False
        for k in main_word:
            i += 1
            if user_guess == k:
                guessed_word_list[i] = k
                ugadal = True
    comparing()

    def word_output():
        global att
        print("".join(map(str, guessed_word_list)))
        if ugadal == False:
            att -= 1
            print("That letter doesn't appear in the word")
            print(str(att))

        if collections.Counter(guessed_word_list) == collections.Counter(main_word):
            print("You win")
            raise SystemExit(1)

    word_output()


while att > 0:
    main_function()
    if (att == 0):
        print("You lose!")
        raise SystemExit(1)
