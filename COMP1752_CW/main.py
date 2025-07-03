import tkinter as tk
from tkinter import ttk
import font_manager as fonts

from view_tracks import TrackViewer
from create_tracks import CreateTracks
from update_track import UpdateTracks

window = tk.Tk()
window.title("Jukebox")
window.geometry("800x400")

fonts.configure()

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

tab1 = tk.Frame(notebook, bg="#121212")
tab2 = tk.Frame(notebook, bg="#121212")
tab3 = tk.Frame(notebook, bg="#121212")

notebook.add(tab1, text="View Tracks")
notebook.add(tab2, text="Create Playlist")
notebook.add(tab3, text="Update Tracks")

TrackViewer(tab1)
CreateTracks(tab2)
UpdateTracks(tab3)

window.mainloop()