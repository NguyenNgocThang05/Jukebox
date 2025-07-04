import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    """
    Defines a helper function named "set_text" to update the content of a Tkinter text and scrolled text widget
    "text_area" is the Tkinter text widget to be updated
    "content" is the string that will be inserted into the text area
    """
    text_area.delete("1.0", tk.END)
    """
    Deletes all existing content from the "text_area" widget
    "1.0" refers to the first character of the first line
    tk.END refers to the end of the text
    """
    text_area.insert(1.0, content)
    """
    Inserts the "content" string into the "text_area" widget, starting at "1.0" (beginning)
    """


class TrackViewer:
    """
    Defines a class named "TrackViewer", which creates the GUI elements and logic for view tracks
    """
    def __init__(self, parent):
        """
        The constructor method for the "TrackViewer" class
        "self" is an instance of the class being created
        "parent" is a frame that will contain this viewer
        """
        self.tab1_interface(parent)
        # Calls the "tab1_interface" method, passing the "parent" widget
        # This method is responsible for creating and laying out the GUI elements

    def tab1_interface(self, frame):
        """
        Defines a method named "tab1_interface" which sets up the user interface elements within a given "frame"
        "frame" is the Tkinter widget (Ex: Tk.Frame) where the widgets will be placed
        """

        # List All Tracks button
        list_tracks_btn = tk.Button(frame, text="List All Tracks",bg="#888888", fg="white", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Enter Track Number label
        enter_lbl = tk.Label(frame, text="Enter Track Number",bg="#888888", fg="white")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # User Entry Field
        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # View Track button
        view_track_btn = tk.Button(frame, text="View Track",bg="#888888", fg="white", command=self.view_tracks_clicked)
        view_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Scrolled Text widget under List All Tracks button
        self.list_txt = tkst.ScrolledText(frame,bg="#888888", fg="white", width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget under View Track button
        self.track_txt = tk.Text(frame,bg="#888888", fg="white", width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(frame, text="", bg="#444444", fg="white")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)


    def view_tracks_clicked(self):
        """
        Defines a method that is called when the "View Track" button is clicked
        """
        key = self.input_txt.get().strip() # Retrieves the text entered from the user
        name = lib.get_name(key) # Calls the "get_name" functon to get the track's name using entered key
        if name is not None:
            # Checks if a track with the given key was found
            artist = lib.get_artist(key) # Retrieves the artist of the track
            rating = lib.get_rating(key) # Retrieves the rating of the track
            play_count = lib.get_play_count(key) # Retrieves the play count of the track
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}" # Formats the retrieved track details into a string
            set_text(self.track_txt, track_details) # Calls the "set_text" function to display the track details in the text widget
            self.status_lbl.configure(text="View Track button was clicked!") # Updates the status label to notify the user
        else:
            # If name is None (track not found)
            self.status_lbl.configure(text="Track not found")
            # Updates the status label to notify the user

    def list_tracks_clicked(self):
        """
        Defines a method that is called when  the "List All Tracks" button is clicked
        """

        track_list = lib.list_all() # Calls the "list_all" function from the track_library to get all tracks
        set_text(self.list_txt, track_list) # Calls the "set_text" function to display the "track_list" in the scrolled text widget
        self.status_lbl.configure(text="List Tracks button was clicked!") # Updates the status label

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
