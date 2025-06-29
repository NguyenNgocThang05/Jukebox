import tkinter as tk
import track_library as lib

def view_tracks_clicked(input, output):
    """
    :param input: get the user input
    :param output: output will be display in the listbox
    """

    output.delete(1.0, tk.END)
    track_key = input.get()

    track_name = lib.get_name(track_key)
    track_artist = lib.get_artist(track_key)

    if track_name and track_artist:
        output.insert(tk.END, f"Track Name: {track_name}\nArtist: {track_artist}")
    else:
        output(tk.END, "Track not found.")