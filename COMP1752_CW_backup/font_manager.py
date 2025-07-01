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
            "font": ("Segoe UI", 24, "bold"),
            "fg": "white",
            "bg": "#000000"
        },

        "label": {
            "font": ("Segoe UI", 13, "normal"),
            "fg": "#424242",
            "bg": "#DCEDC8"
        },

        "button": {
            "font": ("Segoe UI", 11, "normal"),
            "fg": "white",
            "bg": "#1A73E8"
        },

        "entry": {
            "font": ("Arial", 11, "normal"),
            "fg": "212121",
            "bg": "#1976D2"
        },

        "text": {
            "font": ("Segoe UI", 11, "normal"),
            "fg": "#212121",
            "bg": "white"
        },

        "status": {
            "font": ("Segoe UI", 9, "italic"),
            "fg": "#E0E0E0",
            "bg": "white"
        }
    }

