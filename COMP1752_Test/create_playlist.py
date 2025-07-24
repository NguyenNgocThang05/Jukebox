import customtkinter as ctk
import  track_library as lib
import theme_manager as theme


class CreatePlaylist:
    def __init__(self, parent):
        self.parent = parent
        self.playlist = []
        self.input_txt = None
        self.list_txt = None
        self.status_lbl = None
        self.play_btn = None
        self.reset_btn = None
        self.create_widgets()

    def create_widgets(self):
        # Track number label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        # Track number entry
        self.input_txt = ctk.CTkEntry(self.parent, width=60)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        # Add button
        add_btn = ctk.CTkButton(self.parent, text="Add", command=self.create_tracks_clicked, corner_radius=10)
        add_btn.grid(row=0, column=2, padx=5, pady=5)

        # Playlist display
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Action buttons
        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        self.play_btn = ctk.CTkButton(button_frame, text="Play", command=self.play_track_list, corner_radius=10)
        self.play_btn.pack(pady=5)

        self.reset_btn = ctk.CTkButton(button_frame, text="Reset", command=self.reset_playlist, corner_radius=10)
        self.reset_btn.pack(pady=5)

        # Status bar
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    def create_tracks_clicked(self):
        key = self.input_txt.get().strip()
        if key:
            if lib.get_name(key) is not None:
                self.playlist.append(key)
                self.update_track_list_display()
                self.input_txt.delete(0, ctk.END)
                self.status_lbl.configure(text=f"Track {key} added to playlist")
            else:
                self.status_lbl.configure(text=f"Error: Track {key} not found in library")
        else:
            self.status_lbl.configure(text="Please enter a track number")

    def update_track_list_display(self):
        self.list_txt.configure(state="normal")
        self.list_txt.delete("1.0", ctk.END)
        if not self.playlist:
            return

        display_text = "Play List:\n"
        for i, key in enumerate(self.playlist):
            name = lib.get_name(key)
            if name:
                display_text += f"{i + 1}. {name}\n"
        self.list_txt.insert("1.0", display_text)
        self.list_txt.configure(state="disabled")

    def play_track_list(self):
        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty. Add tracks before playing")
            return

        for key in self.playlist:
            lib.increment_play_count(key)

        lib.update_library()
        self.status_lbl.configure(text="Playlist is now playing")

    def reset_playlist(self):
        self.playlist = []
        self.update_track_list_display()
        self.status_lbl.configure(text="Playlist has been reset")

if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    CreatePlaylist(window)
    window.mainloop()

