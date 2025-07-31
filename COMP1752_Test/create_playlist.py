import customtkinter as ctk
import track_library as lib
import theme_manager as theme


class CreatePlaylist:
    def __init__(self, parent):
        self.parent = parent
        self.playlists = {"Main Playlist": []}  # Dictionary to store playlists
        self.current_playlist = "Main Playlist"

        # Widget variables
        self.input_txt = None
        self.list_txt = None
        self.status_lbl = None
        self.play_btn = None
        self.reset_btn = None
        self.playlist_var = None
        self.playlist_menu = None

        self.create_widgets()
        self.update_track_list_display()

    def create_widgets(self):
        # Track number label
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        # Track number entry
        self.input_txt = ctk.CTkEntry(self.parent, width=60)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        # Add button
        add_btn = ctk.CTkButton(self.parent, text="Add", command=self.add_track, corner_radius=10)
        add_btn.grid(row=0, column=2, padx=5, pady=5)

        # Playlist display textbox
        self.list_txt = ctk.CTkTextbox(self.parent, width=480, height=240, state="disabled")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

        # Frame to group action buttons
        button_frame = ctk.CTkFrame(self.parent)
        button_frame.grid(row=1, column=2, padx=5, pady=5, sticky="n")

        # Play button
        play_btn = ctk.CTkButton(button_frame, text="Play", command=self.play_playlist, corner_radius=10, fg_color="green")
        play_btn.pack(pady=5)

        # Reset button
        reset_btn = ctk.CTkButton(button_frame, text="Reset", command=self.reset_playlist, corner_radius=10, fg_color="red")
        reset_btn.pack(pady=5)

        # Create new playlist button
        new_btn = ctk.CTkButton(button_frame, text="New Playlist", command=self.create_new_playlist, corner_radius=10)
        new_btn.pack(pady=5)

        # Dropdown menu for playlists
        self.playlist_var = ctk.StringVar(value=self.current_playlist)
        self.playlist_menu = ctk.CTkOptionMenu(button_frame, variable=self.playlist_var, values=list(self.playlists.keys()), command=self.select_playlist,corner_radius=10)
        self.playlist_menu.pack(pady=5)

        # Status label
        self.status_lbl = ctk.CTkLabel(self.parent, text="")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="w", padx=5, pady=5)

    def add_track(self):
        key = self.input_txt.get().strip()
        name = lib.get_name(key)
        playlist = self.playlists[self.current_playlist]

        if key:
            if name is not None:
                playlist.append(key)
                self.update_track_list_display()
                self.input_txt.delete(0, ctk.END)
                self.status_lbl.configure(text=f"Track {key} added to {self.current_playlist}")
            else:
                self.status_lbl.configure(text=f"Error: Track {key} not found")
        else:
            self.status_lbl.configure(text="Please enter a track number")

    def update_track_list_display(self):
        self.list_txt.configure(state="normal")
        self.list_txt.delete("1.0", ctk.END)
        playlist = self.playlists[self.current_playlist]

        if not playlist:
            self.list_txt.insert("1.0", "Playlist is empty")
        else:
            display_text = f"{self.current_playlist}:\n\n"
            for i, key in enumerate(playlist, 1):
                name = lib.get_name(key)
                display_text += f"{i}. {name} (ID: {key})\n"
            self.list_txt.insert("1.0", display_text)

        self.list_txt.configure(state="disabled")

    def play_playlist(self):
        playlist = self.playlists[self.current_playlist]
        if not playlist:
            self.status_lbl.configure(text="Playlist is empty")
            return

        for key in playlist:
            lib.increment_play_count(key)

        lib.update_library()
        self.status_lbl.configure(text=f"Playing {self.current_playlist}")

    def reset_playlist(self):
        self.playlists[self.current_playlist] = []
        self.update_track_list_display()
        self.status_lbl.configure(text=f"{self.current_playlist} has been reset")

    def select_playlist(self, choice):
        self.current_playlist = choice
        self.update_track_list_display()
        self.status_lbl.configure(text=f"Selected playlist: {choice}")

    def create_new_playlist(self):
        dialog = ctk.CTkInputDialog(text="Enter new playlist name:", title="Create Playlist")
        playlist_name = dialog.get_input()

        if playlist_name and playlist_name not in self.playlists:
            self.playlists[playlist_name] = []
            self.current_playlist = playlist_name
            self.playlist_menu.configure(values=list(self.playlists.keys()))
            self.playlist_var.set(playlist_name)
            self.update_track_list_display()
            self.status_lbl.configure(text=f"Created new playlist: {playlist_name}")
        elif playlist_name in self.playlists:
            self.status_lbl.configure(text="Playlist name already exists!")


if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    CreatePlaylist(window)
    window.mainloop()