import tkinter.font as tkfont

def configure():
    """
    Set global font styles for default widgets
    """
    family = "Helvetica"

    # Configure default fonts used by Tkinter widgets
    tkfont.nametofont("TkDefaultFont").configure(size=12, family=family)
    tkfont.nametofont("TkTextFont").configure(size=12, family=family)
    tkfont.nametofont("TkFixedFont").configure(size=12, family=family)

def get_styles():
    """
    Returns a dictionary of customs widget styles including fonts, foreground, and background
    """
    return {
        "title": {
            "font": ("Arial", 24, "bold"),
            "fg": "blue",
            "bg": "light green"
        },

        "section": {
            "font": ("Arial", 14, "bold"),
            "fg": "black",
            "bg": "light pink"
        },

        "button": {
            "font": ("Arial", 12, "bold"),
            "fg": "white",
            "bg": "green"
        },

        "entry": {
            "font": ("Arial", 12),
            "fg": "black",
            "bg": "white"
        },

        "text": {
            "font": ("Arial", 12),
            "fg": "dark red",
            "bg": "beige"
        }
    }

