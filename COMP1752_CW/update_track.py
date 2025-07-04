import tkinter as tk
import font_manager as fonts
import track_library as lib

class UpdateTracks:
    """
    Defines a class named "UpdateTracks" which is responsible for the GUI and logic
    to update a track's rating
    """
    def __init__(self, parent):
        """
        The constructor method for the "UpdateTrack" class
        "self" refers to the instance of the class being created
        "parent" is a frame that will contain this interface
        """
        self.tab3_interface(parent) # Calls the "tab3_interface" method, passing the "parent" widget, to set up the GUI elements

    def tab3_interface(self, frame):
        """
        Defines a method named "tab3_interface" which sets up the user interface within given "frame"
        "frame" is the Tkinter widget (Ex: Tk.Frame) where the widgets will be laid out
        """

        # Enter Track Number label
        update_lbl = tk.Label(frame, text="Enter Track Number", bg="#888888", fg="white")
        update_lbl.grid(row=0 ,column=0, padx=10, pady=10)

        # User Entry Field
        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # Enter button
        enter_btn = tk.Button(frame, text="Enter",bg="#888888", fg="white", command=self.show_track_info)
        enter_btn.grid(row=0, column=2, padx=10, pady=10)

        # Listbox widget
        self.list_txt = tk.Listbox(frame,bg="#888888", fg="white", width=50, height=2)
        self.list_txt.grid(row=1, column=0,padx=10, pady=10)

        # Update button
        update_btn = tk.Button(frame, text="Update",bg="#888888", fg="white", command=self.update_track_clicked)
        update_btn.grid(row=1, column=1, padx=10, pady=10)



        # Frame to hold radio buttons
        radio_frame = tk.Frame(frame, bg="#444444")
        radio_frame.grid(row=3, column=0, columnspan=3, pady=10)

        # Choose a new rating label
        option_lbl = tk.Label(radio_frame,bg="#888888", fg="white", text="Choose a new rating:")
        option_lbl.grid(row=0, column=0)

        # Set default rating to 1
        self.selected_option = tk.StringVar(value="1")

        # Rating 1 button
        radio_btn1 = tk.Radiobutton(radio_frame, text="1", bg="#888888", fg="white",selectcolor="#888888", variable=self.selected_option, value="1")
        radio_btn1.grid(row=0, column=1, padx=5)

        # Rating 2 button
        radio_btn2 = tk.Radiobutton(radio_frame, text="2",bg="#888888", fg="white",selectcolor="#888888", variable=self.selected_option, value="2")
        radio_btn2.grid(row=0, column=2, padx=5)

        # Rating 3 button
        radio_btn3 = tk.Radiobutton(radio_frame, text="3",bg="#888888", fg="white",selectcolor="#888888", variable=self.selected_option, value="3")
        radio_btn3.grid(row=0, column=3, padx=5)

        # Rating 4 button
        radio_btn4 = tk.Radiobutton(radio_frame, text="4",bg="#888888", fg="white",selectcolor="#888888", variable=self.selected_option, value="4")
        radio_btn4.grid(row=0, column=4, padx=5)

        # Rating 5 button
        radio_btn5 = tk.Radiobutton(radio_frame, text="5",bg="#888888", fg="white",selectcolor="#888888", variable=self.selected_option, value="5")
        radio_btn5.grid(row=0, column=5, padx=5)

        # Status label
        self.status_lbl = tk.Label(frame, text="", bg="#444444", fg="white")
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="w", padx=10, pady=10)

    def show_track_info(self):
        """
        Defines a method that is called when the "Enter" button is clicked
        """
        key = self.input_txt.get().strip() # Retrieves the text entered from the user
        self.list_txt.delete(0, tk.END) # Clears all existing tracks from the listbox widget

        if not key:
            # Checks if the "key" (user input) is empty
            self.status_lbl.configure(text="Please enter a track number") # If empty, updates the status to notify the user
            return # Exits the function

        name = lib.get_name(key) # Calls the "get_name" function to return the name of the track based on the user's "key"

        if name is not None:
            # If "name" is not None (meaning a track was found with a given key)
            self.list_txt.insert(tk.END, f"Track {key}: {name}") # Inserts a string into the listbox widget
        else:
            # If "name" is None (track not found)
            self.status_lbl.configure(text=f"Track {key} not found") # Updates the status label to indicate that the track was not found


    def update_track_clicked(self):
        """
        Defines a method that is called when the "Update" button is clicked
        """

        key = self.input_txt.get().strip() # Retrieves the text from the user's input
        new_rating = self.selected_option.get() # Retrieves the value of the current selected radio button
        name = lib.get_name(key) # Retrieves the name of the track using the entered "key" to check if the track exists

        if not key:
            # Checks if the track key input is empty
            self.status_lbl.configure(text="Please enter a track number") # Updates the status label
            return  # Exits the function

        if name is None:
            # Checks if the track based on the "key" was not found
            self.status_lbl.configure(text=f"Error: Track {key} not found") # Updates the status label with an error message
            return # Exits the function

        try:
            # Initialize a try block to handle errors during conversion
            rating_value = int(new_rating) # Converts the "new_rating" to an integer
            if not (1 <= rating_value <= 5):
                # Checks if the "rating_value" is within the range 1 to 5
                self.status_lbl.configure(text="Error: Rating must be between 1 and 5") # Updates the status label with an error message if the rating is out of range
                return # Exits the function

            lib.set_rating(key, rating_value) # Calls the "Set_rating" to set a new rating
            self.status_lbl.configure(text=f"Track {key} rating updated to {rating_value} star(s)") # Updates the status label


            lib.update_library() # Saved updated rating to CSV file

            self.show_track_info() # Calls "show_track_info" again to refresh the display

        except ValueError:
            # Catch a ValueError if "new_rating" cannot be converted to an integer (though this might not be the case for radio buttons)
            self.status_lbl.configure(text="Error: Invalid rating value") # Updates status label with an error message


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)
    window.mainloop()