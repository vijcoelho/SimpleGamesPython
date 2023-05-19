import random as rd

# THIS CODE IS NOT FINISHED YET
def write_a_string():
    global word
    with open("C:/Users/u23623/Documents/GitHub/SimpleGamesPython/hangman.txt", "a") as txt:
        word = input("Put a random word: ")
        txt.writelines(f"\n{word}")
    
def pick_a_string():
    search = input("search a word:")
    with open("C:/Users/u23623/Documents/GitHub/SimpleGamesPython/hangman.txt", "r") as txt:
        line = txt.readlines()
        find = False
        for i, line in enumerate(line):
            if search in line:
                find = True
                print(line)


pick_a_string()

            

