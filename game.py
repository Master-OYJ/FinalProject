import random
import player
from gun import Gun
import items


class Game:
    def __init__(self, player_1, player_2):
        self.round = 1
        self.player_1 = player.Player(player_1)
        self.player_2 = player.Player(player_2)
        self.players = [self.player_1, self.player_2]
        self.current_turn = 0  # 0: player1's turn, 1: player2's turn
        self.gun = Gun()

    def start(self):
        print("Now game start!")

        while self.player_1.is_alive() and self.player_2.is_alive():
            print(f"\n======  Round {self.round}  ======")
            real_bullet = random.randint(1,3)
            self.gun.load(real_bullet)
            self.play_round()
            self.round += 1

            if self.player_1.is_alive() and self.player_2.is_alive():
                self.grant_items()

        self.game_over()

    def play_round(self):
        while not self.gun.is_empty() and self.player_1.is_alive() and self.player_2.is_alive():
            current_player = self.players[self.current_turn]
            # target = self.players[1 - self.current_turn]

            print(f"\n👉 It's {current_player.name}'s turn to shoot.")
            target = int(input("Press 1 to shoot player 1, or enter 2 to shoot player 2!\n"))
            if target < 1 or target > 2:
                print("Invaild number, enter again")
                continue
            target = target - 1
            hit = self.gun.fire(target)

            if hit:
                print("💥  Bang! It's a real bullet!")
                target.hp -= 1
                print(f"😵 {target.name} got hit! Remaining HP: {target.hp}")
                self.current_turn = 1 - self.current_turn
            elif hit == False and target == current_player:
                print("💨 Click! It was a blank... You have one more turn.")        
            else:
                print("💨 Click! It was a blank... Safe for now.")
                self.current_turn = 1 - self.current_turn

            

    def grant_items(self):
        print("\n End of round! Distributing random items...")
        for player in self.players:
            new_items = items.get_random_items()
            for item in new_items:
                player.get_item(item)

    def game_over(self):
        print("\nGame Over!")
        if self.player1.is_alive():
            winner = self.player1.name
        else:
            winner = self.player2.name
        print(f"Congratulations {winner}, you get the last piece of cake!")
