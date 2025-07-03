import tkinter as tk
import tkinter.scrolledtext as tkst

import  track_library as lib
import font_manager as fonts

class CreateTracks:
    def __init__(self, parent):
        self.tab2_interface(parent)

    def tab2_interface(self, frame):

        self.playlist = []

        enter_lbl = tk.Label(frame, text="Enter Track Number")
        enter_lbl.grid(row=0 ,column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(frame, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        create_tracks_btn = tk.Button(frame, text="Add", command=self.create_tracks_clicked)
        create_tracks_btn.grid(row=0, column=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(frame, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # Frame to stack Play and Reset button together in row=1, column=2
        button_frame = tk.Frame(frame)
        button_frame.grid(row=1, column=2, padx=(0, 10), pady=(10, 10), sticky="n")

        self.play_btn = tk.Button(button_frame, text="Play", command=self.play_track_list)
        self.play_btn.grid(row=0, column=0, pady=(0, 2))

        self.reset_btn = tk.Button(button_frame, text="Reset", command=self.reset_playlist)
        self.reset_btn.grid(row=1, column=0, pady=(0, 0))


        self.status_lbl = tk.Label(frame, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=10, pady=10)

    def create_tracks_clicked(self):
        key = self.input_txt.get().strip()
        if key:
            if lib.get_name(key) is not None:
                self.playlist.append(key)
                self.update_track_list_display()
                self.input_txt.delete(0, tk.END)
                self.status_lbl.configure(text=f"Track {key} added to playlist")
            else:
                self.status_lbl.configure(text=f"Error: Track {key} not found in library")
        else:
            self.status_lbl.configure(text="Please enter a track number")


    def update_track_list_display(self):
        self.list_txt.delete(1.0, tk.END)
        if not self.playlist:
            return

        display_text = "Play List:\n"
        for i, key in enumerate(self.playlist):
            name = lib.get_name(key)
            if name:
                display_text += f"{i+1}. {name}\n"
        self.list_txt.insert(1.0, display_text)


    def play_track_list(self):
        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty. Add tracks before playing")
            return

        for key in self.playlist:
            lib.increment_play_count(key)

        # Save updated play counts to the CSV file
        lib.update_library()
        self.status_lbl.configure(text="Playlist is now playing")


    def reset_playlist(self):
        self.playlist = []
        self.update_track_list_display()
        self.status_lbl.configure(text="Playlist has been reset")

if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateTracks(window)
    window.mainloop()

