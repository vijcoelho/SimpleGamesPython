import random as rd 

computer_vec = [ ]
player_vec = [ ]

def card():
    player_vec.append(rd.randint(1,11))
    print(f"\n{player_vec}")

def computer_card():
    computer_vec.append(rd.randint(1,11))

def verify_winner_player():
    total_player = sum(player_vec)
    print("\nPlayer Total:", total_player)
    
    if total_player == 21:
        print("\nYou won!")
    elif total_player < 21:
        print("\nYou lose!")
    else:
        print("\nYou lose!")

def verify_winner_computer():
    total_computer = sum(computer_vec)
    print("\nComputer Total:", total_computer)
    
    if total_computer == 21:
        print("\nComputer won!")
    elif total_computer < 21:
        print("\nComputer lose!")
    else:
        print("\nComputer lose!")    


for i in range(5):
    computer_card()
while(True):
    playing_card = input("\nEnter for continue play, if u wanna stop press 0 : ")
    if playing_card == "0": break
    card()
verify_winner_player()
verify_winner_computer()
    