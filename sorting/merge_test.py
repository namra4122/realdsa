from merge_sort import MergeSort

def test_merge_sort():
    # Test helpers
    def arrays_equal(a, b):
        return a == b

    def is_sorted(a):
        return all(a[i] <= a[i+1] for i in range(len(a)-1))

    # 1. Normal unsorted list (positive, negative, mixed)
    m1 = MergeSort([22, 3, 4, 5, 1, 2, 388, 6, 9, 8, 0])
    m1.sort()
    assert is_sorted(m1.data), "Case 1: should be sorted"

    # 2. Already sorted list
    m2 = MergeSort([1, 2, 3, 4, 5])
    m2.sort()
    assert is_sorted(m2.data), "Case 2: already sorted"
    assert m2.data == [1, 2, 3, 4, 5], "Case 2: order unchanged"

    # 3. Reverse‑sorted list
    m3 = MergeSort([5, 4, 3, 2, 1])
    m3.sort()
    assert is_sorted(m3.data), "Case 3: reverse sorted"
    assert m3.data == [1, 2, 3, 4, 5], "Case 3: correct order"

    # 4. Single element
    m4 = MergeSort([42])
    m4.sort()
    assert m4.data == [42], "Case 4: single element"

    # 5. Empty list
    m5 = MergeSort([])
    m5.sort()
    assert m5.data == [], "Case 5: empty list"

    # 6. Duplicates
    m6 = MergeSort([3, 1, 4, 1, 5, 9, 2, 6, 5])
    m6.sort()
    assert is_sorted(m6.data), "Case 6: duplicates, should still sort"
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert m6.data == expected, "Case 6: correct duplicate handling"

    # 7. Two elements (both orderings)
    m7a = MergeSort([2, 1])
    m7a.sort()
    assert m7a.data == [1, 2], "Case 7a: two elements, reverse"

    m7b = MergeSort([1, 2])
    m7b.sort()
    assert m7b.data == [1, 2], "Case 7b: two elements, already sorted"

    # 8. Negative numbers
    m8 = MergeSort([0, -1, -5, 3, -3, 10])
    m8.sort()
    expected = [-5, -3, -1, 0, 3, 10]
    assert m8.data == expected, "Case 8: negatives + zero + positives"

    # 9. All same values
    m9 = MergeSort([7, 7, 7, 7])
    m9.sort()
    assert m9.data == [7, 7, 7, 7], "Case 9: all equal"

    # 10. Large list (sanity, not exhaustive)
    large = list(range(1000, 0, -1))  # [1000, 999, ... 1]
    m10 = MergeSort(large.copy())
    m10.sort()
    assert m10.data == sorted(large), "Case 10: large reverse‑sorted"

    print("All merge‑sort tests passed.")
