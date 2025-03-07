'''
Do not use AI! You can schedule to try again if you have a bad grade!
You are building a music playlist system. Write a function named 'manage_playlist' which receives 3 paramenters: a
list of song names, a new song name to be added to the end of the playlist, and a song name to be searched in the
playlist. It should return the index of the searched song in the updated playlist (or None if the song is not found).

Example:
playlist = ['Dream On', 'Bohemian Rhapsody', 'Stairway to Heaven']
print(manage_playlist(playlist, 'Hotel California', 'Bohemian Rhapsody'))  # Output: 1
print(playlist)  # Output: ['Dream On', 'Bohemian Rhapsody', 'Stairway to Heaven', 'Hotel California']

playlist = ['Imagine', 'Confortably Numb']
print(manage_playlist(playlist, 'Wish You Were Here', 'Wish You Were Here'))  # Output: 2
print(playlist)  # Output: ['Imagine', 'Confortably Numb', 'Wish You Were Here']

playlist = ['Imagine', 'Confortably Numb']
print(manage_playlist(playlist, 'Wish You Were Here', 'Smoking on the Water'))  # Output: None
print(playlist)  # Output: ['Imagine', 'Confortably Numb', 'Wish You Were Here']
'''
def manage_playlist(playlist, new_song, search_song):
    playlist.append(new_song)
    for i in range(len(playlist)):
        if playlist[i] == search_song:
            return i
    return None

playlist = ['Dream On', 'Bohemian Rhapsody', 'Stairway to Heaven']
print(manage_playlist(playlist, 'Hotel California', 'Bohemian Rhapsody'))  # Output: 1
print(playlist)  # Output: ['Dream On', 'Bohemian Rhapsody', 'Stairway to Heaven', 'Hotel California']

playlist = ['Imagine', 'Confortably Numb']
print(manage_playlist(playlist, 'Wish You Were Here', 'Wish You Were Here'))  # Output: 2
print(playlist)  # Output: ['Imagine', 'Confortably Numb', 'Wish You Were Here']

playlist = ['Imagine', 'Confortably Numb']
print(manage_playlist(playlist, 'Wish You Were Here', 'Smoking on the Water'))  # Output: None
print(playlist)  # Output: ['Imagine', 'Confortably Numb', 'Wish You Were Here']