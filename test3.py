import tkinter as tk

window = tk.Tk()
window.title("Jukebox")
window.geometry("1120x600")

# === Main Frame using grid for consistency ===
main_frame = tk.Frame(window, bg="light pink")
main_frame.grid(row=0, column=0, sticky="nsew")

# Make the main_frame fill the entire window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Configure main_frame's grid layout
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# === Title Label ===
title_label = tk.Label(main_frame, text="Welcome to Jukebox!", font=("Arial", 20), fg="blue", bg="light green")
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# === Left Frame ===
left_frame = tk.Frame(main_frame, bg="light blue", bd=2, relief="groove")
left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# === Right Frame ===
right_frame = tk.Frame(main_frame, bg="light blue", bd=2, relief="groove")
right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

# Configure grid in left_frame to allow resizing
left_frame.grid_rowconfigure(1, weight=1)
left_frame.grid_columnconfigure(0, weight=1)

# === Inside Left Frame: Top Section (Label + Button) ===
top_section = tk.Frame(left_frame, bg="light blue")
top_section.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
top_section.grid_columnconfigure(0, weight=1)
top_section.grid_columnconfigure(1, weight=1)

# Label and Button in the same row
tk.Label(top_section, text="List Tracks", bg="light blue", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=5)
list_tracks_button = tk.Button(top_section, text="List All Tracks")
list_tracks_button.grid(row=0, column=1, sticky="e", padx=5)

# === Tracks Listbox ===
list_tracks_box = tk.Listbox(left_frame, font="Arial", fg="black", bg="light yellow")
list_tracks_box.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Start the GUI event loop
window.mainloop()
