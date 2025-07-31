import customtkinter as ctk                     # Import CustomTkinter as ctk
from view_tracks import TrackViewer             # Import TrackViewer class from view_tracks
from create_playlist import CreatePlaylist      # Import CreatePlaylist class from create_playlist
from update_track import UpdateTracks           # Import UpdateTracks class from update_track
import theme_manager as theme                   # Import theme manager as theme

theme.configure() # Apply the theme and appearance

window = ctk.CTk()          # Create the main app window
window.title("Jukebox")     # Set the window title
window.geometry("730x410")  # Set the window size

tab = ctk.CTkTabview(window)            # Create a tab view container
tab.pack(expand=True, fill="both")      # Expand to fill the window

# Create three tabs and assign each one to a different feature
tab1 = tab.add("View Tracks")           # Tab for viewing all tracks
tab2 = tab.add("Create Playlist")       # Tab for making a custom playlist
tab3 = tab.add("Update Tracks")         # Tab for updating a track's rating

TrackViewer(tab1)       # Place the TrackViewer UI inside the first tab
CreatePlaylist(tab2)    # Place the CreatePlayList UI inside the second tab
UpdateTracks(tab3)      # Place the UpdateTracks UI inside the third tab

window.mainloop()   # Starts the app and keeps the app running