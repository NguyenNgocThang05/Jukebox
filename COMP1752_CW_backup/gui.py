import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import view_tracks as vt

class JukeboxApp:
    def __init__(self, window):
        self.window = window
        window.title("Jukebox")
        window.geometry("1120x600")

        # 1. Initialize Styles
        self._configure_styles()

        # 2. Setup Main Window Layout
        self._setup_main_window_layout()

        # 3. Create Main UI Components
        self._create_main_frame()
        self._create_title_label()
        self._create_left_frame_content()
        self._create_right_frame_content()

    def _configure_styles(self):
        """Configures fonts and loads styles into instance variables."""
        fonts.configure()
        styles = fonts.get_styles()
        self.title_style = styles["title"]
        self.label_style = styles["label"]
        self.button_style = styles["button"]
        self.entry_style = styles["entry"]

    def _setup_main_window_layout(self):
        """Configures the grid weights for the main window to be responsive."""
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

    def _create_main_frame(self):
        """Creates and configures the main frame that holds left and right sections."""
        self.main_frame = tk.Frame(self.window, bg="#c5f0c5")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_rowconfigure(1, weight=1) # Row for left/right frames
        self.main_frame.grid_columnconfigure(0, weight=1) # Column for left frame
        self.main_frame.grid_columnconfigure(1, weight=1) # Column for right frame

    def _create_title_label(self):
        """Creates the main application title label."""
        title_label = tk.Label(self.main_frame, text="Welcome to Jukebox!",
                                font=self.title_style["font"], fg=self.title_style["fg"],
                                bg=self.title_style["bg"])
        title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    def _create_left_frame_content(self):
        """Creates and populates the left frame with List Tracks and View Track sections."""
        self.left_frame = tk.Frame(self.main_frame, bg="light blue", bd=2, relief="groove")
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Configure left_frame grid weights for content areas
        self.left_frame.grid_rowconfigure(1, weight=3) # List Tracks ScrolledText (more height)
        self.left_frame.grid_rowconfigure(3, weight=1) # View Track ScrolledText (less height)
        self.left_frame.grid_columnconfigure(0, weight=1) # Single column, expands horizontally

        self._add_list_tracks_section(self.left_frame)
        self._add_view_track_section(self.left_frame)

    def _add_list_tracks_section(self, parent_frame):
        """Adds the 'List Tracks' section to the specified parent frame."""
        list_section = tk.Frame(parent_frame, bg="light blue")
        list_section.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        list_section.grid_columnconfigure(0, weight=1) # Label column expands
        list_section.grid_columnconfigure(1, weight=0) # Button column is fixed

        tk.Label(list_section, text="List Tracks", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=0, column=0, sticky="w")

        # ScrolledText needs to be an instance variable if accessed by commands
        self.list_tracks_text = tkst.ScrolledText(parent_frame, bg="light yellow",
                                                  wrap="word", width=30, height=10)
        self.list_tracks_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        tk.Button(list_section, text="List All Tracks", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"],
                 command=lambda: vt.list_tracks_clicked(self.list_tracks_text)).grid(row=0, column=1, sticky="e", padx=5)

    def _add_view_track_section(self, parent_frame):
        """Adds the 'View Track' section to the specified parent frame."""
        view_section = tk.Frame(parent_frame, bg="light blue")
        view_section.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        view_section.grid_columnconfigure(1, weight=1) # Entry field column expands

        tk.Label(view_section, text="Enter track number:", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=0, column=0, sticky="w")

        # Entry needs to be an instance variable if accessed by commands
        self.view_track_entry = tk.Entry(view_section, width=10, font=self.entry_style["font"],
                                         fg=self.entry_style["fg"], bg=self.entry_style["bg"])
        self.view_track_entry.grid(row=0, column=1, sticky="w", padx=5)

        # ScrolledText needs to be an instance variable if accessed by commands
        self.view_track_text = tkst.ScrolledText(parent_frame, bg="light yellow",
                                                 wrap="word", width=30, height=5)
        self.view_track_text.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

        tk.Button(view_section, text="View Track", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"],
                 command=lambda: vt.view_tracks_clicked(self.view_track_entry, self.view_track_text)).grid(row=0, column=2, sticky="e", padx=5)

    def _create_right_frame_content(self):
        """Creates and populates the right frame with Create Track List and Update Tracks sections."""
        self.right_frame = tk.Frame(self.main_frame, bg="light blue", bd=2, relief="groove")
        self.right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        # Configure right_frame grid weights for content areas
        self.right_frame.grid_rowconfigure(1, weight=1) # Track List ScrolledText area
        self.right_frame.grid_columnconfigure(0, weight=1) # Single column, expands horizontally

        self._add_create_track_list_section(self.right_frame)
        self._add_update_tracks_section(self.right_frame)

    def _add_create_track_list_section(self, parent_frame):
        """Adds the 'Create Track List' section to the specified parent frame."""
        create_section = tk.Frame(parent_frame, bg="light blue")
        create_section.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        # Column configuration for 'create_section' itself
        create_section.grid_columnconfigure(0, weight=0) # Labels/first elements
        create_section.grid_columnconfigure(1, weight=0) # Entries/second elements
        create_section.grid_columnconfigure(2, weight=0) # Buttons/third elements
        create_section.grid_columnconfigure(3, weight=1) # Spacer column to push content left

        tk.Label(create_section, text="Create Track List", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=0, column=0, sticky="w")

        tk.Button(create_section, text="Create", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"]).grid(row=0, column=1, sticky="w", padx=(5, 0))

        tk.Label(create_section, text="Enter track number:", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=1, column=0, sticky="w")

        self.track_number_entry = tk.Entry(create_section, width=10)
        self.track_number_entry.grid(row=1, column=1, sticky="w", padx=(5, 0))

        # --- Track Control Buttons Group (using an internal frame for precise alignment) ---
        track_control_frame = tk.Frame(create_section, bg="light blue")
        # This frame spans across all 4 columns of create_section and aligns to the west
        track_control_frame.grid(row=2, column=0, columnspan=4, sticky="w", pady=5)

        tk.Label(track_control_frame, text="Your Track List:", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=0, column=0, sticky="w")

        tk.Button(track_control_frame, text="Play", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"]).grid(row=0, column=1, sticky="w", padx=(10, 0))

        tk.Button(track_control_frame, text="Reset", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"]).grid(row=0, column=2, sticky="w", padx=(5, 0))
        # --- End Track Control Buttons Group ---

        # ScrolledText needs to be an instance variable
        self.create_track_text = tkst.ScrolledText(parent_frame, bg="light yellow",
                                                   wrap="word", width=40, height=10)
        self.create_track_text.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    def _add_update_tracks_section(self, parent_frame):
        """Adds the 'Update Tracks' section to the specified parent frame."""
        update_section = tk.Frame(parent_frame, bg="light blue")
        update_section.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        # Configure columns for this frame
        update_section.grid_columnconfigure(0, weight=0) # Labels
        update_section.grid_columnconfigure(1, weight=0) # Entries/Buttons
        update_section.grid_columnconfigure(2, weight=1) # Spacer to push content left

        tk.Label(update_section, text="Update Tracks", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=0, column=0, sticky="w")

        tk.Button(update_section, text="Update", font=self.button_style["font"],
                 fg=self.button_style["fg"], bg=self.button_style["bg"]).grid(row=0, column=1, sticky="w", padx=(5, 0))

        tk.Label(update_section, text="Enter track number:", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=1, column=0, sticky="w")

        self.update_entry = tk.Entry(update_section, width=10)
        self.update_entry.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(update_section, text="New Rating:", font=self.label_style["font"],
                 fg=self.label_style["fg"], bg=self.label_style["bg"]).grid(row=2, column=0, sticky="w")

        self.new_rating_entry = tk.Entry(update_section, width=10)
        self.new_rating_entry.grid(row=2, column=1, sticky="w", padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = JukeboxApp(root)
    root.mainloop()