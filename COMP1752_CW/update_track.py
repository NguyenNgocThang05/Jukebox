import customtkinter as ctk     # Import CustomTkinter as ctk
import track_library as lib     # Import track_library as lib
import theme_manager as theme   # Import theme_manager as theme


class UpdateTracks:
    # Defines a GUI class for updating the ratings for tracks
    def __init__(self, parent):
        self.parent = parent            # Reference to the parent container (usually the main window)
        self.input_txt = None           # Entry widget for track number
        self.track_display = None       # Textbox to display found track name
        self.selected_option = None     # Variable to store selected rating
        self.status_lbl = None          # Label to display status message
        self.create_widgets()           # Create and layout all widgets

    def create_widgets(self):
        # Creates and positions all widgets

        # Track number input label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        # Track number input entry field
        self.input_txt = ctk.CTkEntry(self.parent, width=50)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        # Find button to search for the track
        find_btn = ctk.CTkButton(self.parent, text="Find", command=self.show_track_info, width=60, corner_radius=5)
        find_btn.grid(row=0, column=2, padx=5, pady=5)

        # Display box to show track name
        self.track_display = ctk.CTkTextbox(self.parent, width=200, height=50, corner_radius=5, state="disabled")
        self.track_display.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Update button to apply the new rating
        update_btn = ctk.CTkButton(self.parent, text="Update", command=self.update_track_clicked, width=80, corner_radius=5)
        update_btn.grid(row=1, column=2, padx=5, pady=5)

        # Rating selection label
        rating_label = ctk.CTkLabel(self.parent, text="New Rating:")
        rating_label.grid(row=2, column=0, padx=5, pady=5)

        # Create a variable to store selected rating (default is 1)
        self.selected_option = ctk.StringVar(value="1")
        # Create 5 radio buttons for selecting a rating from 1 to 5
        for i in range(5):
            ctk.CTkRadioButton(self.parent, text=str(i + 1), variable=self.selected_option, value=str(i + 1)).grid(
                row=2, column=i + 1, padx=2, pady=5)

        # Status label
        self.status_lbl = ctk.CTkLabel(self.parent, text="", height=20)
        self.status_lbl.grid(row=3, column=0, columnspan=6, sticky="w", padx=5, pady=5)

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
            self.status_lbl.configure(text=f"Updated {name} to {new_rating} stars") # Shows success message
        except ValueError:
            self.status_lbl.configure(text="Invalid rating value") # If the rating isn't a valid number


if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    UpdateTracks(window)
    window.mainloop()