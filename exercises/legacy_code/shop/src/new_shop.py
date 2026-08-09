from src.old_shop import OldShop


class NewShop:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def update_quality(self):
        for item in self.items:
            if item.name == "Sourdough Starter":
                # Legendary: quality and sell_in never change
                pass
            else:
                OldShop([item]).update_quality()

        return self.items
