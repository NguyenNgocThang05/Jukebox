import tkinter.font as tkfont

def configure():
    """
    Defines a function named configure.
    This function work as a default font settings for the main app
    """
    # family = "Segoe UI" # An alternative font family but was commented out
    family = "Helvetica" # Primary font family used for the main app's fonts

    default_font = tkfont.nametofont("TkDefaultFont")
    # Retrieves the default font object
    default_font.configure(size=15, family=family)
    # sets the font size to 15 and the font family to Helvetica
    text_font = tkfont.nametofont("TkTextFont")
    # Text font is used for text widgets
    text_font.configure(size=12, family=family)
    # Sets the text font size to 12 and the font family to Helvetica
    fixed_font = tkfont.nametofont("TkFixedFont")
    # Fixed width fonts used for displaying code or data where character alignment is important
    fixed_font.configure(size=12, family=family)
    # Sets the font size to 12 and the font family to Helvetica