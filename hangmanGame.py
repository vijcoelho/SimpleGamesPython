import random as rd

# THIS CODE IS NOT FINISHED 
def write_a_word(): 
    global word
    with open("C:/Users/u23623/Documents/GitHub/SimpleGamesPython/hangman.txt", "a") as txt:
        word = input("Put a word: ")
        word_code = input("Put a code for this word: ")
        txt.writelines(f"\n{word + word_code}")

def pick_a_word():
    search = input("search a number for find a word:")
    with open("C:/Users/u23623/Documents/GitHub/SimpleGamesPython/hangman.txt", "r+") as txt:
        line = txt.readlines()
        for i, line in enumerate(line):
            if search in line:
                new_word = line[:-1]
                print(new_word)

def game():
    
















ops = input("If u want write a word PRESS 1, but if u want pick a random word PRESS 2.: ")
if ops == "1":
    write_a_word()
elif ops == "2":      
    pick_a_word()


