# Mutation Testing: The Bun & Board Till

## The Story

Allison's bakery, **The Bun & Board**, has a new electronic till. It totals up an order, applies
the shop's discounts and delivery rules, and works out loyalty points for regulars.

`bun_and_board/till.py` implements the rules:

- Each line costs `quantity * unit_price`.
- **Bulk discount:** 10% off a line when more than 10 of that item are bought.
- **Loyalty discount:** members get a further 5% off the whole order.
- **Delivery:** free when the discounted subtotal is £25.00 or more, otherwise £3.50 (an empty
  order is never charged for delivery).
- **Loyalty points:** 1 point per whole pound of the discounted subtotal, doubled for members.

`tests/test_till.py` already has a test suite that *looks* fairly thorough — and it is fully green.
But green tests with high coverage can still miss important behaviour. Your job is to find those
gaps using **mutation testing**.

## Your task

1. Pick a small change to `till.py` that should break its behaviour — a "mutation". For example,
   change a `>` to `>=`, tweak a constant, or delete a branch.
2. Run the tests. If they fail, good — the suite caught the mutation. If they still pass, you have
   found a gap.
3. When you find a surviving mutation, add or tighten a test until it fails for the mutated code.
4. Revert your mutation and check the suite is green again.
5. Repeat once or twice by hand, then let **mutmut** do it automatically (see below).

## Run the tests once

```bash
pytest tests
```

## Run the tests in watch mode

```bash
ptw tests
```

## Run automated mutation testing with mutmut

```bash
mutmut run
```

Then list what it found:

```bash
mutmut results
```

Anything reported as **survived** is a mutation your tests did not catch — exactly the gaps you
are hunting for. To see what a surviving mutant actually changed:

```bash
mutmut show bun_and_board.till.x_checkout__mutmut_6
```

You can also browse the results interactively with `mutmut browse`.

> Note: not every surviving mutant is a real gap. Some are **equivalent mutants** — changes that
> don't actually alter the behaviour, so no test could ever catch them. Part of the skill is
> telling the two apart.
