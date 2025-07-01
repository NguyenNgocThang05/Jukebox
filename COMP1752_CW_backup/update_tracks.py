# update_tracks.py
import tkinter as tk
import tkinter.messagebox # For displaying messages

import track_library as lib
import font_manager as fonts
import status_message as status # Import the status manager

class UpdateTracks:
    def __init__(self, window):
        self.window = window # Store reference to the Toplevel window
        window.geometry("450x250")
        window.title("Update Track Rating")
        window.configure(bg="black") # Add background color for consistency

        styles = fonts.get_styles()
        label_style = styles["label"]
        button_style = styles["button"]
        entry_style = styles["entry"]

        # Frame for track number input
        track_input_frame = tk.Frame(window, bg="#c5f0c5")
        track_input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        tk.Label(track_input_frame,
                 text="Enter Track Number:",
                 font=label_style["font"],
                 fg=label_style["fg"],
                 bg=label_style["bg"]).grid(row=0, column=0, sticky="w")

        self.update_entry = tk.Entry(track_input_frame, width=10,
                                     font=entry_style["font"],
                                     fg=entry_style["fg"],
                                     bg=entry_style["bg"])
        self.update_entry.grid(row=0, column=1, sticky="w", padx=5)

        # Frame for New Rating and Radio Buttons
        rating_frame = tk.Frame(window, bg="#c5f0c5")
        rating_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        tk.Label(rating_frame,
                 text="New Rating:",
                 font=label_style["font"],
                 fg=label_style["fg"],
                 bg=label_style["bg"]).grid(row=0, column=0, sticky="w")

        # Sub-frame for radio buttons for neat alignment
        radio_button_sub_frame = tk.Frame(rating_frame, bg="#c5f0c5")
        radio_button_sub_frame.grid(row=0, column=1, sticky="w")

        self.selected_option = tk.StringVar()
        self.selected_option.set("1") # Set a default selected option

        for i in range(1, 6):
            radio_button = tk.Radiobutton(radio_button_sub_frame,
                                          text=str(i),
                                          variable=self.selected_option,
                                          value=str(i),
                                          font=label_style["font"], # Use label style for radio buttons
                                          fg=label_style["fg"],
                                          bg=label_style["bg"],
                                          selectcolor="light green") # Color when selected
            radio_button.pack(side="left", padx=2, pady=2)


        # Update Button
        update_button = tk.Button(window,
                                  text="Update Rating",
                                  command=self.update_rating_clicked,
                                  font=button_style["font"],
                                  fg=button_style["fg"],
                                  bg=button_style["bg"])
        update_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def update_rating_clicked(self):
        track_key = self.update_entry.get().strip()
        new_rating = self.selected_option.get()

        if not track_key:
            status.StatusManager.update_status("Please enter a track number.")
            tkinter.messagebox.showwarning("Input Error", "Please enter a track number.")
            return

        if lib.get_name(track_key) is None:
            status.StatusManager.update_status(f"Error: Track {track_key} not found.")
            tkinter.messagebox.showerror("Track Not Found", f"Track number {track_key} does not exist.")
            return

        try:
            rating_value = int(new_rating)
            if not (1 <= rating_value <= 5):
                status.StatusManager.update_status("Error: Rating must be between 1 and 5.")
                tkinter.messagebox.showwarning("Input Error", "Rating must be an integer between 1 and 5.")
                return

            lib.set_rating(track_key, rating_value)
            status.StatusManager.update_status(f"Track {track_key} rating updated to {rating_value}.")
            tkinter.messagebox.showinfo("Success", f"Rating for '{lib.get_name(track_key)}' updated to {rating_value} stars.")
        except ValueError:
            status.StatusManager.update_status("Error: Invalid rating value.")
            tkinter.messagebox.showwarning("Input Error", "Invalid rating value. Please select a rating.")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    # In standalone mode, we create a dummy status label for testing
    temp_status_label = tk.Label(window, text="", bd=1, relief="sunken", anchor="w")
    temp_status_label.grid(row=3, column=0, columnspan=2, sticky="ew") # Adjust row for placement
    status.StatusManager.set_label_widget(temp_status_label)
    UpdateTracks(window)
    window.mainloop()