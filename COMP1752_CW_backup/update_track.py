import tkinter as tk
import font_manager as fonts
import track_library as lib

class UpdateTracks:
    def __init__(self, window):
        window.geometry("630x250")
        window.title("Update Tracks")

        update_lbl = tk.Label(window, text="Enter Track Number")
        update_lbl.grid(row=0 ,column=0, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        enter_btn = tk.Button(window, text="Enter", command=self.show_track_info)
        enter_btn.grid(row=0, column=2, padx=10, pady=10)


        self.list_txt = tk.Listbox(window, width=30, height=2, bg="white")
        self.list_txt.grid(row=1, column=0,padx=10, pady=10)

        update_btn = tk.Button(window, text="Update", command=self.update_track_clicked)
        update_btn.grid(row=1, column=1, padx=10, pady=10)

        option_lbl = tk.Label(window, text="Choose a new rating:")
        option_lbl.grid(row=2, column=0)

        # Frame to hold radio buttons
        radio_frame = tk.Frame(window)
        radio_frame.grid(row=3, column=0, columnspan=3, pady=10)

        self.selected_option = tk.StringVar(value="1")

        radio_btn1 = tk.Radiobutton(radio_frame, text="1", variable=self.selected_option, value="1")
        radio_btn1.grid(row=0, column=0, padx=5)

        radio_btn2 = tk.Radiobutton(radio_frame, text="2", variable=self.selected_option, value="2")
        radio_btn2.grid(row=0, column=1, padx=5)

        radio_btn3 = tk.Radiobutton(radio_frame, text="3", variable=self.selected_option, value="3")
        radio_btn3.grid(row=0, column=2, padx=5)

        radio_btn4 = tk.Radiobutton(radio_frame, text="4", variable=self.selected_option, value="4")
        radio_btn4.grid(row=0, column=3, padx=5)

        radio_btn5 = tk.Radiobutton(radio_frame, text="5", variable=self.selected_option, value="5")
        radio_btn5.grid(row=0, column=4, padx=5)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="w", padx=10, pady=10)

    def show_track_info(self):
        key = self.input_txt.get().strip()
        self.list_txt.delete(0, tk.END)

        if not key:
            self.status_lbl.configure(text="Please enter a track number")
            return

        name = lib.get_name(key)

        if name:
            self.list_txt.insert(tk.END, f"Track {key}: {name}")
        else:
            self.status_lbl.configure(text=f"Track {key} not found")


    def update_track_clicked(self):
        key = self.input_txt.get().strip()
        new_rating = self.selected_option.get()
        name = lib.get_name(key)

        if not key:
            self.status_lbl.configure(text="Please enter a track number")
            return 

        if name is None:
            self.status_lbl.configure(text=f"Error: Track {key} not found")
            return

        try:
            rating_value = int(new_rating)
            if not (1 <= rating_value <= 5):
                self.status_lbl.configure(text="Error: Rating must be between 1 and 5")
                return

            lib.set_rating(key, rating_value)
            self.status_lbl.configure(text=f"Track {key} rating updated to {rating_value} star(s)")
            lib.set_rating(key, rating_value)

            self.show_track_info()

        except ValueError:
            self.status_lbl.configure(text="Error: Invalid rating value")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTracks(window)
    window.mainloop()