import tkinter as tk
import font_manager as fonts
from widgets import JukeboxWidgets

class JukeboxGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1120x600")
        self.window.title("Jukebox")
        self.window.configure(bg="light pink")
        self.window.resizable(False, False)

        # Configure default Tkinter fonts using your font_manager
        fonts.configure()
        # Get custom styles dictionary
        self.styles = fonts.get_styles()

        # Create an instance of JukeboxWidgets, passing the main window and styles
        self.jukebox_widgets = JukeboxWidgets(self.window, self.styles)

        # --- Configure main window's grid weights ---
        # These weights apply to the rows/columns directly managed by self.window
        self.window.grid_rowconfigure(1, weight=1) # Row for left/right panels
        self.window.grid_columnconfigure(0, weight=1) # Left column
        self.window.grid_columnconfigure(1, weight=1) # Right column

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = JukeboxGUI()
    app.run()