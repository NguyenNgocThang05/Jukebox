import tkinter as tk
import tkinter.scrolledtext as tkst

import  track_library as lib
import font_manager as fonts

class CreateTracks:
    """
    Defines a class named "CreateTracks" which is responsible for the GUI and logic
    to create and manage a playlist of tracks
    """
    def __init__(self, parent):
        """
        The constructor method for the "CreateTracks" class
        "self" refers to the instance of the class being created
        "parent" is a frame that will contain this interface
        """
        self.tab2_interface(parent) # Calls the "tab2_interface" method, passing the "parent" widget, to set up the GUI elements

    def tab2_interface(self, frame):
        """
        Defines a method named "tab2_interface" which sets up the user interface within given "frame"
        "frame" is the Tkinter widget (Ex: Tk.Frame) where the widgets will be laid out
        """

        self.playlist = [] # Initialize an empty list named "playlist" as an instance variable
                           # This will store tracks that is added into the playlist

        # Enter Track Number Label
        enter_lbl = tk.Label(frame, text="Enter Track Number", bg="#888888", fg="white")
        enter_lbl.grid(row=0 ,column=0, padx=10, pady=10)

        # User Entry Field
        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # Add button to create playlist
        create_tracks_btn = tk.Button(frame, text="Add",bg="#888888", fg="white", command=self.create_tracks_clicked)
        create_tracks_btn.grid(row=0, column=2, padx=10, pady=10)

        # Scrolled Text widget
        self.list_txt = tkst.ScrolledText(frame,bg="#888888", fg="white", width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # Frame to stack Play and Reset button together in row=1, column=2
        button_frame = tk.Frame(frame, bg="#444444")
        button_frame.grid(row=1, column=2, padx=(0, 10), pady=(10, 10), sticky="n")

        # Play button
        self.play_btn = tk.Button(button_frame, text="Play",bg="#888888", fg="white", command=self.play_track_list)
        self.play_btn.grid(row=0, column=0, pady=(0, 2))

        # Reset button
        self.reset_btn = tk.Button(button_frame, text="Reset",bg="#888888", fg="white", command=self.reset_playlist)
        self.reset_btn.grid(row=1, column=0, pady=(0, 0))

        # Status label
        self.status_lbl = tk.Label(frame, text="",bg="#444444", fg="white")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=10)

    def create_tracks_clicked(self):
        """
        Defines a method that is called when the "Add" button is clicked
        """
        key = self.input_txt.get().strip() # Retrieves the text from the user's input
        name  = lib.get_name(key) # Calls the function get_name and assign it to the variable "name"
        if key:
            # Check if the entered "key" is not an empty string
            if name is not None:
                # Check if the track exists
                self.playlist.append(key) # Appends the "key" (track number) to the playlist
                self.update_track_list_display() # Calls 'update_track_list_display()' to refresh the playlist display in the scrolled text widget
                self.input_txt.delete(0, tk.END) # Clears the content of the entry widget
                self.status_lbl.configure(text=f"Track {key} added to playlist") # Updates the label status
            else:
                # If name is None (track not found)
                self.status_lbl.configure(text=f"Error: Track {key} not found in library")
        else:
            # If the "key" (input) is empty
            self.status_lbl.configure(text="Please enter a track number")


    def update_track_list_display(self):
        """
        Defines a method to refresh the content of the playlist display area
        """
        self.list_txt.delete(1.0, tk.END) # Deletes all existing text from scrolled text widget
        if not self.playlist:
            # Checks if the "playlist" is empty
            return # If empty, the function returns, leaving the display blank

        display_text = "Play List:\n" # Initialize a string to build the text that will be displayed in the playlist
        for i, key in enumerate(self.playlist):
            # Loops through the "playlist", getting both the index("i") and the "key" for each track
            name = lib.get_name(key) # Retrieves the name of the track using its key from the "track_library"
            if name:
                # If a name is found (track exists)
                display_text += f"{i+1}. {name} - From track {key}\n" # Appends the track number, name and key to the display
        self.list_txt.insert(1.0, display_text) # Inserts the "display_text" string into the scrolled text widget


    def play_track_list(self):
        """
        Defines a method that is called when the "Play" button is clicked
        """
        if not self.playlist:
            # Checks if the "playlist" is empty
            self.status_lbl.configure(text="Playlist is empty. Add tracks before playing") # Updates status label
            return # Exits the function without doing anything

        for key in self.playlist:
            # Loops through each track "key" in the "playlist"
            lib.increment_play_count(key) # Calls "increment_play_count" function to increase the play count for each track that is in the playlist

        # Save the updated play count to CSV file
        lib.update_library()
        self.status_lbl.configure(text="Playlist is now playing") # Updates the status label


    def reset_playlist(self):
        """
        Defines a method that is called when the "Reset" button is clicked
        """

        self.playlist = [] # Clears the "playlist" by re-assigning it to an empty list
        self.update_track_list_display() # Calls the "update_track_playlist" function to clear the visual display of the playlist
        self.status_lbl.configure(text="Playlist has been reset") # Updates the status label

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTracks(window)
    window.mainloop()