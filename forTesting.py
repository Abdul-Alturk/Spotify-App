import json
import time
from tqdm import tqdm


# with open('tracks.json', 'r', encoding='utf-8') as json_file:
#     python_Daten = json.load(json_file)


# songs_list  = list(python_Daten["All songs"].items())
# songs_list_keys = list(python_Daten.keys())



################# bubble sort #################
def bubble_sort(array):
    n = len(array)
    # Fortschrittsbalken initialisieren und am Ende ausblenden
    progress_bar = tqdm(total=n, desc="Sorting Progress", ncols=80)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j][0] > array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]
        progress_bar.update(1)

    progress_bar.close()
    return


################# insertion sort #################
def insertion_sort(array):
    n = len(array)
    progress_bar = tqdm(total=n, desc="Sorting Progress", ncols=80)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key[0] < array[j][0]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        progress_bar.update(1)

    progress_bar.close()
    return


################# quick sort #################
def quick_sort(array, progress_bar=None):
    if progress_bar is None:
        progress_bar = tqdm(total=len(array), desc="Sorting Progress", ncols=80)

    length = len(array)
    if length <= 1:
        progress_bar.update(1)
        return array

    pivot = array[-1]
    items_greater = []
    items_lower = []
    
    for item in array[:-1]:
        if item[0] > pivot[0]:
            items_greater.append(item)
        else:
            items_lower.append(item)
        progress_bar.update(1)
    
    sorted_lower = quick_sort(items_lower, progress_bar)
    sorted_greater = quick_sort(items_greater, progress_bar)

    # Schließe die Fortschrittsanzeige nach dem vollständigen Sortieren
    if progress_bar.total == progress_bar.n:
        progress_bar.close()

    return sorted_lower + [pivot] + sorted_greater

################# Merge sort #################
def merge_sort(array, progress_bar=None):
    # Erstelle die Fortschrittsanzeige, falls sie nicht bereits vorhanden ist
    if progress_bar is None:
        progress_bar = tqdm(total=len(array), desc="Sorting Progress", ncols=80)

    if len(array) > 1:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]
        
        merge_sort(left_array, progress_bar)
        merge_sort(right_array, progress_bar)

        i = j = k = 0
        
        while i < len(left_array) and j < len(right_array):
            if left_array[i][0] < right_array[j][0]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
            progress_bar.update(1)

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
            progress_bar.update(1)

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
            progress_bar.update(1)

    if progress_bar.total == progress_bar.n:
        progress_bar.close()

    return array

################# Selection sort #################
def selection_sort(array):
    n = len(array)
    progress_bar = tqdm(total=n, desc="Sorting Progress", ncols=80)
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j][0] < array[min_index][0]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        progress_bar.update(1)
    progress_bar.close()
    return array



################################################# search algorithms


################# linear search #################
def linearSearch(array, key):
    progress_bar = tqdm(total=len(array), desc="Searching Progress", ncols=80)
    for i in range(len(array)):
        if array[i][0] == key:
            progress_bar.close()
            return array[i]
        progress_bar.update(1)
    progress_bar.close()
    return print(f"⚠ The song {key} was not found.")


################# binary search #################
def binarySearch(array, key):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle][0] == key:
            return middle
        elif array[middle][0] < key:
            left = middle + 1
        else:
            right = middle - 1
    return print(f"⚠ The song {key} was not found.")