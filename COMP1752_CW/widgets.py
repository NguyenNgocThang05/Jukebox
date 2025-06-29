import tkinter as tk

class JukeboxWidgets:
    """
    This class is responsible for creating and arranging all the visual components (widgets)
    that make up the Jukebox application's user interface. It acts as a blueprint
    for building the GUI layout.
    """
    def __init__(self, parent, styles):
        """
        Initializes the JukeboxWidgets class.

        Args:
            parent (tk.Tk or tk.Frame): This is the container where these widgets will be placed.
                                        In this application, it will be the main Tkinter window.
            styles (dict): A dictionary containing predefined font, color, and background
                           settings for different types of widgets (e.g., titles, buttons).
        """
        self.parent = parent  # Stores a reference to the parent container.
        self.styles = styles  # Stores the style definitions for consistent appearance.

        # --- Declare all instance attributes here in __init__ ---
        # The main title label that appears at the top of the application.
        self.title_label = None

        # These attributes relate to the widgets found within the left section of the GUI.
        self.left_main_panel_frame = None       # The main frame holding all left-side content.
        self.list_all_tracks_button = None      # Button to show all available tracks.
        self.list_all_tracks_placeholder = None # A list box where current tracks will be displayed.
        self.view_track_entry = None            # Input field for entering a track number to view.
        self.view_track_button = None           # Button to trigger displaying track details.
        self.view_track_placeholder = None      # A text area to show detailed information about a selected track.

        # These attributes relate to the widgets found within the right section of the GUI.
        self.right_main_panel_frame = None      # The main frame holding all right-side content.
        self.create_button = None               # Button to initiate creating a track list.
        self.create_track_entry = None          # Input field for entering track numbers for creation.
        self.create_track_list_placeholder = None # A list box to show custom-created track lists.
        self.update_button = None               # Button to trigger updating a track's details.
        self.update_track_entry = None          # Input field for entering the track number to update.
        self.new_rating_entry = None            # Input field for entering a new rating for a track.

        # The label at the bottom of the window used for displaying status messages.
        self.status_label = None

        # After declaring the attributes, this method is called to actually create
        # and place all the Tkinter widgets onto the screen.
        self.create_widgets()

    def create_widgets(self):
        """
        This method contains all the logic for building the individual Tkinter widgets
        and arranging them on the GUI using the 'grid' layout manager.
        It assigns the created widget objects to the instance attributes declared in __init__.
        """
        # Retrieve specific style dictionaries from the main 'styles' for easier use.
        title_style = self.styles["title"]
        section_style = self.styles["section"]
        button_style = self.styles["button"]
        entry_style = self.styles["entry"]
        text_style = self.styles["text"]

        # --- Title Section ---
        # Creates a large label at the very top of the application window.
        self.title_label = tk.Label(self.parent,  # Parent is the main window
                                    text="Welcome to Jukebox!",  # Text displayed on the label
                                    font=title_style["font"],    # Font style from 'styles'
                                    fg=title_style["fg"],        # Foreground (text) color
                                    bg=title_style["bg"])        # Background color
        # Places the title label using the grid layout manager.
        # row=0: Puts it in the first row of the parent's grid.
        # column=0, columnspan=2: Starts at column 0 and spans across two columns,
        #                         effectively centering it over the left and right panels.
        # sticky="ew": Makes the label expand to fill horizontally (East and West).
        # pady=(10, 20): Adds vertical padding, 10 pixels at the top, 20 at the bottom.
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 20))

        # --- Left Panel: "List of the current tracks" and "View track" sections ---
        # Creates a main frame that will hold all the widgets on the left side of the GUI.
        # It has a distinct background, border, and relief to visually separate it.
        self.left_main_panel_frame = tk.Frame(self.parent, bg="light blue", bd=2, relief="groove")
        # Places this main left frame in row 1, column 0 of the parent's grid.
        # sticky="nsew": Makes the frame expand and fill its cell in all directions (North, South, East, West).
        # padx=10, pady=10: Adds external padding around the frame.
        self.left_main_panel_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # --- "List of the current tracks" sub-section (within the Left Panel) ---
        # Creates a smaller frame specifically for the title and button of this sub-section.
        list_tracks_header_frame = tk.Frame(self.left_main_panel_frame, bg="light blue")
        # Places this header frame in row 0, column 0 of the 'left_main_panel_frame'.
        list_tracks_header_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=(5,0))
        # Configures the grid column within this header frame.
        # columnconfigure(0, weight=1): Makes the first column (where the label is) expand,
        #                              pushing the button to the right.
        list_tracks_header_frame.grid_columnconfigure(0, weight=1)

        # Label for the "List of the current tracks" heading.
        tk.Label(list_tracks_header_frame,
                 text="List of the current tracks",
                 font=section_style["font"],
                 fg=section_style["fg"],
                 bg=section_style["bg"]).grid(row=0, column=0, sticky="w") # sticky="w" aligns text to the west (left)

        # Button labeled "List All Tracks".
        self.list_all_tracks_button = tk.Button(list_tracks_header_frame,
                                                  text="List All Tracks",
                                                  font=button_style["font"],
                                                  fg=button_style["fg"],
                                                  bg=button_style["bg"])
        # Placed next to the label in the header frame.
        self.list_all_tracks_button.grid(row=0, column=1, padx=5, pady=0)

        # Listbox widget where the titles of the available tracks will be displayed.
        # selectmode=tk.SINGLE: Allows only one track to be selected at a time.
        self.list_all_tracks_placeholder = tk.Listbox(
            self.left_main_panel_frame, # Parent is the left_main_panel_frame
            font=text_style["font"],
            fg=text_style["fg"],
            bg=text_style["bg"],
            selectmode=tk.SINGLE
        )
        # Placed in row 1 of the 'left_main_panel_frame'.
        # sticky="nsew": Makes it expand to fill all available space in its cell.
        self.list_all_tracks_placeholder.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)


        # --- "Enter track number" and "View track place holder" sub-section (within the Left Panel) ---
        # Frame to group the label, entry field, and button related to viewing a single track.
        view_track_input_frame = tk.Frame(self.left_main_panel_frame, bg="light blue")
        # Placed in row 2, column 0 of the 'left_main_panel_frame'.
        view_track_input_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        # Configures the column for the entry field within this frame.
        # weight=0: This means this column (where the entry field is) will NOT expand.
        #           The original intention was perhaps for it to expand, but '0' means fixed size.
        view_track_input_frame.grid_columnconfigure(1, weight=0)

        # Label prompting for a track number.
        tk.Label(view_track_input_frame,
                 text="Enter track number",
                 font=entry_style["font"],
                 bg="light blue",
                 fg="black").grid(row=0, column=0, sticky="w")

        # Entry widget for the user to type in the track number they want to view.
        self.view_track_entry = tk.Entry(view_track_input_frame,
                                          font=entry_style["font"],
                                          fg=entry_style["fg"],
                                          bg=entry_style["bg"])
        # Placed in row 0, column 1 of the 'view_track_input_frame'.
        # sticky="ew": Makes it expand horizontally.
        self.view_track_entry.grid(row=0, column=1, sticky="ew", padx=5)

        # Button labeled "View Track".
        self.view_track_button = tk.Button(view_track_input_frame,
                                            text="View Track",
                                            font=button_style["font"],
                                            fg=button_style["fg"],
                                            bg=button_style["bg"])
        # Placed in row 0, column 2 of the 'view_track_input_frame'.
        self.view_track_button.grid(row=0, column=2, padx=5)

        # Text widget to display detailed information about a specific track.
        # It's set with an initial height but will expand if its parent row has weight.
        # wrap="word": Ensures that text wraps at word boundaries, not in the middle of words.
        self.view_track_placeholder = tk.Text(
            self.left_main_panel_frame,
            height=5,
            font=text_style["font"],
            fg=text_style["fg"],
            bg=text_style["bg"],
            wrap="word"
        )
        # Placed in row 3, column 0 of the 'left_main_panel_frame'.
        # sticky="nsew": Makes it expand to fill all available space in its cell.
        self.view_track_placeholder.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)


        # --- Right Panel: "Create Track List" and "Update Tracks" sections ---
        # Creates a main frame that will hold all the widgets on the right side of the GUI.
        # It has a distinct background, border, and relief to visually separate it.
        self.right_main_panel_frame = tk.Frame(self.parent, bg="light yellow", bd=2, relief="groove")
        # Placed in row 1, column 1 of the parent (main window's) grid.
        # sticky="nsew": Makes the frame expand and fill its cell in all directions.
        self.right_main_panel_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)


        # --- "Create Track List" sub-section (within the Right Panel) ---
        # Frame to hold the section title "Create Track List" and "Create" button.
        create_tracks_header_frame = tk.Frame(self.right_main_panel_frame, bg="light yellow")
        # Placed in row 0, column 0 of the 'right_main_panel_frame'.
        create_tracks_header_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=(5,0))
        # Makes the first column (where the label is) expand, pushing the button right.
        create_tracks_header_frame.grid_columnconfigure(0, weight=1)

        # Label for the "Create Track List" heading.
        tk.Label(create_tracks_header_frame,
                 text="Create Track List",
                 font=section_style["font"],
                 fg=section_style["fg"],
                 bg=section_style["bg"]).grid(row=0, column=0, sticky="w")

        # Button labeled "Create".
        self.create_button = tk.Button(create_tracks_header_frame,
                                      text="Create",
                                      font=button_style["font"],
                                      fg=button_style["fg"],
                                      bg=button_style["bg"])
        # Placed next to the label in the header frame.
        self.create_button.grid(row=0, column=1, padx=5, pady=0)

        # Frame for the "Enter track number" label and entry field for creating a track.
        create_entry_frame = tk.Frame(self.right_main_panel_frame, bg="light yellow")
        # Placed in row 1, column 0 of the 'right_main_panel_frame'.
        create_entry_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        # Makes the second column (where the entry field is) expand horizontally.
        create_entry_frame.grid_columnconfigure(1, weight=1)

        # Label for entering track number for creation.
        tk.Label(create_entry_frame,
                 text="Enter track number",
                 font=entry_style["font"],
                 bg="light yellow",
                 fg="black").grid(row=0, column=0, sticky="w")

        # Entry widget for user to input a track number for the new list.
        self.create_track_entry = tk.Entry(create_entry_frame,
                                           font=entry_style["font"],
                                           fg=entry_style["fg"],
                                           bg=entry_style["bg"])
        # Placed in row 0, column 1 of the 'create_entry_frame'.
        self.create_track_entry.grid(row=0, column=1, sticky="ew", padx=5)

        # Label for the "Your Track List" heading, displayed above the custom track listbox.
        tk.Label(self.right_main_panel_frame,
                 text="Your Track List",
                 font=section_style["font"],
                 fg="black",
                 bg="light yellow").grid(row=2, column=0, sticky="w", padx=5, pady=(5,0))

        # Listbox widget where a user's custom track list will be displayed.
        self.create_track_list_placeholder = tk.Listbox(
            self.right_main_panel_frame, # Parent is the right_main_panel_frame
            font=text_style["font"],
            fg=text_style["fg"],
            bg=text_style["bg"],
            selectmode=tk.SINGLE
        )
        # Placed in row 3, column 0 of the 'right_main_panel_frame'.
        # sticky="nsew": Makes it expand to fill all available space.
        self.create_track_list_placeholder.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)


        # --- "Update Tracks" sub-section (within the Right Panel) ---
        # Frame to group the title "Update Tracks" and "Update" button.
        update_tracks_header_frame = tk.Frame(self.right_main_panel_frame, bg="light yellow")
        # Placed in row 4, column 0 of the 'right_main_panel_frame'.
        update_tracks_header_frame.grid(row=4, column=0, sticky="ew", padx=5, pady=(5,0))
        # Makes the first column (where the label is) expand.
        update_tracks_header_frame.grid_columnconfigure(0, weight=1)

        # Label for the "Update Tracks" heading.
        tk.Label(update_tracks_header_frame,
                 text="Update Tracks",
                 font=section_style["font"],
                 fg=section_style["fg"],
                 bg=section_style["bg"]).grid(row=0, column=0, sticky="w")

        # Button labeled "Update".
        self.update_button = tk.Button(update_tracks_header_frame,
                                      text="Update",
                                      font=button_style["font"],
                                      fg=button_style["fg"],
                                      bg=button_style["bg"])
        # Placed next to the label in the header frame.
        self.update_button.grid(row=0, column=1, padx=5, pady=0)

        # Frame for the "Enter track number" label and entry field for updating a track.
        update_track_frame = tk.Frame(self.right_main_panel_frame, bg="light yellow")
        # Placed in row 5, column 0 of the 'right_main_panel_frame'.
        update_track_frame.grid(row=5, column=0, sticky="ew", padx=5, pady=0)
        # Makes the second column (where the entry field is) expand horizontally.
        update_track_frame.grid_columnconfigure(1, weight=1)

        # Label for entering the track number to be updated.
        tk.Label(update_track_frame,
                 text="Enter track number",
                 font=entry_style["font"],
                 bg="light yellow",
                 fg="black").grid(row=0, column=0, sticky="w")

        # Entry widget for user to input the track number to update.
        self.update_track_entry = tk.Entry(update_track_frame,
                                           font=entry_style["font"],
                                           fg=entry_style["fg"],
                                           bg=entry_style["bg"])
        # Placed in row 0, column 1 of the 'update_track_frame'.
        self.update_track_entry.grid(row=0, column=1, sticky="ew", padx=5)

        # Frame for the "New Rating" label and entry field.
        new_rating_frame = tk.Frame(self.right_main_panel_frame, bg="light yellow")
        # Placed in row 6, column 0 of the 'right_main_panel_frame'.
        new_rating_frame.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
        # Makes the second column (where the entry field is) expand horizontally.
        new_rating_frame.grid_columnconfigure(1, weight=1)

        # Label for entering the new rating.
        tk.Label(new_rating_frame,
                 text="New Rating",
                 font=entry_style["font"],
                 bg="light yellow",
                 fg="black").grid(row=0, column=0, sticky="w")

        # Entry widget for user to input the new rating for a track.
        self.new_rating_entry = tk.Entry(new_rating_frame,
                                         font=entry_style["font"],
                                         fg=entry_style["fg"],
                                         bg=entry_style["bg"])
        # Placed in row 0, column 1 of the 'new_rating_frame'.
        self.new_rating_entry.grid(row=0, column=1, sticky="ew", padx=5)


        # --- Status Label at the Bottom ---
        # A label positioned at the very bottom of the main application window.
        # This is typically used to display short messages, errors, or application status.
        self.status_label = tk.Label(
            self.parent, # Parent is the main window
            text="Hello! (This works as a status label)", # Default text
            bd=1, # Border width
            relief=tk.SUNKEN, # Gives a sunken 3D effect to the border
            anchor=tk.W, # Aligns the text to the West (left side) within the label's space
            font=text_style["font"],
            fg=text_style["fg"],
            bg=text_style["bg"]
        )
        # Placed in row 2 of the main window's grid.
        # columnspan=2: Spans across both the left and right columns.
        # sticky="ew": Makes it expand horizontally to fill the width of the window.
        self.status_label.grid(row=2, column=0, columnspan=2, sticky="ew")