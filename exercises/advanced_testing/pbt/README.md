# Property-Based Testing: Merging Sorted Lists

## The Story

`merge_sort/merger.py` takes two already-sorted lists of integers and merges them into a single
sorted list — the same merge step at the heart of merge sort.

It has a bug. Rather than hunting for it with hand-picked examples, you will describe the
**properties** a correct merge must always have, and let [Hypothesis](https://hypothesis.works/)
generate hundreds of inputs trying to break them. When a property fails, Hypothesis **shrinks**
the failure to the smallest counter-example it can find.

## Your task

Open `tests/test_merger_properties.py`. It contains:

- A worked property, `test_merged_output_is_sorted`, which already passes — note that a buggy
  merge can still produce sorted output, so this property alone is not enough.
- Two `TODO` properties for you to complete:
  - `test_merge_preserves_length` — the merged list should be as long as both inputs combined.
  - `test_merge_preserves_all_elements` — the merged list should contain exactly the same elements.

Complete the two properties, run the tests, and read the shrunk minimal counter-example. Then fix
`merge` until every property holds.

## Run the tests once

```bash
pytest tests
```

## Run the tests in watch mode

```bash
ptw tests
```
