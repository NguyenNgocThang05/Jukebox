import customtkinter as ctk     # Import the customer tkinter as ctk
import  track_library as lib    # import the track_library as lib
import theme_manager as theme   # Import the theme_manager as theme


class CreatePlaylist:
    # Defines the GUI class for creating and managing a playlist
    def __init__(self, parent):
        self.parent = parent        # Store reference to the parent container (usually the window)
        self.playlist = []          # Initialize an empty list to store track keys added to the playlist
        self.input_txt = None       # Placeholder for the track number input entry
        self.list_txt = None        # Placeholder for the playlist display textbox
        self.status_lbl = None      # Placeholder for the status message label
        self.play_btn = None        # Placeholder for the Play button
        self.reset_btn = None       # Placeholder for the Reset button
        self.create_widgets()       # Call method to create and layout all GUI components

    def create_widgets(self):
        # Creates and positions all widgets

        # Track number label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        # Track number entry
        self.input_txt = ctk.CTkEntry(self.parent, width=60)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        # Add button
        add_btn = ctk.CTkButton(self.parent, text="Add", command=self.create_tracks_clicked, corner_radius=10)
        add_btn.grid(row=0, column=2, padx=5, pady=5)

        # Playlist display textbox (read only)
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Frame to group Play and Reset button
        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        # Play button
        self.play_btn = ctk.CTkButton(button_frame, text="Play", command=self.play_track_list, corner_radius=10)
        self.play_btn.pack(pady=5)

        # Reset button
        self.reset_btn = ctk.CTkButton(button_frame, text="Reset", command=self.reset_playlist, corner_radius=10)
        self.reset_btn.pack(pady=5)

        # Status bar
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    def create_tracks_clicked(self):
        # This method is called when the Add button is clicked

        key = self.input_txt.get().strip()  # Get the input and remove white spaces from the entry field
        if key:
            if lib.get_name(key) is not None:   # Check if the track exists
                self.playlist.append(key)           # Add track key to the playlist
                self.update_track_list_display()    # Refresh the display
                self.input_txt.delete(0, ctk.END)   # Clear the input field
                self.status_lbl.configure(text=f"Track {key} added to playlist") # Shows success message
            else:
                self.status_lbl.configure(text=f"Error: Track {key} not found in library")  # Error if track doesn't exist
        else:
            self.status_lbl.configure(text="Please enter a track number")   # Prompt if no input

    def update_track_list_display(self):
        # Updates the text box to display all tracks currently in the playlist

        self.list_txt.configure(state="normal") # Enable text box for writing
        self.list_txt.delete("1.0", ctk.END)    # Clear previous content
        if not self.playlist:
            return  # If playlist is empty, stop here

        display_text = "Play List:\n" # Header for playlist display
        for i, key in enumerate(self.playlist):     # Loop through all added track keys
            name = lib.get_name(key)    # Get track name
            if name:
                display_text += f"{i + 1}. {name} | Track ID: {key}\n"    # Add numbered track name to the playlist
        self.list_txt.insert("1.0", display_text)       # Show the full playlist in the text box
        self.list_txt.configure(state="disabled")       # Disable the textbox to prevent the user from editing

    def play_track_list(self):
        # Simulates playing the playlist and updates play counts

        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty. Add tracks before playing")
            return  # Exits if no tracks are in the playlist

        for key in self.playlist:
            lib.increment_play_count(key)   # Increase play count for each track

        lib.update_library()    # Save the updated play counts to the CSV file
        self.status_lbl.configure(text="Playlist is now playing")   # Show the success message

    def reset_playlist(self):
        # Clears the playlist and updates the display

        self.playlist = [] # Clear the list of track keys
        self.update_track_list_display() # Clear the display box
        self.status_lbl.configure(text="Playlist has been reset") # Informs the user

if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    CreatePlaylist(window)
    window.mainloop()

