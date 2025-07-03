import tkinter as tk
from tkinter import ttk # For themed widgets, often looks better

def get_selection():
    print(f"Selected option: {selected_option.get()}")

root = tk.Tk()
root.title("User-Friendly Radio Buttons (Tkinter)")
root.geometry("400x250")
root.configure(bg="#2E2E2E") # Dark background for the window

selected_option = tk.StringVar()
selected_option.set("Option A") # Default selection

# --- Styling (User-Friendly Appearance) ---
# Using ttk.Style for more modern look and easier configuration
style = ttk.Style()
style.theme_use('clam') # 'clam', 'alt', 'default', 'classic' - try different themes

# Customize Radiobutton for a dark theme
style.configure(
    "DarkTheme.TRadiobutton",
    background="#2E2E2E",      # Dark background for the button area
    foreground="#FFFFFF",      # White text for unselected
    font=("Arial", 12),
    indicatorforeground="#00BFFF", # Color of the circle/indicator when unselected
                                # Only visible if indicatoron=1 (default)
)
style.map(
    "DarkTheme.TRadiobutton",
    background=[('active', '#555555'), ('selected', '#00BFFF')], # Hover & Selected bg
    foreground=[('selected', '#000000')], # Black text for selected, or stay white
    indicatorforeground=[('selected', '#00BFFF')] # Circle color when selected
)


# --- Radio Buttons ---
rb1 = ttk.Radiobutton(
    root,
    text="Option A: Recommended",
    variable=selected_option,
    value="Option A",
    command=get_selection,
    style="DarkTheme.TRadiobutton"
)
rb1.pack(pady=5, anchor="w", padx=20)

rb2 = ttk.Radiobutton(
    root,
    text="Option B: Advanced Settings",
    variable=selected_option,
    value="Option B",
    command=get_selection,
    style="DarkTheme.TRadiobutton"
)
rb2.pack(pady=5, anchor="w", padx=20)

rb3 = ttk.Radiobutton(
    root,
    text="Option C: Legacy Mode",
    variable=selected_option,
    value="Option C",
    command=get_selection,
    style="DarkTheme.TRadiobutton"
)
rb3.pack(pady=5, anchor="w", padx=20)

# Example using regular tk.Radiobutton with indicatoron=0 for full custom background
# You can make these look more like toggle buttons
tk_rb_custom = tk.Radiobutton(
    root,
    text="Custom Toggle",
    variable=selected_option,
    value="Custom",
    indicatoron=0, # This makes the entire button clickable and colorable
    width=20,
    padx=10,
    pady=5,
    font=("Arial", 10, "bold"),
    bg="#444444",       # Unselected background
    fg="#EEEEEE",       # Unselected foreground
    selectcolor="#00BFFF", # Background when selected
    activebackground="#666666", # Hover background
    activeforeground="#FFFFFF", # Hover foreground
    relief="raised", # Give it a button-like feel
    bd=2, # Border width
    command=get_selection
)
tk_rb_custom.pack(pady=15)


# A button to show the current selection
select_button = tk.Button(
    root,
    text="Check Selection",
    command=get_selection,
    bg="#555555",
    fg="#FFFFFF",
    font=("Arial", 10)
)
select_button.pack(pady=10)

root.mainloop()