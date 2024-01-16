import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_file(window, text_edit):
    file_path = asksaveasfilename(defaultextension='.txt', filetypes=[
                                  ("Text files", "*.txt")])
    if not file_path:
        print("save not file path")

        return

    with open(file_path, 'w') as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save file: {file_path}")


def open_file(window, text_edit):

    text_edit.delete(1.0, tk.END)
    file_path = askopenfilename(filetypes=[("Text files", "*.txt")])

    if not file_path:
        print("Open not file path")
        return

    with open(file_path, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open file: {file_path}")


def main():
    window = tk.Tk()
    window.title("Text Editor")

    # style configures:
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="black")

    # row and column configure:
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(0)

    text_edit = tk.Text(window, font="Helvatica 19")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=5)
    save_button = ttk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = ttk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))

    frame.grid(row=0, column=0, sticky="ns")
    save_button.grid(row=0, column=0, sticky="ns")
    open_button.grid(row=0, column=1, sticky="ns")

    window.mainloop()


main()
