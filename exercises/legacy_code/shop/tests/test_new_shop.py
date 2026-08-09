from src.item import Item
from src.new_shop import NewShop


class TestSourdoughStarter:
    def test_never_decreases_in_quality(self):
        item = Item("Sourdough Starter", 5, 80)
        NewShop([item]).update_quality()
        assert item.quality == 80

    def test_never_changes_its_sell_by_date(self):
        item = Item("Sourdough Starter", 5, 80)
        NewShop([item]).update_quality()
        assert item.sell_in == 5
