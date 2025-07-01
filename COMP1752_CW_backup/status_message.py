# status_message.py
import tkinter as tk

class StatusManager:
    _label_widget = None

    @classmethod
    def set_label_widget(cls, label):
        cls._label_widget = label

    @classmethod
    def update_status(cls, message):
        if cls._label_widget:
            cls._label_widget.config(text=message)