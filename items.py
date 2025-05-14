import random

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def apply(self, player):
        # Default effect (should be overridden)
        pass


class HealingCandy(Item):
    def __init__(self):
        super().__init__("Healing Candy", "Restores 1 HP.")

    def apply(self, player):
        player.hp += 1
        print(f"{player.name} eats the candy and restores 1 HP! Total HP: {player.hp}")


class ReverseCard(Item):
    def __init__(self):
        super().__init__("Reverse Card", "Reverses turn order.")

    def apply(self, player):
        player.reverse_turn = True  # We'll handle this in game logic if needed
        print(f"{player.name} activated Reverse Card! Turn order will be reversed.")


class XRayScope(Item):
    def __init__(self):
        super().__init__("X-Ray Scope", "Reveals whether the next bullet is real or blank.")

    def apply(self, player):
        player.xray = True
        print(f"{player.name} used X-Ray Scope! They will see the next bullet type.")


class DoubleShot(Item):
    def __init__(self):
        super().__init__("Double Shot", "If the shot hits, it deals 2 damage instead of 1.")

    def apply(self, player):
        player.double_damage = True
        print(f"{player.name} used Double Shot! The next hit will deal 2 damage.")


def get_random_items():
    item_classes = [HealingCandy, ReverseCard, XRayScope, DoubleShot]
    items = []
    for i in range(3):
        items.append(random.choice(item_classes))