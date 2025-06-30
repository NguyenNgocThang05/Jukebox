import tkinter as tk
import tkinter.scrolledtext as tkst  # Import the scrolled text module
import font_manager as fonts
import view_tracks as vt
import create_track_list # Import the create_track_list module

window = tk.Tk()
window.title("Jukebox")
window.geometry("1120x600")

fonts.configure()
styles = fonts.get_styles()

title_style = styles["title"]
label_style = styles["label"]
button_style = styles["button"]
entry_style = styles["entry"]
text_style = styles["text"]

# === Main Frame using grid for consistency ===
main_frame = tk.Frame(window)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.configure(bg="#c5f0c5")

# Make the main_frame fill the entire window
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Configure main_frame's grid layout
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# === Title Label ===
title_label = tk.Label(main_frame, text="Welcome to Jukebox!", font=title_style["font"], fg=title_style["fg"], bg=title_style["bg"])
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

# === Left Frame ===
left_frame = tk.Frame(main_frame, bg="light blue", bd=2, relief="groove")
left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
left_frame.grid_rowconfigure(1, weight=3) # Was Listbox row (bigger), now ScrolledText
left_frame.grid_rowconfigure(2, weight=0) # Entry field (fixed height)
left_frame.grid_rowconfigure(3, weight=1) # Was View Track placeholder (smaller), now ScrolledText
left_frame.grid_columnconfigure(0, weight=1)

# === Right Frame ===
right_frame = tk.Frame(main_frame, bg="light blue", bd=2, relief="groove")
right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
right_frame.grid_rowconfigure(1, weight=1) # The 'Your Track List' expands
right_frame.grid_columnconfigure(0 ,weight=1) # Allow Stretching horizontally

# === Inside Left Frame: List Tracks Section ===
# Top Left section
top_left_frame = tk.Frame(left_frame, bg="light blue")
top_left_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
top_left_frame.grid_columnconfigure(0, weight=1)
top_left_frame.grid_columnconfigure(1, weight=0)

# List Tracks: Label and Button placed in same row
list_tracks_label = tk.Label(top_left_frame,text="List Tracks", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
list_tracks_label.grid(row=0, column=0, sticky="w")

list_tracks_button = tk.Button(top_left_frame, text="List All Tracks", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"], command=lambda: vt.list_tracks_clicked(list_tracks_text))
list_tracks_button.grid(row=0, column=1, sticky="e", padx=5)

# --- Change 1: Listbox for List Tracks to ScrolledText ---
list_tracks_text = tkst.ScrolledText(left_frame, bg="light yellow", wrap="word", width=30, height=10) # Added width/height for initial size
list_tracks_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
# Note: You'd use list_tracks_text.insert(tk.END, "track info\n") here
# And list_tracks_text.delete(1.0, tk.END) to clear
# --------------------------------------------------------

# === Inside Left Frame: View Track Section ===
# Bottom Left section
bottom_left_frame = tk.Frame(left_frame, bg="light blue")
bottom_left_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
bottom_left_frame.grid_columnconfigure(1, weight=1)

# View Track Label
view_track_label = tk.Label(bottom_left_frame, text="Enter track number:", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
view_track_label.grid(row=0, column=0, sticky="w", padx=5)

# View Track Entry Field
view_track_entry = tk.Entry(bottom_left_frame, width= 10, font=entry_style["font"], fg=entry_style["fg"], bg=entry_style["bg"])
view_track_entry.grid(row=0, column=1, sticky="w", padx=5)

# View Track Button
view_track_button = tk.Button(bottom_left_frame, text="View Track", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"], command=lambda: vt.view_tracks_clicked(view_track_entry, view_track_text))
view_track_button.grid(row=0, column=2, sticky="e", padx=5)

# --- Change 2: Listbox for View Track to ScrolledText ---
view_track_text = tkst.ScrolledText(left_frame, bg="light yellow", wrap="word", width=30, height=5) # Added width/height for initial size
view_track_text.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
# Note: You'd use view_track_text.insert(tk.END, "track info\n") here
# And view_track_text.delete(1.0, tk.END) to clear
# --------------------------------------------------------

# === Inside Right Frame: Create Track List Section ===
# Top Right section
top_right_frame = tk.Frame(right_frame, bg="light blue")
top_right_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
top_right_frame.grid_columnconfigure(0, weight=1) # Allow column 0 to expand

# Create Track List: Label and Button placed in same row
create_track_label = tk.Label(top_right_frame, text="Create Track List", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
create_track_label.grid(row=0, column=0, sticky="w")

# Modified: Added command to create_track_button
create_track_button = tk.Button(top_right_frame, text="Create", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"], command=lambda: create_track_list.create_track_list_clicked(track_number_entry, create_track_text))
create_track_button.grid(row=0, column=1, sticky="e", padx=5)

# Create Track List: Enter Track Number Entry Field placed in same row
track_number_label = tk.Label(top_right_frame, text="Enter track number:", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
track_number_label.grid(row=1, column=0, sticky="w")

track_number_entry = tk.Entry(top_right_frame, width=10)
track_number_entry.grid(row=1, column=1, sticky="w", padx=5)

# --- Modified Section for Your Tracks List Label, Play Button, Reset Button ---
# Use a sub-frame to group the label and buttons
your_tracks_frame = tk.Frame(top_right_frame, bg="light blue")
your_tracks_frame.grid(row=2, column=0, columnspan=2, sticky="w") # Spanning two columns and sticking to west

your_tracks_label = tk.Label(your_tracks_frame, text="Your Track List:", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
your_tracks_label.grid(row=0, column=0, sticky="w")

# Modified: Added command to play_button
play_button = tk.Button(your_tracks_frame, text="Play", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"], command=lambda: create_track_list.play_track_list(create_track_text))
play_button.grid(row=0, column=1, sticky="w", padx=5) # Stick to west with padding

# Modified: Added command to reset_button
reset_button = tk.Button(your_tracks_frame, text="Reset", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"], command=lambda: create_track_list.reset_playlist(create_track_text))
reset_button.grid(row=0, column=2, sticky="w", padx=5) # Stick to west with padding
# -----------------------------------------------------------------------------

# --- Change 3: Your Track List Listbox to ScrolledText (from previous example) ---
create_track_text = tkst.ScrolledText(right_frame, bg="light yellow", wrap="word", width=40, height=10) # Added width/height for initial size
create_track_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
# Note: You'd use create_track_text.insert(tk.END, "track info\n") here
# And create_track_text.delete(1.0, tk.END) to clear
# --------------------------------------------------------------------------------

# === Inside Right Frame: Update Tracks Section ===
# Bottom Right section
bottom_right_frame = tk.Frame(right_frame, bg="light blue")
bottom_right_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

# Update Tracks: Label and Button placed in same row
update_tracks_label = tk.Label(bottom_right_frame, text="Update Tracks", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
update_tracks_label.grid(row=0, column=0, sticky="w")

update_tracks_button = tk.Button(bottom_right_frame, text="Update", font=button_style["font"], fg=button_style["fg"], bg=button_style["bg"])
update_tracks_button.grid(row=0, column=1, sticky="e", padx=5)

# Update Tracks: 'Enter track number' Label and Entry Field placed in same row
update_entry_label = tk.Label(bottom_right_frame, text="Enter track number:", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
update_entry_label.grid(row=1, column=0, sticky="w")

update_entry = tk.Entry(bottom_right_frame, width=10)
update_entry.grid(row=1, column=1, sticky="W", padx=5)

# Update Tracks: New Rating's Label and Entry Field placed in same row
new_rating_label = tk.Label(bottom_right_frame, text="New Rating:", font=label_style["font"], fg=label_style["fg"], bg=label_style["bg"])
new_rating_label.grid(row=2, column=0, sticky="w")

new_rating_entry = tk.Entry(bottom_right_frame, width=10)
new_rating_entry.grid(row=2, column=1, sticky="w", padx=5)


# Start the GUI event loop
window.mainloop()