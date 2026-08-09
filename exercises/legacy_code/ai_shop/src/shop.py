class Shop:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def update_quality(self):
        for i in range(len(self.items)):
            if self.items[i].name != "Fruit Cake" and self.items[i].name != "Wedding Cake":
                if self.items[i].quality > 0:
                    if self.items[i].name != "Sourdough Starter":
                        self.items[i].quality = self.items[i].quality - 1
            else:
                if self.items[i].quality < 50:
                    self.items[i].quality = self.items[i].quality + 1
                    if self.items[i].name == "Wedding Cake":
                        if self.items[i].sell_in < 11:
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 1
                        if self.items[i].sell_in < 6:
                            if self.items[i].quality < 50:
                                self.items[i].quality = self.items[i].quality + 1
            if self.items[i].name != "Sourdough Starter":
                self.items[i].sell_in = self.items[i].sell_in - 1
            if self.items[i].sell_in < 0:
                if self.items[i].name != "Fruit Cake":
                    if self.items[i].name != "Wedding Cake":
                        if self.items[i].quality > 0:
                            if self.items[i].name != "Sourdough Starter":
                                self.items[i].quality = self.items[i].quality - 1
                    else:
                        self.items[i].quality = self.items[i].quality - self.items[i].quality
                else:
                    if self.items[i].quality < 50:
                        self.items[i].quality = self.items[i].quality + 1

        return self.items
