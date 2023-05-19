def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    print(i)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# Example usage:
array = [5, 2, 9, 1, 7, 6, 3]
n = len(array)
quick_sort(array, 0, n - 1)
print(array)
