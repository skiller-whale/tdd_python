import pytest
from bun_and_board.till import LineItem, checkout


def test_empty_order_charges_nothing_and_earns_no_points():
    receipt = checkout([])
    assert receipt.total == pytest.approx(0.0)
    assert receipt.loyalty_points == 0


def test_small_order_has_delivery_fee_added():
    receipt = checkout([LineItem("Croissant", 3, 2.00)])
    assert receipt.total == pytest.approx(9.50)
    assert receipt.loyalty_points == 6


def test_bulk_discount_applied_when_buying_plenty_of_an_item():
    receipt = checkout([LineItem("Roll", 20, 1.00)])
    assert receipt.total == pytest.approx(21.50)
    assert receipt.loyalty_points == 18


def test_no_bulk_discount_for_a_modest_quantity():
    receipt = checkout([LineItem("Roll", 8, 1.00)])
    assert receipt.total == pytest.approx(11.50)
    assert receipt.loyalty_points == 8


def test_members_get_an_extra_discount_off_the_whole_order():
    receipt = checkout([LineItem("Cake", 1, 20.00)], member=True)
    assert receipt.total == pytest.approx(22.50)


def test_large_order_ships_for_free():
    receipt = checkout([LineItem("Cake", 2, 15.00)])
    assert receipt.total == pytest.approx(30.00)
    assert receipt.loyalty_points == 30


def test_multiple_lines_are_summed_with_bulk_discount_per_line():
    receipt = checkout(
        [
            LineItem("Croissant", 2, 2.00),
            LineItem("Roll", 12, 1.00),
        ]
    )
    assert receipt.total == pytest.approx(18.30)
    assert receipt.loyalty_points == 14
