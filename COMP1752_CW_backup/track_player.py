# track_player.py
import tkinter as tk

import font_manager as fonts
import status_message as status # Import the status manager
from view_tracks import TrackViewer
from create_track_list import CreateTrackList
from update_tracks import UpdateTracks

# Function to open View Tracks window
def open_view_tracks_window():
    view_window = tk.Toplevel(window)
    TrackViewer(view_window)
    status.StatusManager.update_status("View Tracks window opened.")

# Function to open Create Track List window
def open_create_track_list_window():
    create_window = tk.Toplevel(window)
    CreateTrackList(create_window)
    status.StatusManager.update_status("Create Track List window opened.")

# Function to open Update Tracks window
def open_update_tracks_window():
    update_window = tk.Toplevel(window)
    UpdateTracks(update_window)
    status.StatusManager.update_status("Update Tracks window opened.")

window = tk.Tk()
window.geometry("920x180") # Adjusted height to accommodate status label better
window.title("JukeBox Main Menu")
window.configure(bg="black") # Consistent background color

# Configure fonts globally first
fonts.configure()
styles = fonts.get_styles() # Get the configured styles

header_lbl = tk.Label(window,
                      text="Select an option by clicking one of the buttons below",
                      font=styles["title"]["font"], # Use a style from font_manager
                      fg=styles["title"]["fg"],
                      bg=styles["title"]["bg"])
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons for opening feature windows
view_tracks_btn = tk.Button(window,
                            text="View Tracks",
                            command=open_view_tracks_window,
                            font=styles["button"]["font"],
                            fg=styles["button"]["fg"],
                            bg=styles["button"]["bg"])
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window,
                                 text="Create Track List",
                                 command=open_create_track_list_window,
                                 font=styles["button"]["font"],
                                 fg=styles["button"]["fg"],
                                 bg=styles["button"]["bg"])
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window,
                             text="Update Tracks",
                             command=open_update_tracks_window,
                             font=styles["button"]["font"],
                             fg=styles["button"]["fg"],
                             bg=styles["button"]["bg"])
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

# Status Label for the main window
status_lbl = tk.Label(window,
                      bg=styles["status"]["bg"],
                      fg=styles["status"]["fg"],
                      text="Ready",
                      font=styles["status"]["font"],
                      bd=1, relief="sunken", anchor="w") # Added border and anchor for better appearance
status_lbl.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

# Initialize the StatusManager with the main window's status label
status.StatusManager.set_label_widget(status_lbl)

window.mainloop()