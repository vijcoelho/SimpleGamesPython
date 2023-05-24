import random

def welcome():
    print("\t##############################################")
    print("\t#         Welcome To Pig Game Dice           #")
    print("\t##############################################")

def start_game():
    global start
    start = int(input("How much face the dice will have: "))
    
def turn():
    global person_turn
    global computer_turn    
    person_turn = random.randint(1,start)
    print(f"\n\tYour Number |{person_turn}|")
    computer_turn = random.randint(1,start)
    print("\t---")
    print(f"\tComputer Number |{computer_turn}|")
    

def verification():
    if person_turn == computer_turn: print("\n\t Its a DRAW!!")
    elif person_turn > computer_turn: print("\n\t You WON!!")
    else: print("\n\t You LOSE!!")

while(True):
    welcome()
    start_game()
    turn()
    verification()
    stop = input("If you wanna stop the game enter 0, to continue to play just press <ENTER>: ")
    if stop == "0": break