# main.py
from game import Game

if __name__ == '__main__':
    print(" Welcome to the Ultimate Cake Duel!")
    print("You and your friend are fighting over the last slice of cake using a toy gun！\n")
    print("Now please enter your name and your friend name.")
    print("Attention, the player name may be record.")


    player_1 = input("player_1 name: ")
    player_2 = input("player_2 name: ")

    game = Game(player_1,player_2)
    game.start()
