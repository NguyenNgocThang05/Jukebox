import customtkinter as ctk
from view_tracks import TrackViewer
from create_playlist import CreatePlaylist
from update_track import UpdateTracks
import theme_manager as theme
theme.configure()

window = ctk.CTk()
window.title("Jukebox")
window.geometry("800x410")

notebook = ctk.CTkTabview(window)
notebook.pack(expand=True, fill="both")

tab1 = notebook.add("View Tracks")
tab2 = notebook.add("Create Playlist")
tab3 = notebook.add("Update Tracks")

TrackViewer(tab1)
CreatePlaylist(tab2)
UpdateTracks(tab3)

window.mainloop()