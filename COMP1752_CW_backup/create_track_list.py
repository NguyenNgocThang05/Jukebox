# create_track_list.py
import tkinter as tk
import tkinter.scrolledtext as tkst

import track_library as lib
import font_manager as fonts
import status_message as status # Import the status manager

class CreateTrackList:
    def __init__(self, window):
        self.window = window # Store reference to the Toplevel window
        window.geometry("600x400")
        window.title("Create Your Track List")
        window.configure(bg="black") # Add background color for consistency

        self.playlist = [] # Store track numbers for the playlist

        styles = fonts.get_styles()
        label_style = styles["label"]
        button_style = styles["button"]

        # Input for adding tracks
        track_input_frame = tk.Frame(window, bg="black")
        track_input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        track_input_frame.grid_columnconfigure(1, weight=1)

        tk.Label(track_input_frame,
                 text="Enter Track Number:",
                 font=label_style["font"],
                 fg=label_style["fg"],
                 bg=label_style["bg"]).grid(row=0, column=0, sticky="w")

        self.track_number_entry = tk.Entry(track_input_frame, width=10)
        self.track_number_entry.grid(row=0, column=1, sticky="w", padx=5)

        add_button = tk.Button(track_input_frame,
                               text="Add to List",
                               command=self.add_track_to_list,
                               font=button_style["font"],
                               fg=button_style["fg"],
                               bg=button_style["bg"])
        add_button.grid(row=0, column=2, sticky="e", padx=5)


        # Display for the current track list
        tk.Label(window,
                 text="Your Current Track List:",
                 font=label_style["font"],
                 fg=label_style["fg"],
                 bg=label_style["bg"]).grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.create_track_text = tkst.ScrolledText(window, bg="light yellow", wrap="word", width=50, height=15)
        self.create_track_text.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        window.grid_rowconfigure(2, weight=1) # Allow text area to expand
        window.grid_columnconfigure(0, weight=1)


        # Control buttons for play and reset
        control_buttons_frame = tk.Frame(window, bg="#c5f0c5")
        control_buttons_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        control_buttons_frame.grid_columnconfigure(0, weight=1) # Allow the first column to expand to push buttons right

        play_button = tk.Button(control_buttons_frame,
                                text="Play Track List",
                                command=self.play_track_list,
                                font=button_style["font"],
                                fg=button_style["fg"],
                                bg=button_style["bg"])
        play_button.grid(row=0, column=1, padx=5, sticky="e")

        reset_button = tk.Button(control_buttons_frame,
                                 text="Reset List",
                                 command=self.reset_playlist,
                                 font=button_style["font"],
                                 fg=button_style["fg"],
                                 bg=button_style["bg"])
        reset_button.grid(row=0, column=2, padx=5, sticky="e")

    def add_track_to_list(self):
        track_key = self.track_number_entry.get().strip()
        if track_key:
            if lib.get_name(track_key) is not None:
                self.playlist.append(track_key)
                self.update_track_list_display()
                self.track_number_entry.delete(0, tk.END)
                status.StatusManager.update_status(f"Track {track_key} added to list.")
            else:
                status.StatusManager.update_status(f"Error: Track {track_key} not found in library.")
        else:
            status.StatusManager.update_status("Please enter a track number.")

    def update_track_list_display(self):
        self.create_track_text.delete(1.0, tk.END)
        if not self.playlist:
            self.create_track_text.insert(1.0, "Your track list is empty.")
            return

        display_text = "Track List:\n"
        for i, key in enumerate(self.playlist):
            name = lib.get_name(key)
            if name:
                display_text += f"{i+1}. {key} - {name}\n"
            else:
                display_text += f"{i+1}. {key} - (Track not found)\n"
        self.create_track_text.insert(1.0, display_text)

    def play_track_list(self):
        if not self.playlist:
            status.StatusManager.update_status("Track list is empty. Add tracks before playing.")
            return

        status.StatusManager.update_status("Playing track list...")
        # Simulate playing by incrementing play counts and displaying
        play_summary = "Playing:\n"
        for key in self.playlist:
            if lib.get_name(key):
                lib.increment_play_count(key)
                play_summary += f"- {lib.get_name(key)} by {lib.get_artist(key)}\n"
            else:
                play_summary += f"- Track {key} (Not found)\n"
        status.StatusManager.update_status(f"Finished playing playlist. {len(self.playlist)} tracks played.")
        tk.messagebox.showinfo("Playback Complete", play_summary) # Use a messagebox for playback info

    def reset_playlist(self):
        self.playlist = []
        self.update_track_list_display()
        status.StatusManager.update_status("Track list reset.")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    # In standalone mode, we create a dummy status label for testing
    temp_status_label = tk.Label(window, text="", bd=1, relief="sunken", anchor="w")
    temp_status_label.grid(row=4, column=0, columnspan=3, sticky="ew") # Adjust row for placement
    status.StatusManager.set_label_widget(temp_status_label)
    CreateTrackList(window)
    window.mainloop()