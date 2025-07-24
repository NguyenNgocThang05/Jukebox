import customtkinter as ctk
import track_library as lib
import theme_manager as theme


class TrackViewer:
    def __init__(self, parent):
        self.parent = parent
        self.input_txt = None
        self.list_txt = None
        self.track_txt = None
        self.status_lbl = None
        self.create_widgets()
        self.list_tracks_clicked()

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

        # Main content
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self.track_txt = ctk.CTkTextbox(self.parent, width=240, height=100, state="disabled")
        self.track_txt.grid(row=1, column=3, sticky="nw", padx=5, pady=5)

        # Status bar
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    def view_tracks_clicked(self):
        key = self.input_txt.get().strip()

        self.track_txt.configure(state="normal")
        self.track_txt.delete("1.0", ctk.END)

        if not key:
            self.status_lbl.configure(text="Please enter a track number")
        else:
            name = lib.get_name(key)
            if name:
                artist = lib.get_artist(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                self.track_txt.insert("1.0", f"{name}\n{artist}\nRating: {rating}\nPlays: {play_count}")
            else:
                self.track_txt.insert("1.0", f"Track {key} not found")

        self.track_txt.configure(state="disabled")

    def list_tracks_clicked(self):
        self.list_txt.configure(state="normal")
        track_list = lib.list_all()
        self.list_txt.delete("1.0", ctk.END)
        self.list_txt.insert("1.0", track_list)
        self.list_txt.configure(state="disabled")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = ctk.CTk()        # create a TK object
    theme.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
