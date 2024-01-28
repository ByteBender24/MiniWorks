from pytube import YouTube
from tkinter import filedialog
from gui import window as gui_window
from gui import url_entry, format_entry


def download_video(url, save_path, file_ext="mp4"):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension=file_ext)
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


def run_gui_and_download():
    try:
        gui_window.mainloop()  # Run the GUI window
        save_dir = open_file_dialog()

        if save_dir:
            print("Started download...")
            print(url_entry, format_entry)
            download_video(url_entry,
                           save_dir, format_entry)
        else:
            print("Enter correct file path")
    except:
        print("Unexpected Error occured....Please Try Again")


if __name__ == "__main__":
    run_gui_and_download()
