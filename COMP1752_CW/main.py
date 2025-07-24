import tkinter as tk # Import tkinter and tk as a new alias
from tkinter import ttk # Import another module from tkinter called ttk to create tabs
import font_manager as fonts # Import font_manager and fonts as a new alias

from view_tracks import TrackViewer # Import TrackViewer Class to connect the components
from create_tracks import CreateTracks # Import CreateTracks Class to connect the components
from update_track import UpdateTracks # Import UpdateTracks Class to connect the components

window = tk.Tk() # Creates a main Tkinter window for the app
window.title("Jukebox") # Title of the main window
window.geometry("800x400") # Size of the main window

fonts.configure() # Calls the "configure" function from fonts
                  # to set a global font styles that will be used throughout the app

notebook = ttk.Notebook(window) # Creates a tab interface widget
notebook.pack(expand=True, fill="both") # This will fill the entire window
                                        # "expand=True" allows the widget to expand to fill any extra space in the parent
                                        # "fill=both" makes it expand both horizontally and vertically

tab1 = tk.Frame(notebook, bg="#444444") # Creates a first frame for the first tab
tab2 = tk.Frame(notebook, bg="#444444") # Creates a second frame for the second tab
tab3 = tk.Frame(notebook, bg="#444444") # Creates a third frame for the third tab

notebook.add(tab1, text="View Tracks") # Adds "tab1" to the notebook widget with a label name View Tracks
notebook.add(tab2, text="Create Playlist") # Adds "tab2" to the notebook widget with a label name Create Playlist
notebook.add(tab3, text="Update Tracks") # Adds "tab3" to the notebook widget with a label name Update Track

TrackViewer(tab1) # Creates an instance of the "TrackViewer" class, passing "tab1" as its parent
                  # This means the GUI elements defined in "TrackViewer" will appear in "tab1" frame
CreateTracks(tab2) # Creates an instance of the "CreateTracks" class, passing "tab2" as its parent
                   # The GUI elements defined in "CreateTracks" will appear in "tab2" frame
UpdateTracks(tab3) # Create an instance of the "UpdateTracks" class, passing "tab3" as its parent
                   # The GUI elements defined in "UpdateTracks" will appear in "tab3" frame

window.mainloop() # This line helps the app to remain open