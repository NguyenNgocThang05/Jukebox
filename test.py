import tkinter as tk

root = tk.Tk()
root.geometry("400x200") # A wider window

# Without fill=tk.X
label1 = tk.Label(root, text="I'm a short label", bg="lightblue")
label1.pack(pady=10) # No fill specified

# With fill=tk.X
label2 = tk.Label(root, text="I'm a label that fills horizontally", bg="lightgreen")
label2.pack(fill=tk.X, pady=10) # Fills horizontally

root.mainloop()