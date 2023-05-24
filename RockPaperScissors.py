import random

#ENJOY THIS GAME :)

def welcome():
    print("\t Welcome to Rock 🌑, Paper 📰, Scissors ✂️!!!")

def choose_player():
    global start
    start = int(input("\nChoose 1 for rock, 2 for paper and 3 for scissors.: "))
    if start < 1 or start > 3: 
        print("\nOnly 1, 2 or 3...")
        start = int(input("\nChoose 1 for rock, 2 for paper and 3 for scissors.: "))
    if start == 1:
        print("\nYou chose ROCK 🌑")
    elif start == 2:
        print("\nYou chose PAPER 📰")
    else: print("\nYou chose SCISSORS ✂️")

def choose_computer():
    global computer_turn
    computer_turn = random.randint(1,3)
    if computer_turn == 1:
        print("\nComputer has chose ROCK 🌑")
    elif computer_turn == 2:
        print("\nComputer has chose PAPER 📰")
    else: print("\nComputer has chose SCISSORS ✂️")

def verification():
    if start == computer_turn:
        print("\n\tIts a DRAW.😞😞")
    elif start == 1:
        if computer_turn == 2:
            print("\nComputer WIN!!😑😑")
        elif computer_turn == 3:
            print("\nYou WIN!!😄😄")
    elif start == 2:
        if computer_turn == 1:
            print("\nComputer WIN!!😑😑")
        elif computer_turn == 3:
            print("\nComputer WIN!!😑😑")
    elif start == 3:
        if computer_turn == 1:
            print("\nComputer WIN!!😑😑")
        elif computer_turn == 2:
            print("\nYou WIN!!😄😄")

while(True):
    
    welcome()
    choose_player()
    choose_computer()
    verification()
    stop = (input("\tIf u wanna stop this game type it 0: "))
    if stop == "0":
        break