class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 3  # Health points at the start of each round
        self.items = []  # Holds up to 3 items
        self.xray = False
        self.reverse_turn = False
        self.double_damage = False

    def is_alive(self):
        return self.hp > 0

    def reset_for_new_round(self):
        """Reset health and temporary flags for a new round."""
        self.hp = 3
        self.xray = False
        self.reverse_turn = False
        self.double_damage = False
        # Items are not reset here

    def use_item(self, index):
        """Use an item by index (0-2), apply its effect, and remove it."""
        if 0 <= index < len(self.items):
            item = self.items.pop(index)
            item.apply(self)
        else:
            print("Invalid item index.")

    def get_item(self, item):
        """Try to pick up an item. Reject if inventory is full."""
        if len(self.items) < 3:
            self.items.append(item)
            print(f"{self.name} received: {item.name} - {item.description}")
        else:
            print(f"{self.name}'s inventory is full. {item.name} was discarded.")

    def show_status(self):
        print(f"\n{self.name} | HP: {self.hp}")
        print(" Items:")
        if self.items:
            for i, item in enumerate(self.items):
                print(f"  {i + 1}. {item.name} - {item.description}")
        else:
            print("  (No items)")
