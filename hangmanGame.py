import random as rd

# THIS CODE IS NOT FINISHED 
def write_a_word(): 
    global word
    word = input("\nPut a word: ")

def main():
    global word
    for letter in word:
        print("_", end=" ")

def verification():


write_a_word()
main()


