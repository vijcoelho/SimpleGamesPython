import random as rd
 
def write_a_word(): 
    global word
    word = input("Put a word: ")

def main():
    for letter in word:
        print("_", end=" ")

def verification():
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

