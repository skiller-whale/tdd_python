"""The Bun & Board till: totals an order, applies discounts, awards loyalty points."""

from dataclasses import dataclass

BULK_THRESHOLD = 10
BULK_DISCOUNT = 0.10
MEMBER_DISCOUNT = 0.05
FREE_DELIVERY_THRESHOLD = 25.0
DELIVERY_FEE = 3.50


@dataclass(frozen=True)
class LineItem:
    name: str
    quantity: int
    unit_price: float


@dataclass(frozen=True)
class Receipt:
    total: float
    loyalty_points: int


def checkout(items, member=False):
    subtotal = 0.0
    for item in items:
        line_total = item.quantity * item.unit_price
        if item.quantity > BULK_THRESHOLD:
            line_total -= line_total * BULK_DISCOUNT
        subtotal += line_total

    if member:
        subtotal -= subtotal * MEMBER_DISCOUNT

    delivery = DELIVERY_FEE
    if subtotal >= FREE_DELIVERY_THRESHOLD:
        delivery = 0.0
    if subtotal == 0.0:
        delivery = 0.0

    points = int(subtotal)
    if member:
        points *= 2

    return Receipt(total=round(subtotal + delivery, 2), loyalty_points=points)
