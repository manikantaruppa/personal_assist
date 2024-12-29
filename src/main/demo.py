
def bubble_sort(arr):
    """
    Sorts a list of integers using the bubble sort algorithm.

    Args:
        arr (list): The list of integers to be sorted.

    Returns:
        list: The sorted list of integers.

    Examples:
        >>> bubble_sort([5, 3, 8, 2, 1])
        [1, 2, 3, 5, 8]
        >>> bubble_sort([9, 4, 7, 6, 2])
        [2, 4, 6, 7, 9]
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the bubble_sort function
print(bubble_sort([5, 3, 8, 2, 1]))
print(bubble_sort([9, 4, 7, 6, 2]))
