import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class TrackViewer:
    def __init__(self, parent):
        self.tab1_interface(parent)

    def tab1_interface(self, frame):

        list_tracks_btn = tk.Button(frame, text="List All Tracks",bg="#888888", fg="white", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(frame, text="Enter Track Number",bg="#888888", fg="white")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(frame, text="View Track",bg="#888888", fg="white", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(frame,bg="#888888", fg="white", width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(frame,bg="#888888", fg="white", width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(frame, text="", bg="#444444", fg="white")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get().strip()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
            self.status_lbl.configure(text="View Track button was clicked!")
        else:
            self.status_lbl.configure(text="Track not found")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
