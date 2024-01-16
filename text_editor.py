import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_file(window, text_edit):
    """
    Save the content of the text editor to a file.

    Parameters:
    - window (tk.Tk): The main Tkinter window.
    - text_edit (tk.Text): The Text widget representing the text editor.
    """
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[
                                  ("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, 'w') as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save file: {file_path}")


def open_file(window, text_edit):
    """
    Open a file and load its content into the text editor.

    Parameters:
    - window (tk.Tk): The main Tkinter window.
    - text_edit (tk.Text): The Text widget representing the text editor.
    """
    text_edit.delete(1.0, tk.END)
    file_path = askopenfilename(filetypes=[("Text files", "*.txt")])

    if not file_path:
        print("Error")
        return

    with open(file_path, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open file: {file_path}")


def on_entry_click(event, text_edit):
    """
    Function to handle placeholder text when the Text widget is clicked.

    Parameters:
    - event (tk.Event): The Tkinter event object.
    - text_edit (tk.Text): The Text widget representing the text editor.
    """
    if text_edit.get("1.0", tk.END).strip() == "Write here":
        text_edit.delete("1.0", tk.END)
        text_edit.unbind("<Button-1>", on_entry_click)


def on_focus_out(event, text_edit):
    """
    Function to handle placeholder text when the Text widget loses focus.

    Parameters:
    - event (tk.Event): The Tkinter event object.
    - text_edit (tk.Text): The Text widget representing the text editor.
    """
    if not text_edit.get("1.0", tk.END).strip():
        text_edit.insert("1.0", "Write here")
        text_edit.bind(
            "<Button-1>", lambda event: on_entry_click(event, text_edit))


def main():
    """
    Main function to create and run the text editor application.
    """
    window = tk.Tk()  # Create the main application window
    window.title("Text Editor")  # Set the title of the window

    # Style configurations:
    style = ttk.Style()  # Create a style object for ttk elements
    # Configure a style for a specific ttk element
    style.configure("BW.TLabel", foreground="black")

    # Row and column configurations:
    # Configure the minimum size of the row at index 0
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(0, weight=1)  # Make column 0 expandable

    # Text editor widget:
    text_edit = tk.Text(window, font="Helvetica 19", wrap="word")
    text_edit.grid(row=0, column=0, sticky="nsew")  # Make text_edit expandable

    # Frame for buttons:
    frame = tk.Frame(window, relief=tk.RAISED, bd=5)
    # Save button:
    save_button = ttk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    # Open button:
    open_button = ttk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))

    # Grid placement:
    # Place the frame in the specified row and column with sticky configuration
    frame.grid(row=0, column=1, sticky="ns")
    # Place the Save button in the frame
    save_button.grid(row=0, column=0, sticky="ns")
    # Place the Open button in the frame
    open_button.grid(row=0, column=1, sticky="ns")

    # Placeholder text
    text_edit.insert("1.0", "Write here")
    text_edit.bind(
        "<Button-1>", lambda event: on_entry_click(event, text_edit))
    text_edit.bind("<FocusOut>", lambda event: on_focus_out(event, text_edit))

    # Keybindings:
    # Bind the Save action to Ctrl+s
    window.bind('<Control-s>', lambda event: save_file(window, text_edit))
    # Bind the Open action to Ctrl+o
    window.bind('<Control-o>', lambda event: open_file(window, text_edit))

    # Run the application loop:
    window.mainloop()  # Start the main event loop


# Call the main function to start the application:
main()

# Grid placement explanation:

# window.rowconfigure(0, minsize=400)
# - `window`: The Tkinter main window.
# - `rowconfigure(0, minsize=400)`: This sets the minimum size of the row at index 0 to 400 pixels.

# window.columnconfigure(0, weight=1)
# - `columnconfigure(0, weight=1)`: This makes the column at index 0 expandable, allowing it to take up any available extra space.

# text_edit.grid(row=0, column=0, sticky="nsew")
# - `text_edit`: The Text widget representing the text editor.
# - `row=0`: Specifies that the Text widget should be placed in the 0th row of the grid.
# - `column=0`: Specifies that the Text widget should be placed in the 0th column of the grid.
# - `sticky="nsew"`: This parameter specifies how the Text widget would expand or contract if the cell is larger than the widget.
#   - "nsew" stands for North-South-East-West, meaning the widget will expand in all directions, sticking to all edges of its cell.
#   - This configuration makes the Text widget expand both vertically and horizontally.

# frame.grid(row=0, column=1, sticky="ns")
# - `frame`: The Frame widget that contains the Save and Open buttons.
# - `row=0`: Specifies that the frame should be placed in the 0th row of the grid.
# - `column=1`: Specifies that the frame should be placed in the 1st column of the grid.
# - `sticky="ns"`: This parameter ensures that the frame expands vertically, sticking to the top and bottom edges of its cell.

# save_button.grid(row=0, column=0, sticky="ns")
# - `save_button`: The Save button widget.
# - `row=0`: Specifies that the Save button should be placed in the 0th row of the grid.
# - `column=0`: Specifies that the Save button should be placed in the 0th column of the grid.
# - `sticky="ns"`: Similar to the frame, this parameter ensures that the Save button expands vertically, sticking to the top and bottom edges.

# open_button.grid(row=0, column=1, sticky="ns")
# - `open_button`: The Open button widget.
# - `row=0`: Specifies that the Open button should be placed in the 0th row of the grid.
# - `column=1`: Specifies that the Open button should be placed in the 1st column of the grid.
# - `sticky="ns"`: Similar to the other widgets, this parameter ensures that the Open button expands vertically, sticking to the top and bottom edges.
