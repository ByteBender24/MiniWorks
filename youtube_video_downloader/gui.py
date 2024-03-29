
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

url_entry = ""
format_entry = ""

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_data():

    global url_entry
    global format_entry

    url_entry = entry_1.get()
    format_entry = entry_2.get().lower()

    print("URL:", url_entry)
    print("Format:", format_entry)

    window.destroy()


window = Tk()

window.title("YT video Downloader")
window.geometry("537x352")
window.configure(bg="#E1C1C1")


canvas = Canvas(
    window,
    bg="#E1C1C1",
    height=352,
    width=537,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    537.0,
    68.0,
    fill="#3936AD",
    outline="")

canvas.create_text(
    31.0,
    20.0,
    anchor="nw",
    text="Youtube Video Downloader",
    fill="#FFFFFF",
    font=("Monda Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    276.5,
    154.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F0E6E6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=110.0,
    y=132.0,
    width=333.0,
    height=42.0
)

canvas.create_text(
    101.0,
    102.0,
    anchor="nw",
    text="Enter Youtube Link Here:",
    fill="#1E1E1E",
    font=("Monda Bold", 17 * -1)
)

canvas.create_text(
    101.0,
    198.0,
    anchor="nw",
    text="Mp4 Or Mp3",
    fill="#011F19",
    font=("Monda Bold", 17 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    157.0,
    253.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#ECE2E2",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=110.0,
    y=233.0,
    width=94.0,
    height=38.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_data(),
    relief="flat"
)
button_1.place(
    x=291.0,
    y=212.0,
    width=167.0,
    height=61.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    485.0,
    244.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    492.0,
    34.0,
    image=image_image_2
)


window.resizable(False, False)
window.mainloop()
