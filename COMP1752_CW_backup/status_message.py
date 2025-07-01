import tkinter as tk

class StatusManager:
    """
    Manages the app's status label
    It allows to display messages that stay on screen until a new message is called.
    """

    _status_label = None

    @classmethod
    def set_label_widget(cls, label_widget):
        """
        Sets up which Tkinter Label widget will be used to show messages.
        Needs to call this once when the app starts up.
        """

        cls._status_label = label_widget

    @classmethod
    def update_message(cls, message):
        """
        Changes the text displayed on the status label
        The new message will stay visible until this function is called again
        with a different message/
        :param message: The text(string) that will be display
        """

        if cls._status_label is None:
            # This message will appear in the console if set_label_widget wasn't called.
            print("Error: Status label not set up!")
            return

        # Update the text of the Tkinter label widget
        cls._status_label.config(text=message)