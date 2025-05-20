import random
import player
from gun import Gun
import items
from colorama import Fore, Style, init

init(autoreset=True)  # 自动重置颜色，避免污染后续输出


class Game:
    def __init__(self, player_1, player_2):
        self.round = 1
        self.player_1 = player.Player(player_1)
        self.player_2 = player.Player(player_2)
        self.players = [self.player_1, self.player_2]
        self.current_turn = 0  # 0: player1's turn, 1: player2's turn
        self.gun = Gun()

    def start(self):
        print("🎉 The party begins! The last piece of cake is on the line!\n")

        while self.player_1.is_alive() and self.player_2.is_alive():
            print(f"\n======  Round {self.round}  ======")
            real_bullet = random.randint(2, 3)
            self.gun.load(real_bullet)
            self.play_round()
            self.round += 1

            if self.player_1.is_alive() and self.player_2.is_alive():
                self.grant_items()

        self.game_over()


    def play_round(self):
        taunts = {
            "not_a_number": [
                "You can't even type a number?",
                "Numbers are too hard for you?",
                "Try using your fingers to count!"
            ],
            "invalid_number": [
                "You sure you know how to play?",
                "That's not even an option!",
                "Read the instructions maybe?"
            ],
            "invalid_item_slot": [
                "Trying to cheat with invisible items?",
                "You don't have that many items!",
                "Even your items don't like you!"
            ],
            "normal": [
                "😏 You call that a shot?",
                "😂 My grandma aims better!",
                "😮 Missed again? Try glasses!",
                "🙄 I'm not even sweating.",
                "😜 You sure this is your turn?"
            ]
        }

        while not self.gun.is_empty() and self.player_1.is_alive() and self.player_2.is_alive():
            current_player = self.players[self.current_turn]
            opponent = self.players[1 - self.current_turn]

            print(Fore.CYAN + "\n" + "=" * 45)
            print(Fore.CYAN + f"🎯 TURN: {current_player.name}")
            print(Fore.CYAN + "=" * 45)
            print(Fore.RED + f"❤️ HP: {current_player.hp}")
            print(Fore.YELLOW + "🎒 Items:")
            if current_player.items:
                for i, item in enumerate(current_player.items):
                    print(Fore.YELLOW + f"  [{i + 4}] {item.name} - {item.description}")
            else:
                print(Fore.YELLOW + "  (No items)")
            
            # 🔍 X-RAY effect
            if getattr(current_player, 'xray', False):
                next_bullet = self.gun.peek()
                if next_bullet is not None:
                    bullet_info = f"{Fore.RED}REAL 🔴" if next_bullet else f"{Fore.WHITE}BLANK ⚪️"
                    print(Fore.MAGENTA + f"\n🔍 X-RAY ACTIVE: Next bullet is {bullet_info}")
                else:
                    print(Fore.MAGENTA + "\n🔍 X-RAY ACTIVE: Gun is empty.")
                current_player.xray = False

            print(Fore.GREEN + "\n📌 ACTION OPTIONS:")
            print(Fore.GREEN + "  [1] Shoot Player 1")
            print(Fore.GREEN + "  [2] Shoot Player 2")
            print(Fore.GREEN + "  [4~6] Use item in slot 4~6")
            user_input = input(Fore.LIGHTBLUE_EX + "💬 Enter your action: ")

            try:
                action = int(user_input)
            except ValueError:
                print(Fore.RED + "\n❌ Invalid input! That’s not even a number.")
                print(Fore.LIGHTMAGENTA_EX + "🧠💬", f"{opponent.name} taunts: \"{random.choice(taunts['not_a_number'])}\"")
                continue

            if action in [1, 2]:
                target = self.players[action - 1]
                hit = self.gun.fire()

                damage = 2 if current_player.double_damage else 1
                current_player.double_damage = False

                if hit:
                    print(Fore.RED + "\n💥 BANG! It was a REAL BULLET!")
                    target.hp -= damage
                    print(Fore.RED + f"😵 {target.name} took {damage} damage! HP left: {target.hp}")
                    print(Fore.LIGHTMAGENTA_EX + "🧠💬", f"{opponent.name} taunts: \"{random.choice(taunts['normal'])}\"")
                    self.current_turn = 1 - self.current_turn
                elif not hit and target == current_player:
                    print(Fore.BLUE + "\n💨 CLICK! Blank shot at yourself! Extra turn granted.")
                else:
                    print(Fore.BLUE + "\n💨 CLICK! Just a blank... You're lucky.")
                    self.current_turn = 1 - self.current_turn

            elif action in [4, 5, 6]:
                index = action - 4
                if index < len(current_player.items):
                    item = current_player.items.pop(index)
                    print(Fore.CYAN + f"\n🧪 Using item: {item.name}")
                    item.apply(current_player, opponent, self.gun)
                else:
                    print(Fore.RED + "\n❌ Invalid item slot! No item there.")
                    print(Fore.LIGHTMAGENTA_EX + "🧠💬", f"{opponent.name} taunts: \"{random.choice(taunts['invalid_item_slot'])}\"")
            else:
                print(Fore.RED + "\n❌ Invalid number! Choose 1, 2 or 4~6.")
                print(Fore.LIGHTMAGENTA_EX + "🧠💬", f"{opponent.name} taunts: \"{random.choice(taunts['invalid_number'])}\"")







    def grant_items(self):
        print("\n🎁 End of round! Distributing random items...")
        for p in self.players:
            new_items = items.get_random_items()
            for item in new_items:
                p.get_item(item)

    def game_over(self):
        print("\n🏁 Game Over!")
        if self.player_1.is_alive():
            winner = self.player_1.name
        else:
            winner = self.player_2.name
        print(f"🎂 Congratulations {winner}, you get the last piece of cake!")
