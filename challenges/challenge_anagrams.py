def quicksort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return "", "", False

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    quicksort(first_string, 0, len(first_string) - 1)
    quicksort(second_string, 0, len(second_string) - 1)

    first_string = ''.join(first_string)
    second_string = ''.join(second_string)

    if first_string == second_string:
        return first_string, second_string, True

    return first_string, second_string, False
