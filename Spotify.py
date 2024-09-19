import json
import re
import time
import forTesting as ft
import timeit


with open('tracks.json', 'r', encoding='utf-8') as json_file:
    python_Daten = json.load(json_file)

all_songs = python_Daten["All songs"]
favorite_songs = python_Daten["Favorite songs"]

all_songs_list  = list(python_Daten["All songs"].items())
favorite_songs_list  = list(python_Daten["Favorite songs"].items())


# print(all_songs.get("Bohemian Rhapsody"))

def show_all_songs():
    len_of_all_songs = len(all_songs_list)
    start_show_songs_indx = 0
    show_songs_indx = 25
    ask_if_sort(all_songs_list, "All songs")
    show_more = True
    while show_more == True:
        for i in range(start_show_songs_indx, show_songs_indx):
            if i >= len(all_songs_list):
                print("")
                print(f"Showed songs: {len_of_all_songs}/{len(all_songs_list)}")
                print("")
                print("✔ all songs are shown")
                return
            if all_songs_list[i][1][4] == True:
                print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                print(f"{i+1}. ❤  {all_songs_list[i][0]}\n    Information: #Artist: {all_songs_list[i][1][0]}  #Genre: {all_songs_list[i][1][1]}  #Album: {all_songs_list[i][1][2]}  #Duration: {all_songs_list[i][1][3]}")
                print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
            else:
                print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                print(f"{i+1}.    {all_songs_list[i][0]}\n    Information: #Artist: {all_songs_list[i][1][0]}  #Genre: {all_songs_list[i][1][1]}  #Album: {all_songs_list[i][1][2]}  #Duration: {all_songs_list[i][1][3]}")
                print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
        start_show_songs_indx = show_songs_indx
        show_songs_indx += 25
        print("")
        print(f"Showed songs: {start_show_songs_indx}/{len_of_all_songs}")
        print("________________________")
        input1 = input("more songs? (y/n): ")
        if input1.lower() == "y":
            show_more = True
        else:
            show_more = False
            get_old_lists(0)

def get_old_lists(all_or_favorite):
    global all_songs_list, favorite_songs_list
    if all_or_favorite == 0:
        all_songs_list  = list(python_Daten["All songs"].items())
    elif all_or_favorite == 1:
        favorite_songs_list  = list(python_Daten["Favorite songs"].items())
    else:
        all_songs_list  = list(python_Daten["All songs"].items())
        favorite_songs_list  = list(python_Daten["Favorite songs"].items())


def show_favorite_songs():
    len_of_favorite = len(favorite_songs_list)
    start_show_songs_indx = 0
    show_songs_indx = 25
    ask_if_sort(favorite_songs_list, "Favorite songs")
    show_more = True
    while show_more == True:
        for i in range(start_show_songs_indx, show_songs_indx):
            if i >= len(favorite_songs_list):
                print("")
                print(f"Showed songs: {len_of_favorite}/{len_of_favorite}")
                print("")
                print("✔ all favorite songs are shown")
                return
            else:
                print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                print(f"{i+1}. ❤  {favorite_songs_list[i][0]}\n    Information: #Artist: {favorite_songs_list[i][1][0]}  #Genre: {favorite_songs_list[i][1][1]}  #Album: {favorite_songs_list[i][1][2]}  #Duration: {favorite_songs_list[i][1][3]}")
                print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
        start_show_songs_indx = show_songs_indx
        show_songs_indx += 25
        print()
        print(f"Showed songs: {start_show_songs_indx}/{len_of_favorite}")
        print("________________________")
        input1 = input("show more favorite songs? (y/n): ")
        if input1.lower() == "y":
            show_more = True
        else:
            show_more = False

def add_new_song():
    new_song = input("Enter the name of the new song: ")
    for song in all_songs_list:
        if song[0] == new_song:
            print("")
            print(f"⚠ This song '{new_song}' already exists")
            return
    new_song_artist = input("Enter the artist of the new song: ")
    new_song_genre = input("Enter the genre of the new song: ")
    new_song_album = input("Enter the name of the album of the new song: ")
    new_song_duration = input("Enter the duration of the new song: ")
    new_song_is_favorite = input("Is the new song a favorite? (y/n): ")
    while new_song_is_favorite.lower() not in ["y", "n"]:
        new_song_is_favorite = input("please enter y or n\nIs the new song a favorite? (y/n): ")
    if new_song_is_favorite.lower() == "y":
        new_song_is_favorite = True
        new_song_to_add = (f"{new_song}",[new_song_artist, new_song_genre, new_song_album, new_song_duration, new_song_is_favorite])
        all_songs_list.append(new_song_to_add)
        favorite_songs_list.append(new_song_to_add)
        update_json_file()
        print("")
        print("✔ New song added")
    else:
        new_song_is_favorite = False
        new_song_to_add = (f"{new_song}",[new_song_artist, new_song_genre, new_song_album, new_song_duration, new_song_is_favorite])
        all_songs_list.append(new_song_to_add)
        update_json_file()
        print("")
        print("✔ New song added")


def update_json_file():
    global all_songs_list, favorite_songs_list
    python_Daten["All songs"] = dict(all_songs_list)
    python_Daten["Favorite songs"] = dict(favorite_songs_list)
    with open('tracks.json', 'w', encoding='utf-8') as json_file:
        json.dump(python_Daten, json_file, ensure_ascii=False, indent=4)

def ask_if_sort(all_songs_or_favorite_songs, type:str):
    global all_songs_list, favorite_songs_list
    with_sort = input("Do you want to sort the songs? (y/n): ")
    if with_sort.lower() == "y":
        while True:
            sort_to_what = input("Sort to what?\n1. Name of the song\n2. Artist\n3. Genre\n4. Album\n5. duration of the song\n")
            if sort_to_what in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("________________________")
                print("Invalid input. Please try again: ")        
        ascending_or_descending = input("Ascending or Descending? (a/d): ")
        while ascending_or_descending.lower() not in ["a","d"]:
            ascending_or_descending = input("please chose Ascending or Descending? (a/d):")
        if sort_to_what == "1":
            if type == "All songs":
                all_songs_list = quick_sort(all_songs_or_favorite_songs, firstNum=0, descending= True if ascending_or_descending.lower() == "d" else False)
            elif type == "Favorite songs":
                favorite_songs_list = quick_sort(all_songs_or_favorite_songs, firstNum=0, descending= True if ascending_or_descending.lower() == "d" else False)
        elif sort_to_what == "2":
            if type == "All songs":
                all_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 0, descending= True if ascending_or_descending.lower() == "d" else False)
            elif type == "Favorite songs":
                favorite_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 0, descending= True if ascending_or_descending.lower() == "d" else False)
        elif sort_to_what == "3":
            if type == "All songs":
                all_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 1, descending= True if ascending_or_descending.lower() == "d" else False)
            elif type == "Favorite songs":
                favorite_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 1, descending= True if ascending_or_descending.lower() == "d" else False)
        elif sort_to_what == "4":
            if type == "All songs":
                all_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 2, descending= True if ascending_or_descending.lower() == "d" else False)
            elif type == "Favorite songs":
                favorite_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 2, descending= True if ascending_or_descending.lower() == "d" else False)
        elif sort_to_what == "5":
            if type == "All songs":
                all_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 3, descending= True if ascending_or_descending.lower() == "d" else False)
            elif type == "Favorite songs":
                favorite_songs_list = quick_sort(all_songs_or_favorite_songs, 1, 3, descending= True if ascending_or_descending.lower() == "d" else False)
    else:
        return

def quick_sort(sequence, firstNum:int, secoundNum:int = None, descending:bool = None):
    length = len(sequence)
    if length <= 1:
        return sequence

    pivot = sequence[-1]
    items_greater = []
    items_lower = []
    
    for item in sequence[:-1]:
        if firstNum == 0:
            if item[0] < pivot[0] if descending else item[0] > pivot[0]:
                items_greater.append(item)
            else:
                items_lower.append(item)
        else:
            if item[firstNum][secoundNum] == pivot[firstNum][secoundNum]:  # If equal, use song name for tie-breaking
                if item[0] > pivot[0]:  # always sort Ascending
                    items_greater.append(item)
                else:
                    items_lower.append(item)
            elif item[firstNum][secoundNum] < pivot[firstNum][secoundNum] if descending else item[firstNum][secoundNum] > pivot[firstNum][secoundNum]:
                items_greater.append(item)
            else:
                items_lower.append(item)
    
    return quick_sort(items_lower, firstNum, secoundNum, descending) + [pivot] + quick_sort(items_greater, firstNum, secoundNum, descending)

def search_song(search_term):
    pattern = re.compile(search_term, re.IGNORECASE)
    search_results = {}
    for song in all_songs_list:
        if pattern.search(song[0]) or any(pattern.search(str(song[1])) for el in song[1]):
            search_results[song[0]] = song[1]
    
    if search_results:
        search_results = list(search_results.items())
        length = len(search_results)
        if length > 10:
            start_show_songs = 0
            end_show_songs = 10
            show_more = True
            while show_more:
                for i in range(start_show_songs, end_show_songs):
                    if i >= length:
                        print("")
                        print(f"Showed songs: {length}/{length}")
                        print("")
                        print("✔ All songs have been shown.")
                        return
                    else:
                        print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                        print(f"{i+1}." + (f"❤  " if search_results[i][1][4] else '  ')+ f"{search_results[i][0]}\n    Information: #Artist: {search_results[i][1][0]}  #Genre: {search_results[i][1][1]}  #Album: {search_results[i][1][2]}  #Duration: {search_results[i][1][3]}")
                        print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
                start_show_songs = end_show_songs
                end_show_songs += 10
                print("")
                print(f"Showed songs: {start_show_songs}/{length}")
                print("____________________________")
                user_input = input("Do you want to see more songs? (y/n): ")
                if user_input.lower() == "y":
                    show_more = True
                else:
                    show_more = False
        else:
            for i in range(length):
                print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                print(f"{i+1}." + (f"❤  " if search_results[i][1][4] else '  ')+ f"{search_results[i][0]}\n    Information: #Artist: {search_results[i][1][0]}  #Genre: {search_results[i][1][1]}  #Album: {search_results[i][1][2]}  #Duration: {search_results[i][1][3]}")
                print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
            print("")
            print(f"Showed songs: {length}/{length}")
    else:
        print("")
        print("⚠ No songs found matching your search.")
            

def binarySearch(array, key, look_just_for_this_song:bool = False, printing:bool = True):
    sorted_list = quick_sort(array,firstNum=0,secoundNum=0,descending=False)
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_list[middle][0] == key:
            if printing:
                print("◣▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼◢")
                print(("❤  " if sorted_list[middle][1][4] else '  ')+ f"{sorted_list[middle][0]}\n    Information: #Artist: {sorted_list[middle][1][0]}  #Genre: {sorted_list[middle][1][1]}  #Album: {sorted_list[middle][1][2]}  #Duration: {sorted_list[middle][1][3]}")
                print("◤▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲◥")
                return sorted_list[middle]
            else:
                return sorted_list[middle]
        elif sorted_list[middle][0] < key:
            left = middle + 1
        else:
            right = middle - 1
    if look_just_for_this_song:
        return False
    else:
        search_song(key)


def remove_song():
    remove_song = input("Enter the name of the song you want to remove: ")
    song_to_remove = binarySearch(all_songs_list, remove_song, True)
    if not song_to_remove:
        print("")
        print("⚠ No such song found")
        return
    elif song_to_remove and song_to_remove[1][4] == True:
        confirmation = input(f"Are you sure you want to remove {remove_song} from all songs and favorite songs? (y/n) ")
        if confirmation.lower() != "y":
            print("")
            print("⚠ The song was not removed")
            return
        else:
            all_songs_list.remove(song_to_remove)
            favorite_songs_list.remove(song_to_remove)
            update_json_file()
            print("")
            print(f"✔ The song '{remove_song}' is removed from the all songs and favorite songs")
    else:
        confirmation = input(f"Are you sure you want to remove {remove_song} from all songs? (y/n) ")
        if confirmation.lower() != "y":
            print("")
            print("⚠ The song was not removed")
            return
        else:
            all_songs_list.remove(song_to_remove)
            update_json_file()
            print("")
            print(f"✔ The song '{remove_song}' is removed from the all songs")

def edit_song():
    edit_song = input("Which song would you like to edit?")
    song_to_edit = binarySearch(all_songs_list, edit_song, True)
    if not song_to_edit:
        print("")
        print("⚠ No such song found")
    else:
        if song_to_edit[1][4] == True:
            add_or_remove = "remove from favorite"
        else:
            add_or_remove = "add to favorite"
        edit_input = input(f"What would you like to edit in the song information?\n1. Name of the song\n2. Artist\n3. Genre\n4. Album\n5. Duration\n6. {add_or_remove}\n0. Cancel\n")
        if edit_input == "1":
            new_name = input("Enter new name: ")
            edited_song = (new_name, song_to_edit[1])
            all_songs_list.append(edited_song)
            all_songs_list.remove(song_to_edit)
            if song_to_edit[1][4]:
                favorite_songs_list.append(edited_song)
                favorite_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "2":
            new_artist = input("Enter new artist: ")
            edited_song = (song_to_edit[0], [new_artist, song_to_edit[1][1], song_to_edit[1][2], song_to_edit[1][3], song_to_edit[1][4]])
            all_songs_list.append(edited_song)
            all_songs_list.remove(song_to_edit)
            if song_to_edit[1][4]:
                favorite_songs_list.append(edited_song)
                favorite_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "3":
            new_genre = input("Enter new genre: ")
            edited_song = (song_to_edit[0], [song_to_edit[1][0], new_genre, song_to_edit[1][2], song_to_edit[1][3], song_to_edit[1][4]])
            all_songs_list.append(edited_song)
            all_songs_list.remove(song_to_edit)
            if song_to_edit[1][4]:
                favorite_songs_list.append(edited_song)
                favorite_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "4":
            new_album = input("Enter new album name: ")
            edited_song = (song_to_edit[0], [song_to_edit[1][0], song_to_edit[1][1], new_album, song_to_edit[1][3], song_to_edit[1][4]])
            all_songs_list.append(edited_song)
            all_songs_list.remove(song_to_edit)
            if song_to_edit[1][4]:
                favorite_songs_list.append(edited_song)
                favorite_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "5":
            new_duration = input("Enter new duration: ")
            edited_song = (song_to_edit[0], [song_to_edit[1][0], song_to_edit[1][1], song_to_edit[1][2], new_duration, song_to_edit[1][4]])
            all_songs_list.append(edited_song)
            all_songs_list.remove(song_to_edit)
            if song_to_edit[1][4]:
                favorite_songs_list.append(edited_song)
                favorite_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "6":
            if song_to_edit[1][4]:
                edited_song = (song_to_edit[0], [song_to_edit[1][0], song_to_edit[1][1], song_to_edit[1][2], song_to_edit[1][3], False])
                favorite_songs_list.remove(song_to_edit)
                all_songs_list.append(edited_song)
                all_songs_list.remove(song_to_edit)
            else:
                edited_song = (song_to_edit[0], [song_to_edit[1][0], song_to_edit[1][1], song_to_edit[1][2], song_to_edit[1][3], True])
                favorite_songs_list.append(edited_song)
                all_songs_list.append(edited_song)
                all_songs_list.remove(song_to_edit)
            update_json_file()
            print("")
            print("✔ Edited")
        elif edit_input == "0":
            return
        

def clear_all_favorite_songs():
    for song in favorite_songs_list:
        song_name = song[0]
        song_Tuple = binarySearch(all_songs_list, song_name, True, False)
        edited_song = (song_Tuple[0], [song_Tuple[1][0], song_Tuple[1][1], song_Tuple[1][2], song_Tuple[1][3], False])
        all_songs_list.append(edited_song)
        all_songs_list.remove(song_Tuple)
    favorite_songs_list.clear()
    update_json_file()

def add_a_song_to_favorite_songs():
    song_to_favorite = input("Enter the name of the song you want to add to favorite songs: ")
    song_Tuple = binarySearch(all_songs_list, song_to_favorite, True, True)
    if song_Tuple[1][4]:
        print("")
        print("⚠ The song is already in favorite songs")
    else:
        edited_song = (song_Tuple[0], [song_Tuple[1][0], song_Tuple[1][1], song_Tuple[1][2], song_Tuple[1][3], True])
        all_songs_list.append(edited_song)
        all_songs_list.remove(song_Tuple)
        favorite_songs_list.append(edited_song)
        update_json_file()
        print("")
        print(f"✔ The song '{song_to_favorite}' is added to favorite songs")

def remove_a_song_from_favorite_songs():
    song_to_remove = input("Enter the name of the song you want to remove from favorite songs: ")
    song_Tuple = binarySearch(all_songs_list, song_to_remove, True, True)
    if not song_Tuple[1][4]:
        print("")
        print("⚠ The song is not in favorite songs")
    else:
        edited_song = (song_Tuple[0], [song_Tuple[1][0], song_Tuple[1][1], song_Tuple[1][2], song_Tuple[1][3], False])
        all_songs_list.append(edited_song)
        all_songs_list.remove(song_Tuple)
        favorite_songs_list.remove(song_Tuple)
        update_json_file()
        print("")
        print(f"✔ The song '{song_to_remove}' is removed from favorite songs")

def development_menu():
    pass

user_input = None
while user_input != 0:
    print("__________________________\n__________________________")
    user_input = input("Main menu:\n1. All songs\n2. Favorite songs\n3. Add new song\n4. Remove song\n5. More options\n0. Exit\n")

    if user_input == "1":
        user_input = None
        while user_input in ["1", "2", "0", None]:
            print("__________________________\n__________________________")
            user_input = input("1. Show all songs\n2. Search for a song\n0. Back to main menu\n")
            if user_input == "1":
                print("__________________________")
                print("All songs:")
                show_all_songs()
            elif user_input == "2":
                print("__________________________")
                what_song = input("Enter the name of the song you want to search: ")
                binarySearch(all_songs_list, what_song)
            elif user_input == "0":
                break
            else:
                user_input = None
                print("__________________________")
                print("Invalid input. Please try again: ")
            
    elif user_input == "2":
        user_input = None
        while user_input in ["1", "2", "3", "4", "0", None]:
            print("__________________________\n__________________________")
            user_input = input("1. Show all favorite songs\n2. Add a song to favorite songs\n3. Remove a song from favorite songs\n4. Clear all favorite songs\n0. Back to main menu\n")
            if user_input == "1":
                if len(favorite_songs) == 0:
                    print("No favorite songs")
                else:
                    print("__________________________")
                    print("Favorite songs:")
                    show_favorite_songs()
            elif user_input == "2":
                add_a_song_to_favorite_songs()
            elif user_input == "3":
                if len(favorite_songs) == 0:
                    print("No favorite songs")
                else:
                    remove_a_song_from_favorite_songs()
            elif user_input == "4":
                if len(favorite_songs) == 0:
                    print("No favorite songs")
                else:   
                    confirm = input("Are you sure you want to clear all favorite songs? (y/n): ")
                    if confirm.lower() == "y":
                        clear_all_favorite_songs()
                        print("All favorite songs cleared")
                    else:
                        print("Canceled")
            elif user_input == "0":
                break
            else:
                user_input = None
                print("__________________________")
                print("Invalid input. Please try again: ")

    elif user_input == "3":
        add_new_song()

    elif user_input == "4":
        remove_song()

    elif user_input == "5":
        user_input = None
        while user_input in ["1", "2", "0", None]:
            print("__________________________\n__________________________")
            user_input = input("1. Edit a song\n2. Development World\n0. Back to main menu\n")

            if user_input == "1":
                edit_song()

            elif user_input == "2":
                user_input = None
                while user_input in ["1", "2", "0", None]:
                    print("__________________________\n__________________________")
                    user_input = input("Development menu:\n1. Sort algorithm testing\n2. Search algorithm testing\n0. Back to main menu\n")

                    if user_input == "1":
                        user_input = None
                        while user_input in ["1", "2", "3", "4", "5", "0", None]:
                            print("__________________________\n__________________________")
                            print("Sort algorithm testing:")
                            user_input = input("1. Bubble Sort\n2. Insertion Sort\n3. Quick Sort\n4. Merge Sort\n5. Selection Sort\n0. Back to main menu\n")

                            if user_input == "1":
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.bubble_sort(all_songs_list), number=1)
                                print(f"Bubble sort took {my_time:.6f} seconds to complete")

                            elif user_input == "2":
                                print("__________________________")
                                estimated_time = timeit.timeit(lambda: ft.insertion_sort(all_songs_list), number=1)
                                print(f"Insertion sort took {estimated_time:.6f} seconds to complete")

                            elif user_input == "3":
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.quick_sort(all_songs_list), number=1)
                                print(f"Quick sort took {my_time:.6f} seconds to complete")

                            elif user_input == "4":
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.merge_sort(all_songs_list), number=1)
                                print(f"Merge sort took {my_time:.6f} seconds to complete")	

                            elif user_input == "5":
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.selection_sort(all_songs_list), number=1)
                                print(f"Selection sort took {my_time:.6f} seconds to complete")

                            elif user_input == "0":
                                break
                            else:
                                user_input = None
                                print("__________________________")
                                print("Invalid input. Please try again: ")

                    elif user_input == "2":
                        user_input = None
                        while user_input in ["1", "2", "0", None]:
                            print("__________________________\n__________________________")
                            print("Search algorithm testing:")
                            user_input = input("1. Linear Search\n2. Binary Search\n0. Back to main menu\n")
                            
                            if user_input == "1":
                                what_song = input("Enter the name of the song you want to search: ")
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.linearSearch(all_songs_list, what_song), number=1)
                                print(f"Linear search took {my_time:.6f} seconds to complete")

                            elif user_input == "2":
                                print("__________________________")
                                print("⚠ for your information: for this Search algorithm the list has to be sorted first ⚠\nTherefore the list will be sorted alphabetically with 'Quick Sort' as this is the most quick and efficient sort algorithm\n-----> The time for sorting is not included in the binary search time")
                                what_song = input("Enter the name of the song you want to search: ")
                                sorted_new_array = ft.quick_sort(all_songs_list)
                                print("__________________________")
                                my_time = timeit.timeit(lambda: ft.binarySearch(sorted_new_array, what_song), number=1)
                                print(f"Binary search took {my_time:.6f} seconds to complete")

                            elif user_input == "0":
                                break
                            else:
                                user_input = None
                                print("__________________________")
                                print("Invalid input. Please try again: ")

                    elif user_input == "0":
                        break
                    else:
                        user_input = None
                        print("__________________________")
                        print("Invalid input. Please try again: ")
            elif user_input == "0":
                break
            else:
                user_input = None
                print("__________________________")
                print("Invalid input. Please try again: ")
        
    elif user_input == "0":
        break
    else:
        print("Invalid input")
