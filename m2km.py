from ttkbootstrap as ttk
import tkinter as tk


def convert():
    try:
        mile_input = entry_int.get()
        if mile_input < 0:
            output_string.set("Please enter a positive number!")
        else:
            km_output = mile_input * 1.60934
            output_string.set(km_output)
    except tk.TclError:
        output_string.set(
            "Enter a number, other characters are not supported!")


# window
window = ttk.Window(themename="darkly")
window.title("Convertor")

# label
label = ttk.Label(master=window, text="Miles to Kilometers",
                  font="Calibri 24 bold")
label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.DoubleVar()
entry = ttk.Entry(master=input_frame,
                  textvariable=entry_int)
button = ttk.Button(master=input_frame,
                    text="Convert",
                    command=convert)
input_frame.pack(pady=10)
entry.pack(side="left", padx=10)
button.pack(side="right")

# output field
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text="Output",
    font="Calibri 24 italic",
    textvariable=output_string)
output_label.pack(pady=5)

# mainloop
window.mainloop()
