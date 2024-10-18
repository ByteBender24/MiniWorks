import pyperclip
import tkinter as tk
import os
import time
import threading

class ClipboardManager:
    def __init__(self, master):
        self.master = master
        master.title("Clipboard Manager")

        # Set fixed size for the window
        master.geometry("200x200")  # Width x Height

        self.clip_history = []
        self.log_file = "clipboard_history.txt"

        # Load history from log file
        self.load_history()

        # Frame to hold the clipboard items
        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        self.history_display = tk.Frame(self.frame)
        self.history_display.pack(fill=tk.BOTH, expand=True)

        # Start the clipboard monitor
        self.previous_clip = ""
        self.running = True
        threading.Thread(target=self.monitor_clipboard, daemon=True).start()

        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_history(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                self.clip_history = f.read().splitlines()

    def save_history(self):
        with open(self.log_file, "w") as f:
            for item in self.clip_history:
                f.write(f"{item}\n")

    def add_clip_item(self, text):
        clip_frame = tk.Frame(self.history_display, borderwidth=2, relief=tk.RAISED)
        clip_frame.pack(pady=2, fill=tk.X)

        label = tk.Label(clip_frame, text=text[:30] + '...' if len(text) > 30 else text, padx=10, pady=5)
        label.pack(side=tk.LEFT)

        # Bind click event to copy full text to clipboard
        label.bind("<Button-1>", lambda e: self.copy_full_text(text))

        self.history_display.update_idletasks()

    def monitor_clipboard(self):
        while self.running:
            current_clip = pyperclip.paste()
            if current_clip != self.previous_clip:
                self.previous_clip = current_clip
                if current_clip not in self.clip_history:
                    self.clip_history.append(current_clip)
                    self.save_history()
                    self.add_clip_item(current_clip)
            time.sleep(1)  # Check the clipboard every second

    def copy_full_text(self, text):
        pyperclip.copy(text)  # Copy the full text to the clipboard

    def on_closing(self):
        self.running = False
        self.save_history()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    clipboard_manager = ClipboardManager(root)
    root.mainloop()
