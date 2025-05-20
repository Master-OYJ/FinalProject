import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, player, opponent=None, gun=None):
        """Base item does nothing, should be overridden by subclasses."""
        pass


class HealingCandy(Item):
    def __init__(self):
        super().__init__("Healing Candy", "Restores 1 HP.")

    def apply(self, player, opponent=None, gun=None):
        old_hp = player.hp
        player.hp = min(player.hp + 1, 3)
        print(f"{player.name} eats the candy and restores 1 HP! HP: {old_hp} → {player.hp}")


class ReverseCard(Item):
    def __init__(self):
        super().__init__("Reverse Card", "Reverses turn order.")

    def apply(self, player, opponent=None, gun=None):
        player.reverse_turn = True  # You can check this flag in game logic
        print(f"{player.name} activated Reverse Card! Turn order will be reversed.")


class XRayScope(Item):
    def __init__(self):
        super().__init__("X-Ray Scope", "Reveals whether the next bullet is real or blank.")

    def apply(self, player, opponent=None, gun=None):
        if gun and not gun.is_empty():
            bullet_type = gun.peek()
            print(f"{player.name} used X-Ray Scope! Next bullet is: {'REAL 🔴' if bullet_type else 'BLANK ⚪️'}.")
        else:
            print(f"{player.name} used X-Ray Scope, but the gun is empty.")


class DoubleShot(Item):
    def __init__(self):
        super().__init__("Double Shot", "Next shot deals 2 damage instead of 1.")

    def apply(self, player, opponent=None, gun=None):
        player.double_damage = True
        print(f"{player.name} activated Double Shot! Next hit will deal 2 damage.")


def get_random_items():
    item_classes = [HealingCandy, ReverseCard, XRayScope, DoubleShot]
    return [random.choice(item_classes)() for _ in range(3)]
