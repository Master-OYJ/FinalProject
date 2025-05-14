import random

class Gun:
    def __init__(self):
        self.magazine = []

    def load(self, num_real):
        """Load the gun with specified number of real and blank bullets, then shuffle."""
        num_blank = 6 - num_real
        self.magazine = [True] * num_real + [False] * num_blank
        random.shuffle(self.magazine)
        print(f"\n Gun loaded with {num_real} real and {num_blank} blank bullets.")

    def fire(self):
        """Simulate firing the gun. Returns True if it's a real bullet, False if blank."""
        if not self.magazine:
            print("Gun is empty! Reload required.")
            return None
        bullet = self.magazine.pop(0)
        return bullet

    def is_empty(self):
        return len(self.magazine) == 0

    def peek(self):
        """Reveal the next bullet type (True for real, False for blank)."""
        if not self.magazine:
            return None
        return self.magazine[0]
