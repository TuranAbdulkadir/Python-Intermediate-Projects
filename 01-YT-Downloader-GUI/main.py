import customtkinter as ctk
from pytubefix import YouTube

def download():
    try:
        url = entry.get()
        yt = YouTube(url)
        status.configure(text=f"Downloading: {yt.title}...", text_color="yellow")
        yt.streams.get_highest_resolution().download()
        status.configure(text="✅ Download Complete!", text_color="green")
    except Exception as e:
        status.configure(text=f"Error: {e}", text_color="red")

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("500x300")
root.title("YouTube Downloader")

ctk.CTkLabel(root, text="YouTube Video Downloader", font=("Arial", 20)).pack(pady=20)
entry = ctk.CTkEntry(root, width=350, placeholder_text="Enter YouTube Video URL")
entry.pack(pady=10)
ctk.CTkButton(root, text="Download", command=download).pack(pady=20)
status = ctk.CTkLabel(root, text="")
status.pack()

root.mainloop()