import tkinter as tk
import track_library as lib
import status_message as status

def view_tracks_clicked(input, output):
    """
    :param input: get the user input
    :param output: output will be display in the listbox
    """

    output.delete(1.0, tk.END)
    key = input.get()

    if not key:
        status.StatusManager.update_message("Error: Please enter a track number to view.")
        return

    song_name = lib.get_name(key)

    if song_name:
        song_name = lib.get_name(key)
        artist = lib.get_artist(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        track_details = f"{song_name}\n{artist}\nRating: {rating}\nPlays: {play_count}"
        output.insert(tk.END, track_details)
        status.StatusManager.update_message(f"View tracks was clicked!")
    else:
        status.StatusManager.update_message(f"Error: Track number '{key}' not found.")


def list_tracks_clicked(output):
    output.delete(1.0, tk.END)
    all_tracks = lib.list_all()
    output.insert(tk.END, all_tracks)
    status.StatusManager.update_message("List Tracks was clicked!")