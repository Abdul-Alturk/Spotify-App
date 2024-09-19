import json
import time
from tqdm import tqdm


with open('tracks.json', 'r', encoding='utf-8') as json_file:
    python_Daten = json.load(json_file)


songs_list  = list(python_Daten["All songs"].items())
songs_list_keys = list(python_Daten.keys())
# print(songs_list)



################# bubble sort #################
def bubble_sort(array):
    start = time.time()
    n = len(array)
    # Fortschrittsbalken initialisieren und am Ende ausblenden
    progress_bar = tqdm(total=n, desc="Sorting Progress", ncols=80)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j][0] > array[j + 1][0]:
                array[j], array[j + 1] = array[j + 1], array[j]
        progress_bar.update(1)

    progress_bar.close()
    end = time.time()
    return array , end - start


# print(bubble_sort(songs_list))
# print(len(songs_list_keys))

### Time ###
# 374.0419
# 841.2923
# 421.9551
# 412.4652
# 415.9117
# 413.1437
# mean = 479.802 seconds




################# insertion sort #################
def insertion_sort(array):
    start = time.time()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key[0] < array[j][0]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    end = time.time()
    return array , end - start

# print(insertion_sort(songs_list))
# print(len(songs_list_keys))

### Time ###
# 192.6210
# 301.5926
# 305.1113
# 213.2400
# 158.1961
# 162.1725
# mean = 222.156 seconds




################# quick sort part 1 #################
def quick_sort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort(array, left, pivot - 1)
        quick_sort(array, pivot + 1, right)
    # end = time.time()
    return array

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right][0]
    while i < j:
        while i < right and array[i][0] < pivot:
            # print(array[i][0])
            i += 1
        while j > left and array[j][0] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    if array[i][0] > pivot:
        array[i], array[right] = array[right], array[i]
        
    return i

# start = time.time()
# list = quick_sort(songs_list, 0, len(songs_list) - 1)
# print(len(songs_list))
# print(list)

# python_Daten["All songs"] = dict(songs_list)
# with open('trackssss.json', 'w', encoding='utf-8') as json_file:
#     json.dump(python_Daten, json_file, ensure_ascii=False, indent=4)

### Time ###
# 0.1724
# 0.1666
# 0.1945
# 0.1874
# 0.1949
# 0.1929
# mean = 0.185 seconds



################# quick sort part 2 #################
def quick_sort_2(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence

    pivot = sequence.pop()
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item[1][1] > pivot[1][1]:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    else:
        
        return quick_sort_2(items_lower) + [pivot] + quick_sort_2(items_greater)

# start = time.time()
# sorted_list = quick_sort_2(songs_list)
# # sorted_list = quick_sort_2(songs_list)
# end = time.time()

# print(sorted_list)
# print(len(songs_list))
# print(end - start)



################# Merge sort #################
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]
        merge_sort(left_array)
        merge_sort(right_array)
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i][0] < right_array[j][0]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    end = time.time()
    return "Done" #array , #end - start

# start = time.time()
# print(merge_sort(songs_list))
# print(merge_sort(songs_list))
# python_Daten["All songs"] = dict(songs_list)
# with open('trackssss.json', 'w', encoding='utf-8') as json_file:
#     json.dump(python_Daten, json_file, ensure_ascii=False, indent=4)

### Time ###
# 0.2261
# 0.2231
# 0.2144
# 0.3231
# 0.2729
# 0.2188
# mean = 0.246 seconds



################# Selection sort #################
def selection_sort(array):
    start = time.time()
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j][0] < array[min_index][0]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    end = time.time()
    return array , end - start

# print(selection_sort(songs_list))
# print(len(songs_list))

### Time ###
# 219.3923
# 222.3272
# 226.0901
# 228.7292
# 218.5491
# 224.1195
# mean = 223.201 seconds 



################################################# search algorithms


################# linear search #################
def linearSearch(array, key):
    start = time.time()
    for i in range(len(array)):
        if array[i][0] == key:
            time.sleep(1)
            end = time.time()
            return i , end - start
    time.sleep(1)
    end = time.time()
    return i , end - start
# print(quick_sort(songs_list, 0, len(songs_list) - 1))
# print(quick_sort(songs_list, 0, len(songs_list) - 1))
# print(linearSearch(songs_list, "Maite zaitut - 2015"))
# print(linearSearch(songs_list, "Barbincor"))
# print(linearSearch(songs_list, "Me Abraça - Ao Vivo"))
# print(linearSearch(songs_list, "행복하길 바래"))



################# binary search #################

def binarySearch(array, key):
    # start = time.time()
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle][0] == key:
            time.sleep(1)
            end = time.time()
            return middle , #end - start
        elif array[middle][0] < key:
            left = middle + 1
        else:
            right = middle - 1
    time.sleep(1)
    end = time.time()
    return None , #end - start

# start = time.time()
# print(binarySearch(songs_list, "Maite zaitut - 2015"))
# start = time.time()
# print(binarySearch(songs_list, "Barbincor"))
# start = time.time()
# print(binarySearch(songs_list, "Me Abraça - Ao Vivo"))
# start = time.time()
# print(binarySearch(songs_list, "행복하길 바래"))


###### songs are already sorted and both functions are looking for the last song in the song-list #####
# time needed to look for a song in the list:
# songs name: Maite zaitut - 2015
# 0.0068        -       0.0019
# 0.0050        -       0.0015
# 0.0049        -       0.0007
# 0.0064        -       0.0013
# 0.0046        -       0.0017

# songs name: Barbincor
# 0.0077        -       0.0018
# 0.0021        -       0.0012
# 0.0016        -       0.0012
# 0.0016        -       0.0013
# 0.0072        -       0.0014

# songs name: Me Abraça - Ao Vivo
# 0.0110        -       0.0022
# 0.0055        -       0.0011
# 0.0071        -       0.0007
# 0.0048        -       0.0002
# 0.0052        -       0.0012

# songs name: 행복하길 바래
# 0.0107        -       0.0004
# 0.0091        -       0.0017
# 0.0218        -       0.0016
# 0.0107        -       0.0010
# 0.0106        -       0.0014


