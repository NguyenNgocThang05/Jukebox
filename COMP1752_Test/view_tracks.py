import customtkinter as ctk     # Import the CustomerTkinter as ctk
import track_library as lib     # Import the track_library as lib
import theme_manager as theme   # Import the theme_manager as theme

# Define a class for the GUI components that handles viewing track information
class TrackViewer:
    def __init__(self, parent):
        self.parent = parent            # Store reference to the parent container (usually the main window)
        self.input_txt = None           # User entry field placeholder
        self.list_txt = None            # Textbox placeholder to display all tracks in the library
        self.track_txt = None           # Textbox placeholder to display info for a specific track
        self.status_lbl = None          # Placeholder for the status label at the bottom
        self.create_widgets()           # Call function to create all GUI components
        self.list_tracks_clicked()      # Automatically display the track list when the app starts

    # This function creates and arranges all the widgets in the GUI
    def create_widgets(self):
        # List Tracks button
        list_btn = ctk.CTkButton(self.parent, text="List All Tracks", command=self.list_tracks_clicked, corner_radius=10)
        list_btn.grid(row=0, column=0, padx=5, pady=5)

        # Track number label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=1, padx=5, pady=5)

        # Track number entry
        self.input_txt = ctk.CTkEntry(self.parent, width=60)
        self.input_txt.grid(row=0, column=2, padx=5, pady=5)

        # View Track button
        view_btn = ctk.CTkButton(self.parent, text="View Track", command=self.view_tracks_clicked, corner_radius=10)
        view_btn.grid(row=0, column=3, padx=5, pady=5)

        # Main content: text box for listing all tracks
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        # Text box for showing details of a specific track
        self.track_txt = ctk.CTkTextbox(self.parent, width=210, height=100, state="disabled")
        self.track_txt.grid(row=1, column=3, sticky="nw", padx=5, pady=5)

        # Status label
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    # This function is triggered when the view track button is clicked
    def view_tracks_clicked(self):
        self.status_lbl.configure(text="View Tracks was clicked!")  # Update the status message
        key = self.input_txt.get().strip()  # Get the entered track number and remove white spaces

        self.track_txt.configure(state="normal")    # Enable text box for writing
        self.track_txt.delete("1.0", ctk.END)   # Clear previous content

        if not key:
            self.status_lbl.configure(text="Please enter a track number") # Informs the user if input is empty
        else:
            name = lib.get_name(key) # Fetch track name by key
            if name:  # If the track exists
                artist = lib.get_artist(key)            # Get artist name
                rating = lib.get_rating(key)            # Get rating
                play_count = lib.get_play_count(key)    # Get play count
                # Display all info in the track detail text box
                self.track_txt.insert("1.0", f"{name}\n{artist}\nRating: {rating}\nPlays: {play_count}")
            else:
                self.status_lbl.configure(text=f"Track {key} not found") # If key is invalid

        self.track_txt.configure(state="disabled") # Disable text box to prevent the user from editing

    # This method is triggered when List all tracks is clicked
    def list_tracks_clicked(self):
        self.status_lbl.configure(text="List track was clicked!")   # Update status message
        self.list_txt.configure(state="normal")     # Enable the list text box
        track_list = lib.list_all()                 # Get the full list of tracks from the library
        self.list_txt.delete("1.0", ctk.END)        # Clear any existing text
        self.list_txt.insert("1.0", track_list)     # Insert the updated track list
        self.list_txt.configure(state="disabled")   # Disable it to prevent the user from editing

if __name__ == "__main__":  # Only runs when this file is run as a standalone
    window = ctk.CTk()      # Create the main app window
    theme.configure()       # Apply the theme
    TrackViewer(window)     # Open the TrackViewer GUI
    window.mainloop()       # Run the window main loop
