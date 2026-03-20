"""
Custom sorting implementation using Merge Sort.
Supports alphabetical (string) and numerical sorting,
ascending or descending — without using sort() or sorted().
"""

def merge_sort(lst: list, reverse: bool = False) -> list:
    """
    Recursively splits the list in half, sorts each half,
    then merges them back together in order.

    Works for both strings (alphabetical) and numbers (numerical).

    Args:
        lst:     The list to sort.
        reverse: If True, sort in descending order.

    Returns:
        A new sorted list (the original is not modified).
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid], reverse)
    right = merge_sort(lst[mid:], reverse)

    return _merge(left, right, reverse)


def _merge(left: list, right: list, reverse: bool) -> list:
    """
    Merges two sorted lists into one sorted list.
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        # For strings, Python's < / > operators compare lexicographically,
        # so the same logic covers both numeric and alphabetical sorting.
        left_wins = left[i] > right[j] if reverse else left[i] < right[j]

        if left_wins:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append whatever's left in either half
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    numbers = [42, 7, 19, 3, 100, 55, 1, 88]
    words   = ["banana", "apple", "cherry", "date", "elderberry", "fig"]

    print("=== Numeric Sorting ===")
    print(f"  Original:   {numbers}")
    print(f"  Ascending:  {merge_sort(numbers)}")
    print(f"  Descending: {merge_sort(numbers, reverse=True)}")

    print("\n=== Alphabetical Sorting ===")
    print(f"  Original:   {words}")
    print(f"  Ascending:  {merge_sort(words)}")
    print(f"  Descending: {merge_sort(words, reverse=True)}")

    # Edge cases
    print("\n=== Edge Cases ===")
    print(f"  Empty list:      {merge_sort([])}")
    print(f"  Single element:  {merge_sort([99])}")
    print(f"  Already sorted:  {merge_sort([1, 2, 3, 4, 5])}")
    print(f"  Reverse sorted:  {merge_sort([5, 4, 3, 2, 1])}")
    print(f"  Duplicates:      {merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5])}")
    
#---------------------------------------------------------------------------------
# Sample command line code.
#---------------------------------------------------------------------------------
#python sorter.py