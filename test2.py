import tkinter as tk

def create_resizable_example_gui():
    root = tk.Tk()
    root.title("Resizable Grid Example")
    root.geometry("500x300") # Initial size

    # --- Configure Grid Weights ---
    # Row 0: Our "header" row. We don't want it to get taller.
    root.grid_rowconfigure(0, weight=0)

    # Row 1: Our "main content" row. We want it to take all extra vertical space.
    root.grid_rowconfigure(1, weight=1)

    # Column 0: Our "left sidebar" column. It should expand horizontally.
    # We give it a weight of 1.
    root.grid_columnconfigure(0, weight=1)

    # Column 1: Our "main content" column on the right. It should expand horizontally,
    # but we want it to expand *more* than column 0, so we give it a higher weight.
    root.grid_columnconfigure(1, weight=2) # This column will get twice the extra width of column 0

    # --- Create Widgets and Place Them in the Grid ---

    # Label for Row 0 (Header)
    header_label = tk.Label(root, text="This is the Header (Row 0)",
                            bg="lightblue", font=("Arial", 14, "bold"))
    # Placed in row 0, spans both columns, sticks to east/west for internal centering.
    # No sticky="ns" because we explicitly set weight=0 for row 0.
    header_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)


    # Frame for Row 1, Column 0 (Left Panel)
    left_frame = tk.Frame(root, bg="lightcoral", bd=2, relief="solid")
    # Placed in row 1, column 0.
    # sticky="nsew" is crucial here: it makes the frame fill its grid cell,
    # which is expanding due to root.grid_rowconfigure(1, weight=1) and root.grid_columnconfigure(0, weight=1).
    left_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    # Add a label inside the frame to show its boundaries
    tk.Label(left_frame, text="Left Panel (Row 1, Col 0)\nWeight=1",
             bg="lightcoral", font=("Arial", 12)).pack(expand=True)


    # Frame for Row 1, Column 1 (Right Panel)
    right_frame = tk.Frame(root, bg="lightgreen", bd=2, relief="solid")
    # Placed in row 1, column 1.
    # sticky="nsew" makes it fill its grid cell, which is expanding due to its configured weights.
    right_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    # Add a label inside the frame to show its boundaries
    tk.Label(right_frame, text="Right Panel (Row 1, Col 1)\nWeight=2",
             bg="lightgreen", font=("Arial", 12)).pack(expand=True)


    root.mainloop()

if __name__ == "__main__":
    create_resizable_example_gui()