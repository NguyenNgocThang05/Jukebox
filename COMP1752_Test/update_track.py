import customtkinter as ctk     # Import CustomTkinter as ctk
import track_library as lib     # Import track_library as lib
import theme_manager as theme   # Import theme_manager as theme


class UpdateTracks:
    # Defines a GUI class for updating the ratings for tracks
    def __init__(self, parent):
        self.parent = parent            # Reference to the parent container (usually the main window)
        self.list_txt = None
        self.input_txt = None           # Entry widget for track number
        self.track_display = None       # Textbox to display found track name
        self.selected_option = None     # Variable to store selected rating
        self.status_lbl = None          # Label to display status message
        self.create_widgets()           # Create and layout all widgets
        self.list_track()

    def create_widgets(self):
        # Creates and positions all widgets

        # Main textbox (left side - 70% width)
        self.list_txt = ctk.CTkTextbox(self.parent, width=400, height=300, state="disabled")
        self.list_txt.grid(row=0, column=0, rowspan=5, padx=(10, 5), pady=10, sticky="nsew")

        # Right side controls (30% width) - no frames used
        ctk.CTkLabel(self.parent, text="Track ID:").grid(row=0, column=1, padx=5, pady=3, sticky="e")
        self.input_txt = ctk.CTkEntry(self.parent, width=80)
        self.input_txt.grid(row=0, column=2, padx=5, pady=3, sticky="w")

        find_btn = ctk.CTkButton(self.parent, text="Find", width=60, command=self.show_track_info)
        find_btn.grid(row=0, column=3, padx=(0, 10), pady=3)

        # Track display (compact)
        self.track_display = ctk.CTkTextbox(self.parent, height=40, width=180, state="disabled")
        self.track_display.grid(row=1, column=1, columnspan=3, padx=10, pady=3, sticky="ew")

        # Rating controls
        rating_lbl = ctk.CTkLabel(self.parent, text="New rating:")
        rating_lbl.grid(row=2, column=1, padx=5, pady=3, sticky="e")

        # Frame to hold the radio buttons tightly together
        rating_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        rating_frame.grid(row=2, column=2, columnspan=3, padx=5, pady=(2, 8), sticky="w")

        # Rating variable and radio buttons
        self.selected_option = ctk.StringVar(value="1")

        for i in range(5):
            ctk.CTkRadioButton(
                rating_frame,
                text=str(i + 1),
                variable=self.selected_option,
                value=str(i + 1),
                width=20
            ).pack(side="left", padx=4, pady=2)

        # Update button
        update_btn = ctk.CTkButton(self.parent,
                                   text="Update",
                                   width=20,
                                   fg_color="green",
                                   command=self.update_track_clicked)
        update_btn.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Status label at bottom
        self.status_lbl = ctk.CTkLabel(self.parent, text="", height=20)
        self.status_lbl.grid(row=5, column=0, padx=20, sticky="w")

    def list_track(self):
        # This method display all the tracks in the library
        self.list_txt.configure(state="normal")
        track_list = lib.list_all()
        self.list_txt.delete("1.0", ctk.END)
        self.list_txt.insert("1.0", track_list)
        self.list_txt.configure(state="disabled")

    def show_track_info(self):
        # Shows the track name when Find button is clicked
        key = self.input_txt.get().strip() # Get the track number input and remove white spaces

        self.track_display.configure(state="normal")  # Enables textbox for writing
        self.track_display.delete("1.0", ctk.END)  # Clear any previous text
        if not key:
            self.status_lbl.configure(text="Please enter a track number")   # Informs the user if the input is empty
        else:
            name = lib.get_name(key)  # Get the name of the track by ID
            if name: # If the track exists
                self.track_display.insert("1.0", f"{key}: {name}") # Get track
                self.status_lbl.configure(text="Find button was clicked!")
            else:
                self.status_lbl.configure(text=f"Track {key} not found") # Prints a message if the track does not exist

        self.track_display.configure(state="disabled") # Disable editing

    def update_track_clicked(self):
        # Called when the Update button is clicked

        key = self.input_txt.get().strip()  # Get the track number input and remove white spaces
        if not key:
            self.status_lbl.configure(text="Please enter a track number") # Informs the user if input is empty
            return

        name = lib.get_name(key)
        if not name:
            self.status_lbl.configure(text=f"Track {key} not found") # Show error message if the track doesn't exist
            return

        try:
            new_rating = int(self.selected_option.get()) # Get selected rating as integer
            lib.set_rating(key, new_rating) # Update the track's rating
            lib.update_library() # Save changes to CSV
            self.show_track_info()  # Refresh the display info after a new input
            self.list_track()
            self.status_lbl.configure(text=f"Updated {name} to {new_rating} stars") # Shows success message
        except ValueError:
            self.status_lbl.configure(text="Invalid rating value") # If the rating isn't a valid number


if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    UpdateTracks(window)
    window.mainloop()