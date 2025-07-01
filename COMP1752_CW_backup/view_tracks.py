# view_tracks.py
import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts
import status_message as status # Import the status manager

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class TrackViewer():
    def __init__(self, window):
        self.window = window # Store reference to the Toplevel window
        window.geometry("750x350")
        window.title("View Tracks")
        window.configure(bg="black") # Add background color for consistency

        styles = fonts.get_styles()
        label_style = styles["label"]
        button_style = styles["button"]

        list_tracks_btn = tk.Button(window,
                                    text="List All Tracks",
                                    command=self.list_tracks_clicked,
                                    font=button_style["font"],
                                    fg=button_style["fg"],
                                    bg=button_style["bg"])
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window,
                             text="Enter Track Number:",
                             font=label_style["font"],
                             fg=label_style["fg"],
                             bg=label_style["bg"])
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window,
                                    text="View Track",
                                    command=self.view_tracks_clicked,
                                    font=button_style["font"],
                                    fg=button_style["fg"],
                                    bg=button_style["bg"])
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none", bg="light yellow")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none", bg="light yellow")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Remove status_lbl from here, as main window will handle status
        # self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        # self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked() # Populate the list on startup

    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
            status.StatusManager.update_status(f"Track {key} details displayed.") # Update main status
        else:
            set_text(self.track_txt, f"Track {key} not found")
            status.StatusManager.update_status(f"Error: Track {key} not found.") # Update main status

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        status.StatusManager.update_status("All tracks listed.") # Update main status

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    # In standalone mode, we create a dummy status label for testing
    temp_status_label = tk.Label(window, text="", bd=1, relief="sunken", anchor="w")
    temp_status_label.grid(row=2, column=0, columnspan=4, sticky="ew")
    status.StatusManager.set_label_widget(temp_status_label)
    TrackViewer(window)
    window.mainloop()