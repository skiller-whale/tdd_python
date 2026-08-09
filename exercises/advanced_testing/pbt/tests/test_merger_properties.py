from hypothesis import given
from hypothesis import strategies as st
from merge_sort.merger import merge

# Hypothesis generates the raw lists; we sort them before merging so that
# `merge` is always given valid (sorted) input.
sorted_lists = st.lists(st.integers(min_value=0, max_value=100))


# Property: the merged output should always be in non-decreasing order.
#
# This currently passes.
@given(sorted_lists, sorted_lists)
def test_merged_output_is_sorted(left_raw, right_raw):
    merged = merge(sorted(left_raw), sorted(right_raw))

    assert merged == sorted(merged), f"expected sorted output but found {merged}"


# TODO: the merged list should contain every element from both inputs, so its length
# should equal len(left) + len(right).
# Add an assertion to check that, then run `pytest tests`.
@given(sorted_lists, sorted_lists)
def test_merge_preserves_length(left_raw, right_raw):
    left = sorted(left_raw)
    right = sorted(right_raw)

    merged = merge(left, right)  # noqa: F841

    # TODO: assert something about len(merged)


# TODO: the merged list should contain exactly the same elements as the two inputs
# combined. Sorting both sides and comparing is one easy way to check this.
# Add an assertion and run the tests.
@given(sorted_lists, sorted_lists)
def test_merge_preserves_all_elements(left_raw, right_raw):
    left = sorted(left_raw)
    right = sorted(right_raw)

    merged = merge(left, right)  # noqa: F841

    # TODO: assert merged holds the same elements as left and right combined
