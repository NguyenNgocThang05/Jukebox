import customtkinter as ctk
import track_library as lib
import theme_manager as theme


class CreatePlaylist:
    def __init__(self, parent):
        self.parent = parent                    # Reference to the parent container (usually the main window)
        self.playlists = {"Main Playlist": []}  # Dictionary to store playlists, starting with the default one
        self.current_playlist = "Main Playlist" # Set the currently active playlist to the default
        self.input_txt = None                   # User entry field placeholder
        self.list_txt = None                    # Textbox to display all tracks
        self.status_lbl = None                  # Label to display status message
        self.playlist_var = None                # StringVar to hold the currently selected playlist in the dropdown menu
        self.playlist_menu = None               # Placeholder for the dropdown menu (OptionMenu) widget
        self.create_widgets()                   # Create and layout all widgets
        self.update_track_list_display()        # Automatically calls out the function when the app starts

    def create_widgets(self):
        # Track number label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        # Track number entry
        self.input_txt = ctk.CTkEntry(self.parent, width=60)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        # Add button
        add_btn = ctk.CTkButton(self.parent, text="Add", command=self.add_track, corner_radius=10)
        add_btn.grid(row=0, column=2, padx=5, pady=5)

        # Playlist display textbox
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Frame to group action buttons
        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        # Play button
        play_btn = ctk.CTkButton(button_frame, text="Play", command=self.play_playlist, corner_radius=10, fg_color="green")
        play_btn.pack(pady=5)

        # Reset button
        reset_btn = ctk.CTkButton(button_frame, text="Reset", command=self.reset_playlist, corner_radius=10, fg_color="red")
        reset_btn.pack(pady=5)

        # Create new playlist button
        new_btn = ctk.CTkButton(button_frame, text="New Playlist", command=self.create_new_playlist, corner_radius=10)
        new_btn.pack(pady=5)

        # Dropdown menu for playlists
        self.playlist_var = ctk.StringVar(value=self.current_playlist) # Initial value for the current playlist
        self.playlist_menu = ctk.CTkOptionMenu(button_frame, variable=self.playlist_var, values=list(self.playlists.keys()), command=self.select_playlist, corner_radius=10)
        self.playlist_menu.pack(pady=5)

        # Status label
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    # This function will add a track to a playlist
    def add_track(self):
        key = self.input_txt.get().strip() # Get the user input and remove white spaces
        name = lib.get_name(key) # Get track name from the library using the key input from user
        playlist = self.playlists[self.current_playlist] # Get currently selected playlist

        if key: # If the input is not empty
            if name is not None: # If the track exists in the library
                playlist.append(key) # Add track to the playlist
                self.update_track_list_display() # Refresh the display to show the new track
                self.input_txt.delete(0, ctk.END) # Clear the input field
                self.status_lbl.configure(text=f"Track {key} added to {self.current_playlist}") # Shows success message
            else:
                self.status_lbl.configure(text=f"Error: Track {key} not found") # Informs the user if the track doesn't exist in the library
        else:
            self.status_lbl.configure(text="Please enter a track number") # Informs the user if the input is empty

    # This function updates the textbox display
    def update_track_list_display(self):
        self.list_txt.configure(state="normal") # Enable textbox editing
        self.list_txt.delete("1.0", ctk.END) # Clear any existing text
        playlist = self.playlists[self.current_playlist] # Get the current playlist

        if not playlist:
            self.list_txt.insert("1.0", "Playlist is empty") # Informs the user if the playlist has no tracks
        else:
            display_text = f"{self.current_playlist}:\n\n" # Header showing playlist name
            for i, key in enumerate(playlist, 1): # Loop through playlist and display each track
                name = lib.get_name(key)
                display_text += f"{i}. {name} (ID: {key})\n"
            self.list_txt.insert("1.0", display_text) # Insert the full display string

        self.list_txt.configure(state="disabled") # Disable textbox to prevent user editing

    # This function plays the song by incrementing the play count by 1
    def play_playlist(self):
        playlist = self.playlists[self.current_playlist] # Get the current playlist
        if not playlist:
            self.status_lbl.configure(text="Playlist is empty") # Informs the user if the playlist is empty
            return

        for key in playlist:# Loops though each in the playlist
            lib.increment_play_count(key)  # The play count of the track will be incremented by 1

        lib.update_library() # Updates and saves in the CSV file
        self.status_lbl.configure(text=f"Playing {self.current_playlist}") # Inform the user that playlist is playing

    # This function clears all the tracks in a playlist
    def reset_playlist(self):
        self.playlists[self.current_playlist] = [] # Clear all tracks from the current playlist
        self.update_track_list_display() # Refresh display
        self.status_lbl.configure(text=f"{self.current_playlist} has been reset") # Notify the user

    # This function lets the user pick different playlists
    def select_playlist(self, choice):
        self.current_playlist = choice # Change the active playlist to the one selected from the dropdown menu
        self.update_track_list_display() # Refresh display for new playlist
        self.status_lbl.configure(text=f"Selected playlist: {choice}") # Show the success message

    # This function will pop a small window to let the user create a new playlist
    def create_new_playlist(self):
        dialog = ctk.CTkInputDialog(text="Enter new playlist name:", title="Create Playlist") # User prompt to input playlist name
        playlist_name = dialog.get_input() # Get the inputted name

        if playlist_name and playlist_name not in self.playlists: # If it's a valid and unique name
            self.playlists[playlist_name] = [] # Add new playlist to dictionary
            self.current_playlist = playlist_name # Set is as the active playlist
            self.playlist_menu.configure(values=list(self.playlists.keys())) # Update the dropdown options
            self.playlist_var.set(playlist_name) # Update the dropdown to show the new playlist
            self.update_track_list_display() # Refresh the display
            self.status_lbl.configure(text=f"Created new playlist: {playlist_name}") # Shows a success message
        elif playlist_name in self.playlists: # If the playlist already exists
            self.status_lbl.configure(text="Playlist name already exists!") # Show error message


if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    CreatePlaylist(window)
    window.mainloop()