from src.item import Item
from src.shop import Shop


class TestNormalItems:
    def test_decreases_sell_in_by_1_each_day(self):
        item = Item("Bread", 5, 20)
        Shop([item]).update_quality()
        assert item.sell_in == 4

    def test_decreases_quality_by_1_before_the_sell_by_date(self):
        item = Item("Bread", 5, 20)
        Shop([item]).update_quality()
        assert item.quality == 19

    def test_decreases_quality_by_2_on_the_sell_by_date(self):
        item = Item("Bread", 0, 20)
        Shop([item]).update_quality()
        assert item.quality == 18

    def test_decreases_quality_by_2_each_day_after_the_sell_by_date(self):
        item = Item("Bread", -3, 20)
        Shop([item]).update_quality()
        assert item.quality == 18

    def test_continues_to_decrease_sell_in_when_quality_is_0(self):
        item = Item("Bread", 5, 0)
        Shop([item]).update_quality()
        assert item.sell_in == 4

    def test_quality_never_drops_below_0_before_the_sell_by_date(self):
        item = Item("Bread", 5, 0)
        Shop([item]).update_quality()
        assert item.quality == 0

    def test_quality_never_drops_below_0_on_the_sell_by_date(self):
        item = Item("Bread", 0, 1)
        Shop([item]).update_quality()
        assert item.quality == 0

    def test_quality_never_drops_below_0_after_the_sell_by_date(self):
        item = Item("Bread", -1, 1)
        Shop([item]).update_quality()
        assert item.quality == 0

    def test_degrades_correctly_over_days_spanning_the_sell_by_date(self):
        item = Item("Bread", 2, 10)
        shop = Shop([item])
        shop.update_quality()  # sell_in 1, quality 9
        shop.update_quality()  # sell_in 0, quality 8
        shop.update_quality()  # sell_in -1, quality 6
        shop.update_quality()  # sell_in -2, quality 4
        assert item.quality == 4
        assert item.sell_in == -2


class TestFruitCake:
    def test_decreases_sell_in_by_1(self):
        item = Item("Fruit Cake", 5, 10)
        Shop([item]).update_quality()
        assert item.sell_in == 4

    def test_increases_quality_by_1_before_the_sell_by_date(self):
        item = Item("Fruit Cake", 5, 10)
        Shop([item]).update_quality()
        assert item.quality == 11

    def test_increases_quality_by_2_on_the_sell_by_date(self):
        item = Item("Fruit Cake", 0, 10)
        Shop([item]).update_quality()
        assert item.quality == 12

    def test_increases_quality_by_2_after_the_sell_by_date(self):
        item = Item("Fruit Cake", -2, 10)
        Shop([item]).update_quality()
        assert item.quality == 12

    def test_quality_never_exceeds_50(self):
        item = Item("Fruit Cake", 5, 50)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_quality_is_capped_at_50_before_the_sell_by_date(self):
        item = Item("Fruit Cake", 5, 49)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_quality_is_capped_at_50_after_the_sell_by_date(self):
        item = Item("Fruit Cake", -1, 49)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_increases_quality_over_days_spanning_the_sell_by_date(self):
        item = Item("Fruit Cake", 2, 40)
        shop = Shop([item])
        shop.update_quality()  # +1, sell_in 1, quality 41
        shop.update_quality()  # +1, sell_in 0, quality 42
        shop.update_quality()  # +2, sell_in -1, quality 44
        shop.update_quality()  # +2, sell_in -2, quality 46
        assert item.quality == 46


class TestSourdoughStarter:
    def test_never_changes_quality(self):
        item = Item("Sourdough Starter", 0, 80)
        Shop([item]).update_quality()
        assert item.quality == 80

    def test_never_changes_the_sell_by_date(self):
        item = Item("Sourdough Starter", 0, 80)
        Shop([item]).update_quality()
        assert item.sell_in == 0

    def test_remains_completely_unchanged_after_many_days(self):
        item = Item("Sourdough Starter", 0, 80)
        shop = Shop([item])
        for _ in range(30):
            shop.update_quality()
        assert item.quality == 80
        assert item.sell_in == 0


class TestWeddingCake:
    def test_decreases_sell_in_by_1(self):
        item = Item("Wedding Cake", 15, 20)
        Shop([item]).update_quality()
        assert item.sell_in == 14

    def test_increases_quality_by_1_with_more_than_10_days_remaining(self):
        item = Item("Wedding Cake", 15, 20)
        Shop([item]).update_quality()
        assert item.quality == 21

    def test_increases_quality_by_1_with_exactly_11_days_remaining(self):
        item = Item("Wedding Cake", 11, 20)
        Shop([item]).update_quality()
        assert item.quality == 21

    def test_increases_quality_by_2_with_exactly_10_days_remaining(self):
        item = Item("Wedding Cake", 10, 20)
        Shop([item]).update_quality()
        assert item.quality == 22

    def test_increases_quality_by_2_with_6_days_remaining(self):
        item = Item("Wedding Cake", 6, 20)
        Shop([item]).update_quality()
        assert item.quality == 22

    def test_increases_quality_by_3_with_exactly_5_days_remaining(self):
        item = Item("Wedding Cake", 5, 20)
        Shop([item]).update_quality()
        assert item.quality == 23

    def test_increases_quality_by_3_with_1_day_remaining(self):
        item = Item("Wedding Cake", 1, 20)
        Shop([item]).update_quality()
        assert item.quality == 23

    def test_drops_quality_to_0_on_the_sell_by_date(self):
        item = Item("Wedding Cake", 0, 20)
        Shop([item]).update_quality()
        assert item.quality == 0

    def test_quality_stays_0_after_the_sell_by_date(self):
        item = Item("Wedding Cake", -1, 0)
        Shop([item]).update_quality()
        assert item.quality == 0

    def test_sell_in_continues_to_decrease_after_the_sell_by_date(self):
        item = Item("Wedding Cake", -1, 0)
        Shop([item]).update_quality()
        assert item.sell_in == -2

    def test_quality_never_exceeds_50(self):
        item = Item("Wedding Cake", 5, 50)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_quality_is_capped_at_50_with_high_rate_increases(self):
        item = Item("Wedding Cake", 5, 48)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_quality_is_capped_at_50_with_moderate_rate_increases(self):
        item = Item("Wedding Cake", 10, 49)
        Shop([item]).update_quality()
        assert item.quality == 50

    def test_simulates_a_full_run_up_to_the_wedding(self):
        item = Item("Wedding Cake", 15, 5)
        shop = Shop([item])

        # Days 15-11: +1/day for 5 days = +5
        for _ in range(5):
            shop.update_quality()
        assert item.quality == 10
        assert item.sell_in == 10

        # Days 10-6: +2/day for 5 days = +10
        for _ in range(5):
            shop.update_quality()
        assert item.quality == 20
        assert item.sell_in == 5

        # Days 5-1: +3/day for 5 days = +15
        for _ in range(5):
            shop.update_quality()
        assert item.quality == 35
        assert item.sell_in == 0

        # Day 0: quality drops to 0
        shop.update_quality()
        assert item.quality == 0
        assert item.sell_in == -1


class TestMultipleItems:
    def test_updates_all_items_in_a_single_call(self):
        bread = Item("Bread", 3, 10)
        fruit_cake = Item("Fruit Cake", 3, 10)
        sourdough = Item("Sourdough Starter", 0, 80)
        wedding_cake = Item("Wedding Cake", 8, 20)

        Shop([bread, fruit_cake, sourdough, wedding_cake]).update_quality()

        assert bread.quality == 9
        assert fruit_cake.quality == 11
        assert sourdough.quality == 80
        assert wedding_cake.quality == 22


class TestReturnValue:
    def test_returns_the_same_items_list(self):
        items = [Item("Bread", 5, 10)]
        result = Shop(items).update_quality()
        assert result is items
