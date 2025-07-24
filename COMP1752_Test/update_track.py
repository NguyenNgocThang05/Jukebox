import customtkinter as ctk
import track_library as lib
import theme_manager as theme


class UpdateTracks:
    def __init__(self, parent):
        self.parent = parent
        self.input_txt = None
        self.track_display = None
        self.selected_option = None
        self.status_lbl = None
        self.create_widgets()

    def create_widgets(self):
        # Track number input
        track_label = ctk.CTkLabel(self.parent, text="Enter track number:")
        track_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_txt = ctk.CTkEntry(self.parent, width=50)
        self.input_txt.grid(row=0, column=1, padx=5, pady=5)

        find_btn = ctk.CTkButton(self.parent, text="Find", command=self.show_track_info, width=60, corner_radius=5)
        find_btn.grid(row=0, column=2, padx=5, pady=5)

        # Track info display
        self.track_display = ctk.CTkTextbox(self.parent, width=200, height=30, corner_radius=5, state="disabled")
        self.track_display.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        update_btn = ctk.CTkButton(self.parent, text="Update", command=self.update_track_clicked, width=80, corner_radius=5)
        update_btn.grid(row=1, column=2, padx=5, pady=5)

        # Rating selection
        rating_label = ctk.CTkLabel(self.parent, text="New Rating:")
        rating_label.grid(row=2, column=0, padx=5, pady=5)

        self.selected_option = ctk.StringVar(value="1")
        for i in range(5):
            ctk.CTkRadioButton(self.parent, text=str(i + 1), variable=self.selected_option, value=str(i + 1)).grid(
                row=2, column=i + 1, padx=2, pady=5)

        # Status message
        self.status_lbl = ctk.CTkLabel(self.parent, text="", height=20)
        self.status_lbl.grid(row=3, column=0, columnspan=6, sticky="w", padx=5, pady=5)

    def show_track_info(self):
        key = self.input_txt.get().strip()
        if not key:
            self.status_lbl.configure(text="Please enter a track number")
            return

        self.track_display.configure(state="normal")
        self.track_display.delete("1.0", ctk.END)

        name = lib.get_name(key)
        display_text = f"{key}: {name}" if name else f"Track {key} not found"
        self.track_display.insert("1.0", display_text)

        self.track_display.configure(state="disabled")

    def update_track_clicked(self):
        key = self.input_txt.get().strip()
        if not key:
            self.status_lbl.configure(text="Please enter a track number")
            return

        name = lib.get_name(key)
        if not name:
            self.status_lbl.configure(text=f"Track {key} not found")
            return

        try:
            new_rating = int(self.selected_option.get())
            lib.set_rating(key, new_rating)
            lib.update_library()
            self.status_lbl.configure(text=f"Updated {name} to {new_rating} stars")
            self.show_track_info()
        except ValueError:
            self.status_lbl.configure(text="Invalid rating value")


if __name__ == "__main__":
    window = ctk.CTk()
    theme.configure()
    UpdateTracks(window)
    window.mainloop()