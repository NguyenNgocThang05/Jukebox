import tkinter as tk
import track_library as lib

current_playlist = []

def create_track_list_clicked(input, output):
    output.delete(1.0, tk.END) # Clear previous message

    track_number = input.get().strip()
    input.delete(0, tk.END) # Clear the empy entry field after getting input

    if not track_number:
        output.insert(tk.END, "Error: Please enter a track number.")
        return

    if track_number in lib.library:
        current_playlist.append(track_number)

        display_text = ""
        for inputted_number in current_playlist:
            track_name = lib.get_name(inputted_number)
            track_artist = lib.get_artist(inputted_number)
            track_rating = lib.get_rating(inputted_number)
            display_text += f"- {track_name} - {track_artist} - Rating: {track_rating}\n"
        output.insert(tk.END, display_text)
    else:
        output.insert(tk.END, f"Error: Track number '{track_number}' is not valid.")


def play_track_list(output):
    # output.delete(1.0, tk.END)

    if not current_playlist:
        output.insert(tk.END, "Playlist is empty. Add tracks first.")
        return

    for inputted_number in current_playlist:
        lib.increment_play_count(inputted_number)

def reset_playlist(output):
    output.delete(1.0, tk.END)
    global current_playlist
    current_playlist = []