import tkinter as tk
import track_library as lib
import status_message as status

current_playlist = []

def create_track_list_clicked(input, output):
    output.delete(1.0, tk.END) # Clear previous message

    track_number = input.get().strip()
    input.delete(0, tk.END) # Clear the empy entry field after getting input

    if not track_number:
        status.StatusManager.update_message("Error: Please enter a track number to add.")
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
        status.StatusManager.update_message(f"Track '{track_number}' added to your playlist.")
    else:
        status.StatusManager.update_message(f"Error: Track number '{track_number}' is not valid")


def play_track_list():

    if not current_playlist:
        status.StatusManager.update_message("Playlist is empty. Add tracks first to play")
        return

    for inputted_number in current_playlist:
        lib.increment_play_count(inputted_number)
    status.StatusManager.update_message("Playlist is now playing.")

def reset_playlist(output):
    output.delete(1.0, tk.END)
    global current_playlist
    current_playlist = []
    status.StatusManager.update_message("Playlist has been reset.")