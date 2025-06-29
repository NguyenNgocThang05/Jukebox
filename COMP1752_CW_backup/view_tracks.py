import tkinter as tk
import track_library as lib

def view_tracks_clicked(input, output):
    """
    :param input: get the user input
    :param output: output will be display in the listbox
    """

    output.delete(1.0, tk.END)
    key = input.get()

    song_name = lib.get_name(key)
    artist = lib.get_artist(key)
    rating = lib.get_rating(key)
    play_count = lib.get_play_count(key)
    track_details = f"{song_name}\n{artist}\nRating: {rating}\nPlays: {play_count}"

    if song_name and artist:
        output.insert(tk.END, track_details)
    else:
        output(tk.END, "Track not found.")

def list_tracks_clicked(output):
    output.delete(1.0, tk.END)
    all_tracks = lib.list_all()
    output.insert(tk.END, all_tracks)