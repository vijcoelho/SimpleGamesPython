import random as rd
 
def write_a_word(): 
    global word
    word = "macarrao"

def main():
    global word
    for letter in word:
        print("_", end=" ")

def verification():
    global anwser
    anwser = ["_"] * len(word)
    for i in range(6):
        chance = input("\nPut a letter: ")
        for i, letter in enumerate(word):
            if letter == chance:
                anwser[i] = letter
                result = " ".join(anwser)
        print(result)
    print(f"Your chance is over, the anwser was {word}, try again!!")    

write_a_word()
main()
verification()

